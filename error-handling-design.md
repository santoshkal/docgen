# Agent Error Handling Design

**Purpose**: Design robust error handling mechanism for parallel documentation agents
**Date**: 2025-11-24

---

## 📊 Error Classification

### Category 1: Transient/Recoverable Errors (RETRY)
These errors are temporary and may succeed on retry.

| Error Type | Example | Retry Strategy |
|------------|---------|----------------|
| Rate Limit | `429 Too Many Requests` | Exponential backoff (30s → 60s → 120s) |
| Timeout | `Request timeout after 60s` | Immediate retry (up to 3x) |
| Network Glitch | `Connection reset by peer` | Immediate retry (up to 3x) |
| Server Overload | `503 Service Unavailable` | Exponential backoff |
| Temporary API Issue | `500 Internal Server Error` | Wait 10s, retry |

### Category 2: LLM Quality Errors (RETRY WITH CORRECTION)
These errors are due to suboptimal LLM responses that can be improved with follow-up prompts.

| Error Type | Detection Method | Correction Strategy |
|------------|------------------|---------------------|
| Incomplete Code Block | Missing closing ``` or truncated | "Please complete the code block starting from line X" |
| Invalid Mermaid Syntax | Mermaid parser fails | "The diagram has syntax error: {error}. Please fix and regenerate" |
| Missing Required Section | Section header not found | "Section '{name}' is missing. Please generate it following the template" |
| Hallucinated Content | References non-existent paragraphs | "Paragraph {name} doesn't exist in metadata. Please use only: {valid_list}" |
| Incomplete Coverage | Coverage < threshold | "Code explanation only covers {X}%. Please include lines {missing_ranges}" |
| Wrong Format | JSON expected but got prose | "Please respond in JSON format as specified: {format_example}" |
| Exceeded Token Limit | Response truncated | "Response was truncated. Please summarize more concisely" |

### Category 3: Permanent/Fatal Errors (EXIT IMMEDIATELY)
These errors won't be fixed by retrying and require human intervention.

| Error Type | Example | Action |
|------------|---------|--------|
| Authentication | `401 Invalid API Key` | Exit, notify user to check credentials |
| Authorization | `403 Access Denied` | Exit, notify user about permissions |
| Invalid Model | `Model 'gpt-5' not found` | Exit, notify user to check model name |
| Quota Exceeded | `402 Payment Required` | Exit, notify user about billing |
| File Not Found | Source file doesn't exist | Skip file, log error, continue with others |
| Metadata Missing | Required metadata file absent | Skip file, log error, continue with others |
| Configuration Error | Invalid YAML syntax | Exit, notify user to fix config |
| Out of Memory | `MemoryError` | Exit, suggest smaller batch size |

### Category 4: Partial Success (LOG AND CONTINUE)
The agent completed but with warnings or incomplete results.

| Scenario | Action |
|----------|--------|
| 80% coverage achieved (below 95% target) | Accept result, log warning |
| 1 of 12 sections failed | Include successful sections, mark failed section |
| Diagram generation failed | Include document without diagram, log warning |
| Inter-file relationships unavailable | Skip section, note in output |

---

## 🔄 Retry Strategy Patterns

### Pattern 1: Exponential Backoff with Jitter (For Rate Limits)

```python
import random
import time

def exponential_backoff_with_jitter(attempt: int, base_delay: float = 1.0, max_delay: float = 120.0) -> float:
    """
    Calculate delay with exponential backoff and random jitter.
    Jitter prevents thundering herd when multiple agents retry simultaneously.
    """
    # Exponential: 1s, 2s, 4s, 8s, 16s, 32s, 64s, 120s (capped)
    delay = min(base_delay * (2 ** attempt), max_delay)

    # Add jitter: ±25% randomization
    jitter = delay * 0.25 * (random.random() * 2 - 1)

    return delay + jitter

# Usage
for attempt in range(max_retries):
    try:
        result = call_llm(prompt)
        break
    except RateLimitError:
        delay = exponential_backoff_with_jitter(attempt)
        logger.warning(f"Rate limited, waiting {delay:.1f}s before retry {attempt + 1}")
        time.sleep(delay)
```

### Pattern 2: Corrective Retry (For LLM Quality Issues)

```python
def retry_with_correction(
    original_prompt: str,
    original_response: str,
    error_info: dict,
    llm: ChatModel
) -> str:
    """
    Retry LLM call with corrective follow-up prompt.
    """
    correction_prompt = build_correction_prompt(error_info)

    messages = [
        {"role": "system", "content": original_prompt},
        {"role": "assistant", "content": original_response},
        {"role": "user", "content": correction_prompt}
    ]

    return llm.invoke(messages)

def build_correction_prompt(error_info: dict) -> str:
    """
    Build context-aware correction prompt based on error type.
    """
    error_type = error_info["type"]

    prompts = {
        "incomplete_code": f"""
Your previous response was incomplete. The code block was truncated.
Please continue from where you stopped and complete the remaining code.
Last line received: {error_info.get('last_line', 'unknown')}
Expected to cover lines: {error_info.get('expected_range', 'all')}
""",

        "invalid_mermaid": f"""
The Mermaid diagram you generated has a syntax error:
Error: {error_info.get('mermaid_error', 'unknown')}

Please regenerate the diagram with valid Mermaid syntax.
Common issues: missing quotes around labels with spaces, invalid node IDs, unclosed brackets.
""",

        "missing_section": f"""
Your response is missing the required section: "{error_info.get('section_name')}"

Please generate this section following the template structure provided.
""",

        "hallucination": f"""
Your response references content that doesn't exist in the metadata:
- Referenced: {error_info.get('referenced_item')}
- Valid options: {error_info.get('valid_items')}

Please regenerate using only the actual data from the metadata provided.
""",

        "low_coverage": f"""
Your code explanation only covers {error_info.get('coverage', 0)}% of the source code.
Target coverage is {error_info.get('target', 95)}%.

Missing line ranges: {error_info.get('missing_ranges', [])}

Please include explanations for the missing code sections.
""",

        "wrong_format": f"""
Your response was not in the expected format.
Expected: {error_info.get('expected_format', 'structured output')}
Received: {error_info.get('received_format', 'prose')}

Please reformat your response according to the specification.
"""
    }

    return prompts.get(error_type, "Please review and correct your previous response.")
```

### Pattern 3: Circuit Breaker (For System-Wide Issues)

```python
from datetime import datetime, timedelta
from enum import Enum

class CircuitState(Enum):
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Failing, reject requests
    HALF_OPEN = "half_open"  # Testing if recovered

class CircuitBreaker:
    """
    Circuit breaker prevents cascading failures.
    If too many agents fail, stop spawning new ones.
    """

    def __init__(
        self,
        failure_threshold: int = 5,      # Failures before opening
        recovery_timeout: int = 60,       # Seconds before trying again
        success_threshold: int = 2        # Successes to close circuit
    ):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.success_threshold = success_threshold

        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time = None

    def can_execute(self) -> bool:
        """Check if we should allow execution."""
        if self.state == CircuitState.CLOSED:
            return True

        if self.state == CircuitState.OPEN:
            # Check if recovery timeout passed
            if datetime.now() - self.last_failure_time > timedelta(seconds=self.recovery_timeout):
                self.state = CircuitState.HALF_OPEN
                return True
            return False

        # HALF_OPEN: Allow limited requests to test
        return True

    def record_success(self):
        """Record successful execution."""
        if self.state == CircuitState.HALF_OPEN:
            self.success_count += 1
            if self.success_count >= self.success_threshold:
                self.state = CircuitState.CLOSED
                self.failure_count = 0
                self.success_count = 0

    def record_failure(self, error: Exception):
        """Record failed execution."""
        self.failure_count += 1
        self.last_failure_time = datetime.now()

        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN
            logger.error(f"Circuit OPEN: {self.failure_count} consecutive failures")

# Usage in orchestrator
circuit_breaker = CircuitBreaker(failure_threshold=5)

def spawn_agent(file_path: str):
    if not circuit_breaker.can_execute():
        logger.warning(f"Circuit open, skipping {file_path}")
        return None

    try:
        result = run_documentation_agent(file_path)
        circuit_breaker.record_success()
        return result
    except Exception as e:
        circuit_breaker.record_failure(e)
        raise
```

---

## 🏗️ Recommended Error Handling Architecture

### Layer 1: Agent-Level Error Handler

Each agent has its own error handler for LLM-specific errors.

```python
class AgentErrorHandler:
    """
    Handles errors within a single documentation agent.
    """

    def __init__(self, agent_id: str, file_path: str, config: dict):
        self.agent_id = agent_id
        self.file_path = file_path
        self.max_retries = config.get("max_retries", 3)
        self.max_corrections = config.get("max_corrections", 2)

    def execute_with_retry(self, operation: Callable, operation_name: str) -> Result:
        """
        Execute operation with intelligent retry logic.
        """
        last_error = None

        for attempt in range(self.max_retries):
            try:
                result = operation()

                # Validate result quality
                validation = self.validate_result(result, operation_name)

                if validation.is_valid:
                    return Result.success(result)

                # Quality issue - try correction
                if validation.is_correctable and attempt < self.max_corrections:
                    result = self.attempt_correction(result, validation)
                    if self.validate_result(result, operation_name).is_valid:
                        return Result.success(result)

                # Accept partial result if it meets minimum threshold
                if validation.meets_minimum_threshold:
                    return Result.partial_success(result, validation.warnings)

            except RateLimitError as e:
                delay = exponential_backoff_with_jitter(attempt)
                logger.warning(f"[{self.agent_id}] Rate limited, waiting {delay:.1f}s")
                time.sleep(delay)
                last_error = e

            except TransientError as e:
                logger.warning(f"[{self.agent_id}] Transient error: {e}, retrying...")
                time.sleep(1)
                last_error = e

            except FatalError as e:
                # Don't retry fatal errors
                logger.error(f"[{self.agent_id}] Fatal error: {e}")
                return Result.failure(e, retryable=False)

            except Exception as e:
                logger.error(f"[{self.agent_id}] Unexpected error: {e}")
                last_error = e

        # All retries exhausted
        return Result.failure(last_error, retryable=True)
```

### Layer 2: Orchestrator-Level Error Handler

Orchestrator manages errors across all agents.

```python
class OrchestratorErrorHandler:
    """
    Manages errors across all agents in the orchestrator.
    """

    def __init__(self, config: dict):
        self.circuit_breaker = CircuitBreaker(
            failure_threshold=config.get("circuit_breaker_threshold", 5)
        )
        self.failed_files = []
        self.partial_files = []
        self.continue_on_failure = config.get("continue_on_failure", True)
        self.max_failure_rate = config.get("max_failure_rate", 0.2)  # 20%

    def handle_agent_result(self, agent_id: str, file_path: str, result: Result):
        """
        Process result from an agent.
        """
        if result.is_success:
            self.circuit_breaker.record_success()
            return AgentAction.CONTINUE

        elif result.is_partial_success:
            self.partial_files.append({
                "file": file_path,
                "agent_id": agent_id,
                "warnings": result.warnings
            })
            self.circuit_breaker.record_success()  # Partial is still success
            return AgentAction.CONTINUE

        else:  # Failure
            self.failed_files.append({
                "file": file_path,
                "agent_id": agent_id,
                "error": str(result.error),
                "retryable": result.retryable
            })
            self.circuit_breaker.record_failure(result.error)

            # Check if we should stop everything
            if not self.continue_on_failure:
                return AgentAction.STOP_ALL

            # Check failure rate
            total_processed = len(self.failed_files) + len(self.partial_files) + self.success_count
            failure_rate = len(self.failed_files) / max(total_processed, 1)

            if failure_rate > self.max_failure_rate:
                logger.error(f"Failure rate {failure_rate:.1%} exceeds threshold {self.max_failure_rate:.1%}")
                return AgentAction.STOP_ALL

            # Check circuit breaker
            if not self.circuit_breaker.can_execute():
                logger.error("Circuit breaker open, stopping new agents")
                return AgentAction.PAUSE

            return AgentAction.CONTINUE

    def get_retry_candidates(self) -> list:
        """
        Get list of failed files that can be retried.
        """
        return [f for f in self.failed_files if f["retryable"]]

    def generate_error_report(self) -> dict:
        """
        Generate comprehensive error report.
        """
        return {
            "summary": {
                "total_failed": len(self.failed_files),
                "total_partial": len(self.partial_files),
                "retryable": len(self.get_retry_candidates())
            },
            "failed_files": self.failed_files,
            "partial_files": self.partial_files,
            "recommendations": self._generate_recommendations()
        }
```

### Layer 3: Error Classification System

```python
from enum import Enum, auto

class ErrorCategory(Enum):
    TRANSIENT = auto()      # Retry with backoff
    LLM_QUALITY = auto()    # Retry with correction prompt
    FATAL = auto()          # Exit immediately
    PARTIAL = auto()        # Accept and continue

class ErrorClassifier:
    """
    Classifies errors into appropriate categories for handling.
    """

    # Error patterns for classification
    TRANSIENT_PATTERNS = [
        (429, "rate_limit"),
        (503, "service_unavailable"),
        (504, "gateway_timeout"),
        ("timeout", "timeout"),
        ("connection", "network"),
        ("ECONNRESET", "network"),
        ("ETIMEDOUT", "network"),
    ]

    FATAL_PATTERNS = [
        (401, "authentication"),
        (403, "authorization"),
        (402, "payment_required"),
        ("invalid_api_key", "authentication"),
        ("model_not_found", "configuration"),
        ("FileNotFoundError", "file_missing"),
        ("MemoryError", "resource"),
    ]

    LLM_QUALITY_PATTERNS = [
        ("incomplete", "incomplete_response"),
        ("truncated", "incomplete_response"),
        ("invalid.*mermaid", "invalid_diagram"),
        ("syntax error", "invalid_diagram"),
        ("missing section", "missing_content"),
        ("coverage.*below", "low_coverage"),
    ]

    @classmethod
    def classify(cls, error: Exception) -> tuple[ErrorCategory, str]:
        """
        Classify error into category and subtype.
        """
        error_str = str(error).lower()
        error_code = getattr(error, 'status_code', None)

        # Check fatal first (most important)
        for pattern, subtype in cls.FATAL_PATTERNS:
            if cls._matches(error_str, error_code, pattern):
                return ErrorCategory.FATAL, subtype

        # Check transient
        for pattern, subtype in cls.TRANSIENT_PATTERNS:
            if cls._matches(error_str, error_code, pattern):
                return ErrorCategory.TRANSIENT, subtype

        # Check LLM quality
        for pattern, subtype in cls.LLM_QUALITY_PATTERNS:
            if cls._matches(error_str, error_code, pattern):
                return ErrorCategory.LLM_QUALITY, subtype

        # Default: treat as transient (optimistic)
        return ErrorCategory.TRANSIENT, "unknown"

    @staticmethod
    def _matches(error_str: str, error_code: int, pattern) -> bool:
        if isinstance(pattern, int):
            return error_code == pattern
        return bool(re.search(pattern, error_str, re.IGNORECASE))
```

---

## 🔧 LLM Response Validation

### Validation Rules

```python
class ResponseValidator:
    """
    Validates LLM responses for quality and completeness.
    """

    def validate_section_response(self, response: str, section_id: str, context: dict) -> ValidationResult:
        """
        Validate a section generation response.
        """
        errors = []
        warnings = []

        # Rule 1: Response not empty
        if not response or len(response.strip()) < 50:
            errors.append(ValidationError("empty_response", "Response is empty or too short"))

        # Rule 2: Contains required section header
        if section_id not in ["document-header"]:  # Header doesn't need ### prefix
            if f"### " not in response and f"## " not in response:
                warnings.append(ValidationWarning("missing_header", "Section header may be missing"))

        # Rule 3: Mermaid diagrams are valid (if present)
        mermaid_blocks = re.findall(r'```mermaid\n(.*?)```', response, re.DOTALL)
        for i, block in enumerate(mermaid_blocks):
            if not self._validate_mermaid(block):
                errors.append(ValidationError(
                    "invalid_mermaid",
                    f"Mermaid diagram {i+1} has syntax errors",
                    correctable=True,
                    correction_context={"diagram_content": block}
                ))

        # Rule 4: No obvious hallucinations
        if context.get("program_name"):
            # Check if response mentions non-existent programs
            mentioned_programs = re.findall(r"CALL\s+'(\w+)'", response)
            valid_programs = context.get("valid_program_names", [])
            for prog in mentioned_programs:
                if prog not in valid_programs and prog != context["program_name"]:
                    warnings.append(ValidationWarning(
                        "possible_hallucination",
                        f"Reference to '{prog}' not found in metadata"
                    ))

        # Rule 5: Code blocks are complete
        code_blocks = re.findall(r'```(\w*)\n', response)
        code_closes = response.count('```')
        if len(code_blocks) * 2 != code_closes:
            errors.append(ValidationError(
                "incomplete_code_block",
                "Code block not properly closed",
                correctable=True
            ))

        # Rule 6: Check for truncation indicators
        truncation_indicators = ["...", "[continued]", "[truncated]", "etc."]
        for indicator in truncation_indicators:
            if indicator in response[-100:]:  # Check end of response
                warnings.append(ValidationWarning(
                    "possible_truncation",
                    f"Response may be truncated (found '{indicator}')"
                ))

        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            is_correctable=all(e.correctable for e in errors),
            meets_minimum_threshold=len(errors) <= 1 and all(e.correctable for e in errors)
        )

    def validate_code_explanation(self, response: str, source_lines: int, expected_coverage: float = 0.95) -> ValidationResult:
        """
        Validate code explanation section for coverage.
        """
        errors = []
        warnings = []

        # Extract explained line numbers from response
        explained_lines = set()
        line_references = re.findall(r'[Ll]ines?\s+(\d+)(?:\s*-\s*(\d+))?', response)
        for match in line_references:
            start = int(match[0])
            end = int(match[1]) if match[1] else start
            explained_lines.update(range(start, end + 1))

        coverage = len(explained_lines) / max(source_lines, 1)

        if coverage < expected_coverage:
            errors.append(ValidationError(
                "low_coverage",
                f"Coverage {coverage:.1%} below threshold {expected_coverage:.1%}",
                correctable=True,
                correction_context={
                    "coverage": coverage,
                    "target": expected_coverage,
                    "explained_lines": sorted(explained_lines),
                    "total_lines": source_lines
                }
            ))
        elif coverage < expected_coverage * 0.9:  # Within 90% of target
            warnings.append(ValidationWarning(
                "marginal_coverage",
                f"Coverage {coverage:.1%} is close to threshold"
            ))

        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            is_correctable=True,
            meets_minimum_threshold=coverage >= expected_coverage * 0.8  # Accept 80% of target
        )

    def _validate_mermaid(self, diagram: str) -> bool:
        """
        Basic Mermaid syntax validation.
        """
        # Check for common syntax errors
        if diagram.count('[') != diagram.count(']'):
            return False
        if diagram.count('(') != diagram.count(')'):
            return False
        if diagram.count('{') != diagram.count('}'):
            return False

        # Check for required diagram type declaration
        valid_types = ['graph', 'flowchart', 'sequenceDiagram', 'classDiagram', 'stateDiagram', 'erDiagram', 'pie']
        if not any(diagram.strip().startswith(t) for t in valid_types):
            return False

        return True
```

---

## 📋 Recommended Configuration

```yaml
# error_handling section in config
error_handling:
  # Retry settings
  max_retries: 3                    # Max retries for transient errors
  max_corrections: 2                # Max LLM correction attempts

  # Backoff settings
  initial_backoff_seconds: 1.0
  max_backoff_seconds: 120.0
  backoff_multiplier: 2.0
  jitter_percent: 25

  # Circuit breaker
  circuit_breaker:
    enabled: true
    failure_threshold: 5            # Failures before opening circuit
    recovery_timeout_seconds: 60    # Time before trying again
    success_threshold: 2            # Successes to close circuit

  # Failure handling
  continue_on_failure: true         # Continue processing other files
  max_failure_rate: 0.2             # Stop if >20% of agents fail

  # Validation thresholds
  validation:
    min_coverage_percent: 80        # Accept if >= 80% coverage
    target_coverage_percent: 95     # Ideal coverage target
    allow_partial_results: true     # Accept partial success

  # Reporting
  generate_error_report: true       # Generate error summary file
  error_report_path: ./errors/error-report.yaml
```

---

## 🔄 Error Handling Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                        AGENT EXECUTION                               │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
                         ┌───────────────┐
                         │ Execute Task  │
                         └───────┬───────┘
                                 │
                    ┌────────────┼────────────┐
                    │            │            │
                    ▼            ▼            ▼
              ┌──────────┐ ┌──────────┐ ┌──────────┐
              │ SUCCESS  │ │  ERROR   │ │ PARTIAL  │
              └────┬─────┘ └────┬─────┘ └────┬─────┘
                   │            │            │
                   │            ▼            │
                   │   ┌────────────────┐    │
                   │   │ CLASSIFY ERROR │    │
                   │   └───────┬────────┘    │
                   │           │             │
                   │     ┌─────┴─────┬───────┴────┐
                   │     ▼           ▼            ▼
                   │ ┌────────┐ ┌─────────┐ ┌─────────┐
                   │ │TRANSIENT│ │LLM QUAL │ │  FATAL  │
                   │ └───┬────┘ └────┬────┘ └────┬────┘
                   │     │           │           │
                   │     ▼           ▼           ▼
                   │ ┌────────┐ ┌─────────┐ ┌─────────┐
                   │ │BACKOFF │ │CORRECTION│ │  EXIT   │
                   │ │+ RETRY │ │ PROMPT   │ │IMMEDIATE│
                   │ └───┬────┘ └────┬────┘ └────┬────┘
                   │     │           │           │
                   │     ▼           ▼           │
                   │ ┌────────────────────┐      │
                   │ │  RETRY EXHAUSTED?  │      │
                   │ └─────────┬──────────┘      │
                   │      YES  │  NO             │
                   │     ┌─────┴─────┐           │
                   │     ▼           ▼           │
                   │ ┌────────┐  ┌──────┐        │
                   │ │MARK AS │  │RETRY │        │
                   │ │FAILED  │  │ TASK │        │
                   │ └───┬────┘  └──────┘        │
                   │     │                       │
                   │     ▼                       │
                   │ ┌─────────────────────┐     │
                   │ │CHECK CIRCUIT BREAKER│     │
                   │ └─────────┬───────────┘     │
                   │           │                 │
                   │     ┌─────┴─────┐           │
                   │     ▼           ▼           │
                   │  ┌──────┐  ┌────────┐       │
                   │  │CLOSED│  │  OPEN  │       │
                   │  └──┬───┘  └───┬────┘       │
                   │     │          │            │
                   ▼     ▼          ▼            ▼
              ┌─────────────────────────────────────┐
              │         UPDATE TRACKING FILE        │
              └─────────────────────────────────────┘
                                  │
                                  ▼
              ┌─────────────────────────────────────┐
              │    ORCHESTRATOR DECISION POINT      │
              │  • Check failure rate threshold     │
              │  • Check circuit breaker state      │
              │  • Decide: CONTINUE / PAUSE / STOP  │
              └─────────────────────────────────────┘
```

---

## 📊 Summary: Error Handling Strategy

### Your Proposed Approach (Validated ✅)

| Scenario | Your Idea | My Recommendation |
|----------|-----------|-------------------|
| Rate limiting | Exit | ✅ **Retry with backoff** - Rate limits are temporary |
| Other API issues | Exit | ⚠️ **Classify first** - Some API issues are transient |
| LLM suboptimal response | Retry with correction | ✅ **Exactly right** - Use follow-up prompts |
| After correction still fails | Continue | ✅ **Correct** - Mark as failed, continue with others |

### Recommended Additions

1. **Circuit Breaker**: Stop spawning new agents if system-wide issues detected
2. **Validation Layer**: Proactively detect quality issues before considering "success"
3. **Partial Success**: Accept 80%+ coverage instead of failing completely
4. **Error Classification**: Automated categorization for appropriate handling
5. **Exponential Backoff**: Prevents thundering herd on rate limits
6. **Failure Rate Monitoring**: Stop entire run if too many failures (>20%)

### Key Principle: Fail Fast, Recover Gracefully

```
FATAL errors    → Exit immediately (don't waste time/money)
TRANSIENT errors → Retry with backoff (will likely succeed)
QUALITY errors   → Retry with correction prompt (can be fixed)
PARTIAL success  → Accept and continue (good enough)
```

---

---

## 🚨 Parallel Execution Failure Modes

### Category 5: Ray Framework Errors

| Error Type | Cause | Detection | Handling |
|------------|-------|-----------|----------|
| **Worker Crash** | OOM, segfault, unhandled exception | `ray.exceptions.RayActorError` | Reschedule task on different worker |
| **Object Store Full** | Too many large objects in shared memory | `ray.exceptions.ObjectStoreFullError` | Reduce batch size, clear old references |
| **Node Failure** | Machine crashes, network partition | `ray.exceptions.NodeDiedError` | Reschedule all tasks from dead node |
| **Task Timeout** | Agent hangs indefinitely | Custom timeout wrapper | Kill task, mark as failed, continue |
| **Serialization Error** | Non-picklable objects in task args | `ray.exceptions.RayTaskError` | Fix code - don't pass unpicklable objects |
| **Resource Exhaustion** | Requested more CPU/RAM than available | Task stuck in PENDING | Reduce resource requirements or batch size |
| **Plasma Store Crash** | Shared memory corruption | Ray cluster becomes unresponsive | Restart Ray cluster, resume from checkpoint |
| **GCS Failure** | Global Control Store unavailable | Cluster-wide failure | Restart Ray, resume from tracking file |

### Category 6: Resource Contention Errors

| Error Type | Cause | Symptoms | Handling |
|------------|-------|----------|----------|
| **Memory Pressure** | 100 agents × 300MB each | System swap, OOM killer | Reduce batch size, enable memory monitoring |
| **CPU Starvation** | More agents than CPU cores | Slow execution, timeouts | Limit concurrent agents to CPU count |
| **Disk I/O Bottleneck** | All agents writing metadata simultaneously | Slow writes, I/O errors | Stagger writes, use SSD, async I/O |
| **File Descriptor Exhaustion** | Too many open files/sockets | `OSError: Too many open files` | Increase ulimit, reduce concurrency |
| **Network Socket Exhaustion** | 100 agents × multiple LLM connections | Connection refused | Connection pooling, reduce concurrency |
| **GPU Memory (if applicable)** | Multiple agents sharing GPU | CUDA OOM | GPU scheduling, sequential GPU access |

### Category 7: Concurrency & Race Condition Errors

| Error Type | Cause | Symptoms | Handling |
|------------|-------|----------|----------|
| **File Write Conflicts** | Multiple agents writing same file | Corrupted output, partial writes | File locking, unique temp files, atomic rename |
| **Metadata Read Conflicts** | Agent reads while another writes | Inconsistent data, JSON parse errors | Read-only after initial generation |
| **Progress File Corruption** | Concurrent updates to tracking file | Lost progress, duplicate entries | Centralized tracker (Ray actor), append-only log |
| **Stdout/Stderr Interleaving** | Multiple agents logging simultaneously | Unreadable logs | Structured logging with agent ID prefix |
| **Database Connection Pool** | If using DB for tracking | Connection exhaustion, deadlocks | Pool sizing, connection timeout |
| **MCP Server State Corruption** | Multiple agents calling same MCP server | Unpredictable results | Pre-generate all metadata, or serialize MCP calls |

### Category 8: Distributed System Errors

| Error Type | Cause | Detection | Handling |
|------------|-------|-----------|----------|
| **Split Brain** | Network partition in Ray cluster | Inconsistent cluster state | Use single-node Ray for simplicity |
| **Stale Object References** | Object evicted from store | `ObjectLostError` | Re-execute task that produced object |
| **Task Duplication** | Speculative execution, retries | Same file documented twice | Idempotency checks, deduplication |
| **Zombie Agents** | Agent hangs but doesn't crash | Progress stalls | Heartbeat monitoring, timeout kill |
| **Cascading Failures** | One failure triggers others | Rapid increase in failures | Circuit breaker, failure rate monitoring |
| **Resource Leak** | Agents don't clean up on failure | Gradual resource exhaustion | Cleanup handlers, resource monitoring |

---

## 🔧 Ray-Specific Error Handling

### Ray Exception Hierarchy

```python
import ray.exceptions

# Ray exception types to handle
RAY_TRANSIENT_ERRORS = (
    ray.exceptions.RayTaskError,           # Task raised exception
    ray.exceptions.WorkerCrashedError,     # Worker process died
    ray.exceptions.NodeDiedError,          # Node became unavailable
    ray.exceptions.ObjectLostError,        # Object evicted/lost
    ray.exceptions.GetTimeoutError,        # ray.get() timeout
    ray.exceptions.TaskCancelledError,     # Task was cancelled
)

RAY_FATAL_ERRORS = (
    ray.exceptions.ObjectStoreFullError,   # Need to reduce memory usage
    ray.exceptions.OutOfMemoryError,       # System OOM
    ray.exceptions.RaySystemError,         # Internal Ray error
)

RAY_RETRIABLE_ERRORS = (
    ray.exceptions.RayActorError,          # Actor died, can restart
    ray.exceptions.LocalRayletDiedError,   # Local raylet crashed
)
```

### Robust Ray Task Wrapper

```python
import ray
import time
from typing import Any, Callable
from dataclasses import dataclass
from enum import Enum

class TaskStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    TIMEOUT = "timeout"
    CANCELLED = "cancelled"

@dataclass
class TaskResult:
    status: TaskStatus
    result: Any = None
    error: Exception = None
    duration_seconds: float = 0
    retries: int = 0
    worker_id: str = None

@ray.remote(
    max_retries=3,                    # Ray automatic retries
    retry_exceptions=[                 # Only retry these
        ray.exceptions.WorkerCrashedError,
        ray.exceptions.NodeDiedError,
    ]
)
class RobustDocumentationAgent:
    """
    Ray actor with built-in error handling and health monitoring.
    """

    def __init__(self, agent_id: str, config: dict):
        self.agent_id = agent_id
        self.config = config
        self.start_time = time.time()
        self.last_heartbeat = time.time()
        self.status = TaskStatus.PENDING

    def heartbeat(self) -> dict:
        """Health check endpoint for monitoring."""
        self.last_heartbeat = time.time()
        return {
            "agent_id": self.agent_id,
            "status": self.status.value,
            "uptime_seconds": time.time() - self.start_time,
            "last_heartbeat": self.last_heartbeat
        }

    def generate_documentation(self, file_path: str, metadata: dict) -> TaskResult:
        """
        Main entry point with comprehensive error handling.
        """
        self.status = TaskStatus.RUNNING
        start = time.time()

        try:
            # Import here to avoid serialization issues
            from cobol_doc_agent import generate_documentation

            result = generate_documentation(
                program_name=metadata["program_name"],
                workspace_path=metadata["workspace_path"],
                metadata_dir=metadata["metadata_dir"],
                output_dir=metadata["output_dir"],
                llm_config=self.config.get("llm"),
            )

            self.status = TaskStatus.COMPLETED
            return TaskResult(
                status=TaskStatus.COMPLETED,
                result=result,
                duration_seconds=time.time() - start,
                worker_id=ray.get_runtime_context().get_worker_id()
            )

        except MemoryError as e:
            self.status = TaskStatus.FAILED
            # Don't retry OOM - need to reduce batch size
            raise ray.exceptions.OutOfMemoryError(str(e))

        except Exception as e:
            self.status = TaskStatus.FAILED
            return TaskResult(
                status=TaskStatus.FAILED,
                error=e,
                duration_seconds=time.time() - start,
                worker_id=ray.get_runtime_context().get_worker_id()
            )


def execute_with_timeout(
    agent: RobustDocumentationAgent,
    file_path: str,
    metadata: dict,
    timeout_seconds: int = 600  # 10 minutes default
) -> TaskResult:
    """
    Execute agent task with timeout protection.
    """
    try:
        # Get object reference
        result_ref = agent.generate_documentation.remote(file_path, metadata)

        # Wait with timeout
        ready, not_ready = ray.wait([result_ref], timeout=timeout_seconds)

        if ready:
            return ray.get(result_ref)
        else:
            # Timeout - kill the task
            ray.cancel(result_ref, force=True)
            return TaskResult(
                status=TaskStatus.TIMEOUT,
                error=TimeoutError(f"Agent timed out after {timeout_seconds}s"),
                duration_seconds=timeout_seconds
            )

    except ray.exceptions.RayTaskError as e:
        # Task raised an exception
        return TaskResult(
            status=TaskStatus.FAILED,
            error=e.cause if hasattr(e, 'cause') else e
        )

    except ray.exceptions.TaskCancelledError:
        return TaskResult(
            status=TaskStatus.CANCELLED,
            error=Exception("Task was cancelled")
        )
```

### Memory Monitoring and Backpressure

```python
import psutil
import ray

class MemoryMonitor:
    """
    Monitor system memory and apply backpressure when needed.
    """

    def __init__(
        self,
        warning_threshold: float = 0.75,  # 75% memory usage
        critical_threshold: float = 0.90,  # 90% memory usage
        check_interval_seconds: float = 5.0
    ):
        self.warning_threshold = warning_threshold
        self.critical_threshold = critical_threshold
        self.check_interval = check_interval_seconds

    def get_memory_usage(self) -> float:
        """Get current memory usage as percentage (0-1)."""
        return psutil.virtual_memory().percent / 100

    def get_available_memory_gb(self) -> float:
        """Get available memory in GB."""
        return psutil.virtual_memory().available / (1024 ** 3)

    def can_spawn_agent(self, estimated_memory_gb: float = 0.3) -> tuple[bool, str]:
        """
        Check if we have enough memory to spawn another agent.
        """
        usage = self.get_memory_usage()
        available = self.get_available_memory_gb()

        if usage >= self.critical_threshold:
            return False, f"CRITICAL: Memory usage at {usage:.1%}, refusing new agents"

        if available < estimated_memory_gb:
            return False, f"Insufficient memory: {available:.1f}GB available, need {estimated_memory_gb}GB"

        if usage >= self.warning_threshold:
            return True, f"WARNING: Memory usage at {usage:.1%}, proceeding with caution"

        return True, "OK"

    def recommend_batch_size(self, estimated_memory_per_agent_gb: float = 0.3) -> int:
        """
        Recommend batch size based on available memory.
        """
        available = self.get_available_memory_gb()
        # Reserve 20% for system overhead
        usable = available * 0.8
        recommended = int(usable / estimated_memory_per_agent_gb)
        return max(1, min(recommended, 100))  # Between 1 and 100


class AdaptiveBatchController:
    """
    Dynamically adjust batch size based on system health.
    """

    def __init__(self, initial_batch_size: int, memory_monitor: MemoryMonitor):
        self.batch_size = initial_batch_size
        self.min_batch_size = 1
        self.max_batch_size = initial_batch_size * 2
        self.memory_monitor = memory_monitor
        self.failure_count = 0
        self.success_count = 0

    def adjust_batch_size(self, success: bool, error_type: str = None):
        """
        Adjust batch size based on execution results.
        """
        if success:
            self.success_count += 1
            self.failure_count = 0

            # If 10 consecutive successes and memory OK, try increasing
            if self.success_count >= 10:
                can_spawn, _ = self.memory_monitor.can_spawn_agent()
                if can_spawn and self.batch_size < self.max_batch_size:
                    self.batch_size = min(self.batch_size + 5, self.max_batch_size)
                    self.success_count = 0

        else:
            self.failure_count += 1
            self.success_count = 0

            # Reduce batch size on memory-related errors
            if error_type in ["OOM", "ObjectStoreFullError", "MemoryError"]:
                self.batch_size = max(self.batch_size // 2, self.min_batch_size)

            # Reduce on consecutive failures
            elif self.failure_count >= 3:
                self.batch_size = max(self.batch_size - 5, self.min_batch_size)
                self.failure_count = 0

    def get_current_batch_size(self) -> int:
        """Get recommended batch size considering current memory."""
        recommended = self.memory_monitor.recommend_batch_size()
        return min(self.batch_size, recommended)
```

### Zombie Agent Detection

```python
import ray
import time
from typing import Dict, List
import threading

@ray.remote
class AgentHealthMonitor:
    """
    Centralized health monitor for all agents.
    Detects zombie agents (running but not making progress).
    """

    def __init__(self, timeout_seconds: int = 300):  # 5 min default
        self.agents: Dict[str, dict] = {}
        self.timeout_seconds = timeout_seconds

    def register_agent(self, agent_id: str, file_path: str):
        """Register a new agent."""
        self.agents[agent_id] = {
            "file_path": file_path,
            "registered_at": time.time(),
            "last_heartbeat": time.time(),
            "last_progress": None,
            "status": "starting"
        }

    def heartbeat(self, agent_id: str, progress: dict = None):
        """Receive heartbeat from agent."""
        if agent_id in self.agents:
            self.agents[agent_id]["last_heartbeat"] = time.time()
            if progress:
                self.agents[agent_id]["last_progress"] = progress
                self.agents[agent_id]["status"] = progress.get("status", "running")

    def mark_completed(self, agent_id: str, success: bool):
        """Mark agent as completed."""
        if agent_id in self.agents:
            self.agents[agent_id]["status"] = "completed" if success else "failed"
            self.agents[agent_id]["completed_at"] = time.time()

    def get_zombie_agents(self) -> List[str]:
        """
        Find agents that haven't sent heartbeat within timeout.
        """
        now = time.time()
        zombies = []

        for agent_id, info in self.agents.items():
            if info["status"] in ["completed", "failed"]:
                continue

            time_since_heartbeat = now - info["last_heartbeat"]
            if time_since_heartbeat > self.timeout_seconds:
                zombies.append(agent_id)

        return zombies

    def get_status_summary(self) -> dict:
        """Get summary of all agent statuses."""
        summary = {
            "total": len(self.agents),
            "starting": 0,
            "running": 0,
            "completed": 0,
            "failed": 0,
            "zombie": 0
        }

        zombies = set(self.get_zombie_agents())

        for agent_id, info in self.agents.items():
            if agent_id in zombies:
                summary["zombie"] += 1
            else:
                status = info.get("status", "unknown")
                if status in summary:
                    summary[status] += 1

        return summary
```

### File Locking for Concurrent Access

```python
import fcntl
import os
from contextlib import contextmanager
from pathlib import Path

class FileLockError(Exception):
    """Raised when file lock cannot be acquired."""
    pass

@contextmanager
def file_lock(filepath: str, timeout: float = 30.0, mode: str = "exclusive"):
    """
    Cross-platform file locking for concurrent access protection.

    Args:
        filepath: Path to file to lock
        timeout: Max seconds to wait for lock
        mode: "exclusive" (write) or "shared" (read)
    """
    lock_path = Path(filepath).with_suffix(Path(filepath).suffix + ".lock")
    lock_file = None

    try:
        # Create lock file
        lock_file = open(lock_path, 'w')

        # Determine lock type
        lock_type = fcntl.LOCK_EX if mode == "exclusive" else fcntl.LOCK_SH

        # Try to acquire lock with timeout
        start = time.time()
        while True:
            try:
                fcntl.flock(lock_file.fileno(), lock_type | fcntl.LOCK_NB)
                break
            except IOError:
                if time.time() - start > timeout:
                    raise FileLockError(f"Could not acquire lock on {filepath} within {timeout}s")
                time.sleep(0.1)

        yield filepath

    finally:
        if lock_file:
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)
            lock_file.close()
            try:
                lock_path.unlink()
            except:
                pass


def safe_write_file(filepath: str, content: str):
    """
    Safely write file with atomic rename (prevents corruption).
    """
    temp_path = filepath + f".tmp.{os.getpid()}"

    try:
        # Write to temp file
        with open(temp_path, 'w') as f:
            f.write(content)
            f.flush()
            os.fsync(f.fileno())  # Force write to disk

        # Atomic rename
        os.rename(temp_path, filepath)

    finally:
        # Clean up temp file if rename failed
        if os.path.exists(temp_path):
            os.unlink(temp_path)


def safe_append_jsonl(filepath: str, record: dict):
    """
    Safely append to JSONL file (for progress tracking).
    """
    import json

    with file_lock(filepath, mode="exclusive"):
        with open(filepath, 'a') as f:
            f.write(json.dumps(record) + '\n')
            f.flush()
            os.fsync(f.fileno())
```

---

## 📋 Parallel Execution Error Handling Checklist

### Pre-Execution Checks

```python
class PreExecutionValidator:
    """
    Validate system state before spawning agents.
    """

    def validate(self, config: dict, file_count: int) -> List[str]:
        """
        Run all pre-execution checks.
        Returns list of warnings/errors.
        """
        issues = []

        # Check 1: Ray cluster health
        if not ray.is_initialized():
            issues.append("FATAL: Ray not initialized")
            return issues

        cluster_resources = ray.cluster_resources()
        if cluster_resources.get("CPU", 0) < 1:
            issues.append("FATAL: No CPU resources available in Ray cluster")

        # Check 2: Memory availability
        memory_monitor = MemoryMonitor()
        available_gb = memory_monitor.get_available_memory_gb()
        required_gb = file_count * 0.3  # Estimate 300MB per agent

        if available_gb < required_gb:
            issues.append(
                f"WARNING: May not have enough memory. "
                f"Available: {available_gb:.1f}GB, Estimated need: {required_gb:.1f}GB"
            )

        # Check 3: File descriptor limits
        import resource
        soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
        required_fds = file_count * 10  # Estimate 10 FDs per agent

        if soft < required_fds:
            issues.append(
                f"WARNING: File descriptor limit ({soft}) may be too low. "
                f"Consider: ulimit -n {required_fds}"
            )

        # Check 4: Disk space
        import shutil
        disk = shutil.disk_usage(config.get("output_dir", "."))
        free_gb = disk.free / (1024 ** 3)

        if free_gb < 1.0:
            issues.append(f"WARNING: Low disk space: {free_gb:.1f}GB free")

        # Check 5: Output directory writable
        output_dir = config.get("output_dir", "./output")
        if not os.access(output_dir, os.W_OK):
            issues.append(f"FATAL: Output directory not writable: {output_dir}")

        # Check 6: LLM API reachable (quick health check)
        # ... API health check code ...

        return issues
```

### Runtime Monitoring

```python
@ray.remote
class RuntimeMonitor:
    """
    Continuous monitoring during execution.
    """

    def __init__(self, config: dict):
        self.config = config
        self.alerts = []
        self.metrics = {
            "agents_spawned": 0,
            "agents_completed": 0,
            "agents_failed": 0,
            "total_tokens_used": 0,
            "total_cost_usd": 0,
        }

    def check_system_health(self) -> dict:
        """
        Periodic health check.
        """
        health = {
            "timestamp": time.time(),
            "memory_percent": psutil.virtual_memory().percent,
            "cpu_percent": psutil.cpu_percent(interval=1),
            "disk_percent": psutil.disk_usage('/').percent,
            "ray_nodes": len(ray.nodes()),
            "ray_available_resources": ray.available_resources(),
        }

        # Generate alerts
        if health["memory_percent"] > 90:
            self.alerts.append({
                "level": "critical",
                "message": f"Memory usage critical: {health['memory_percent']}%",
                "timestamp": health["timestamp"]
            })

        if health["cpu_percent"] > 95:
            self.alerts.append({
                "level": "warning",
                "message": f"CPU usage high: {health['cpu_percent']}%",
                "timestamp": health["timestamp"]
            })

        return health

    def get_alerts(self, since: float = 0) -> List[dict]:
        """Get alerts since timestamp."""
        return [a for a in self.alerts if a["timestamp"] > since]

    def update_metrics(self, update: dict):
        """Update execution metrics."""
        for key, value in update.items():
            if key in self.metrics:
                self.metrics[key] += value

    def get_metrics(self) -> dict:
        """Get current metrics."""
        return self.metrics.copy()
```

---

## 🎯 Implementation Priority

1. **P0 (Must Have)**: Error classification, basic retry logic, continue on failure
2. **P1 (Should Have)**: Correction prompts, validation layer, error reporting
3. **P2 (Nice to Have)**: Circuit breaker, failure rate monitoring, partial success handling
4. **P3 (Parallel Execution)**: Ray error handling, memory monitoring, zombie detection, file locking

---

## 📊 Error Handling Configuration (Complete)

```yaml
error_handling:
  # === Basic Retry Settings ===
  max_retries: 3
  max_corrections: 2

  # === Backoff Settings ===
  backoff:
    initial_seconds: 1.0
    max_seconds: 120.0
    multiplier: 2.0
    jitter_percent: 25

  # === Circuit Breaker ===
  circuit_breaker:
    enabled: true
    failure_threshold: 5
    recovery_timeout_seconds: 60
    success_threshold: 2

  # === Failure Handling ===
  continue_on_failure: true
  max_failure_rate: 0.2

  # === Validation ===
  validation:
    min_coverage_percent: 80
    target_coverage_percent: 95
    allow_partial_results: true

  # === Parallel Execution (NEW) ===
  parallel:
    # Memory management
    memory:
      warning_threshold_percent: 75
      critical_threshold_percent: 90
      estimated_per_agent_gb: 0.3
      enable_adaptive_batching: true

    # Timeout settings
    timeouts:
      agent_timeout_seconds: 600      # 10 minutes per agent
      heartbeat_interval_seconds: 30
      zombie_detection_seconds: 300   # 5 minutes no heartbeat = zombie

    # Resource limits
    resources:
      max_concurrent_agents: 50       # Hard limit regardless of batch size
      cpu_per_agent: 1
      memory_per_agent_gb: 0.5

    # File locking
    file_locking:
      enabled: true
      timeout_seconds: 30

    # Health monitoring
    monitoring:
      enabled: true
      check_interval_seconds: 10
      alert_on_memory_percent: 85
      alert_on_cpu_percent: 95

  # === Reporting ===
  reporting:
    generate_error_report: true
    error_report_path: ./errors/error-report.yaml
    include_stack_traces: true
    include_system_metrics: true
```

Let me know if you'd like me to expand on any of these patterns!
