"""
Mermaid Diagram Validator

Validates and fixes Mermaid diagrams in generated markdown using:
1. MCP Server (mermaid-mcp:test) for syntax validation
2. LLM for fixing invalid diagrams

Flow:
1. Extract all ```mermaid blocks from markdown with positions
2. Validate each block via MCP "validate" tool
3. If invalid: Use LLM to fix, then re-validate (max 3 retries)
4. Replace fixed blocks back into the original positions
"""

import asyncio
import json
import re
import time
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, TypedDict, Union

from mcp_use import MCPClient


class MermaidValidationStats(TypedDict):
    """Type definition for mermaid validation statistics."""
    total_blocks: int
    valid_blocks: int
    fixed_blocks: int
    failed_blocks: int
    sections_with_mermaid: List[str]


class MermaidSectionStats(TypedDict):
    """Type definition for per-section mermaid stats."""
    total: int
    valid: int
    fixed: int
    failed: int


@dataclass
class MermaidBlock:
    """Represents a mermaid code block with its position in the source text."""
    code: str
    start_pos: int
    end_pos: int
    section_id: str  # Which section this block belongs to


class MermaidValidator:
    """
    Validates and fixes Mermaid diagrams using MCP server and LLM.
    """

    def __init__(
        self,
        docker_image: str = "mermaid-mcp:test",
        llm_config: Optional[Dict[str, Any]] = None,
        fallback_manager: Optional[Any] = None
    ):
        """
        Initialize the Mermaid validator.

        Args:
            docker_image: Docker image name for Mermaid MCP server
            llm_config: LLM configuration for fixing invalid diagrams
            fallback_manager: Optional LLMFallbackManager for automatic fallback on errors
        """
        self.docker_image = docker_image
        self.llm_config: Dict[str, Any] = llm_config or {}
        self.fallback_manager = fallback_manager
        self.mcp_client: Optional[MCPClient] = None
        self.max_retries = 3

    def get_mcp_config(self) -> Dict[str, Any]:
        """
        Generate mcp-use configuration for Mermaid MCP server.
        """
        return {
            "mcpServers": {
                "mermaid": {
                    "command": "docker",
                    "args": [
                        "run",
                        "-i",
                        "--rm",
                        self.docker_image
                    ]
                }
            }
        }

    async def initialize(self):
        """Initialize MCP client and create session."""
        print("\n  → Initializing Mermaid MCP validator...")
        mcp_config = self.get_mcp_config()
        self.mcp_client = MCPClient.from_dict(mcp_config)
        await self.mcp_client.create_all_sessions()
        print("  ✓ Mermaid MCP session ready")

    async def cleanup(self):
        """Cleanup MCP session."""
        if self.mcp_client:
            # Sessions auto-cleanup via Docker --rm flag
            print("  ✓ Mermaid MCP session closed")

    def extract_mermaid_blocks(self, markdown: str, section_id: str = "unknown") -> List[MermaidBlock]:
        """
        Extract all mermaid code blocks from markdown with their positions.

        Args:
            markdown: Markdown content
            section_id: Section identifier for tracking

        Returns:
            List of MermaidBlock objects with code and positions
        """
        blocks = []
        # Pattern to match ```mermaid ... ``` blocks
        pattern = re.compile(r'```mermaid\n(.*?)```', re.DOTALL)

        for match in pattern.finditer(markdown):
            blocks.append(MermaidBlock(
                code=match.group(1).strip(),
                start_pos=match.start(),
                end_pos=match.end(),
                section_id=section_id
            ))

        return blocks

    async def validate_mermaid(self, code: str) -> Tuple[bool, Optional[str]]:
        """
        Validate mermaid diagram syntax using MCP server.

        Args:
            code: Mermaid diagram code

        Returns:
            Tuple of (is_valid, error_message)
        """
        try:
            if self.mcp_client is None:
                return False, "MCP client not initialized"
            session = self.mcp_client.get_session("mermaid")
            result = await session.call_tool("validate", {"code": code})

            # Parse the result
            if hasattr(result, 'content') and result.content:
                first_item = result.content[0]
                if hasattr(first_item, 'text'):
                    response = json.loads(first_item.text)
                    if response.get('valid', False):
                        return True, None
                    else:
                        return False, response.get('error', 'Unknown validation error')

            return False, "Invalid response from MCP server"

        except Exception as e:
            return False, f"MCP validation failed: {str(e)}"

    def fix_mermaid_with_llm(self, invalid_code: str, error: str, section_content: Optional[str] = None) -> str:
        """
        Use LLM to fix invalid mermaid diagram.

        Args:
            invalid_code: The invalid mermaid code
            error: Error message from validator
            section_content: Optional section document for additional context

        Returns:
            Fixed mermaid code
        """
        from langchain_core.messages import HumanMessage, SystemMessage
        from cobol_doc_agent import create_llm

        # Create LLM instance using the factory (supports openai, anthropic, claude_sdk)
        llm_config_for_fix = {
            'provider': self.llm_config.get('provider', 'openai'),
            'model': self.llm_config.get('model', 'gpt-4.1'),
            'api_key': self.llm_config.get('api_key'),
            'temperature': 0.1  # Low temperature for deterministic fixes
        }
        llm = create_llm(llm_config_for_fix)

        # Base system prompt for mermaid syntax fixing
        base_system_prompt = """You are a Mermaid diagram syntax expert. Your task is to fix invalid Mermaid diagram code so it renders in VSCode Mermaid preview.

INPUTS PROVIDED TO YOU:
- Mermaid code (possibly invalid)
- The VSCode Mermaid parse error message

OUTPUT RULES (STRICT):
1. Return ONLY the corrected Mermaid code (no explanations, no markdown fences).
2. Preserve the original intent and structure as much as possible.
3. Prefer the most conservative fix that makes the diagram render successfully.

VSCode-SAFE MERMAID CONSTRAINTS (MUST OBEY):
A) Diagram header:
   - Ensure the first non-empty line is a valid diagram type, e.g.:
     - graph LR / graph TD
     - flowchart LR / flowchart TD
     - sequenceDiagram
B) Node IDs:
   - IDs must use only A–Z, a–z, 0–9, underscore.
   - If an ID contains special characters (hyphen, slash, quotes, asterisk, space, etc.),
     rename it to a sanitized ID (e.g., RMTPRTLBL_030040) and keep the original text in the label.
C) Labels:
   - Use explicit labels: ID["label text"] or ID("label text").
   - Do NOT use HTML tags like <br/> or <br>. Replace with \n inside the label.
   - Do NOT include unescaped double quotes or sequences like \" inside labels.
     If the label contains quotes/slashes like L"S"/"GENL", convert to a safe text form like:
     L S / GENL / RMTPRTLBL
D) Edge labels:
   - If an edge uses |label|, the label must be a compact token:
     only letters/digits/underscore (e.g., 16x_CURRENT_DATE).
   - Remove parentheses, commas, colons, and spaces from edge labels.
   - If the label is too long (e.g., includes line lists), replace it with a short token and
     keep the detailed info out of the edge label.
E) Subgraphs:
   - Use: subgraph SG_ID ["Title"] ... end
   - SG_ID must follow Node ID rules. Title must follow Label rules (no HTML, no quotes).
F) Keep supported shapes only:
   - Use [ ] or ( ) for nodes, { } for decisions. Avoid exotic syntax if not needed.
G) Always fix parse errors caused by tokenization:
   - Unbalanced brackets/quotes
   - Illegal characters in IDs
   - Illegal characters/HTML in labels or edge labels

FINAL CHECK BEFORE OUTPUT:
- No <br> or <br/> anywhere.
- No \" anywhere.
- No spaces/punctuation inside edge labels between | |.
- All IDs are alphanumeric/underscore only.

Output: Return ONLY the corrected Mermaid code.
"""

        # Prepend section context if provided
        if section_content:
            context_prefix = """ADDITIONAL CONTEXT:
You are also provided with the FULL SECTION DOCUMENT where this Mermaid diagram belongs.
Use this context to understand:
- What the diagram is supposed to represent
- The correct node names, relationships, and labels
- The business/technical domain of the diagram

The section document helps you fix the diagram while preserving its intended meaning.
Do NOT change the diagram's purpose - only fix the syntax errors.

---

"""
            system_prompt = context_prefix + base_system_prompt
        else:
            system_prompt = base_system_prompt

        # Build user prompt
        if section_content:
            # Truncate section content if too long (keep first 8000 chars for context)
            max_section_length = 8000
            if len(section_content) > max_section_length:
                truncated_section = section_content[:max_section_length] + "\n\n... [truncated for brevity] ..."
            else:
                truncated_section = section_content

            user_prompt = f"""SECTION DOCUMENT (for context):
---
{truncated_section}
---

Fix this invalid Mermaid diagram from the above section:

ERROR:
{error}

INVALID CODE:
{invalid_code}

Return ONLY the corrected Mermaid code:"""
        else:
            user_prompt = f"""Fix this invalid Mermaid diagram:

ERROR:
{error}

INVALID CODE:
{invalid_code}

Return ONLY the corrected Mermaid code:"""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]

        # Use fallback-aware invocation if fallback_manager is available
        if self.fallback_manager:
            from llm_fallback import invoke_llm_with_fallback
            try:
                response = invoke_llm_with_fallback(
                    llm_config=llm_config_for_fix,
                    messages=messages,
                    fallback_manager=self.fallback_manager,
                    phase=2  # Mermaid fixing is part of Phase 2
                )
                # Handle response.content which can be str or list
                content = response.content
                if isinstance(content, str):
                    fixed_code = content.strip()
                elif isinstance(content, list) and len(content) > 0:
                    first_block = content[0]
                    if hasattr(first_block, 'text'):
                        fixed_code = first_block.text.strip()
                    elif isinstance(first_block, str):
                        fixed_code = first_block.strip()
                    else:
                        fixed_code = str(first_block).strip()
                else:
                    fixed_code = invalid_code
            except Exception as e:
                print(f"        ✗ LLM fix failed: {e}")
                fixed_code = invalid_code
        else:
            # Original retry logic for when no fallback_manager
            max_retries = 5
            base_delay = 2  # seconds
            fixed_code = invalid_code  # Default to original if all retries fail

            for attempt in range(max_retries):
                try:
                    response = llm.invoke(messages)
                    # Handle response.content which can be str or list
                    content = response.content
                    if isinstance(content, str):
                        fixed_code = content.strip()
                    elif isinstance(content, list) and len(content) > 0:
                        # Extract text from first content block
                        first_block = content[0]
                        if hasattr(first_block, 'text'):
                            fixed_code = first_block.text.strip()
                        elif isinstance(first_block, str):
                            fixed_code = first_block.strip()
                        else:
                            fixed_code = str(first_block).strip()
                    break  # Success, exit retry loop
                except Exception as e:
                    error_str = str(e).lower()
                    # Check for rate limit error (429)
                    if '429' in str(e) or 'rate' in error_str or 'too many' in error_str:
                        if attempt < max_retries - 1:
                            delay = base_delay * (2 ** attempt)  # Exponential: 2, 4, 8, 16, 32 seconds
                            print(f"        ⚠ Rate limit hit, waiting {delay}s before retry ({attempt + 1}/{max_retries})...")
                            time.sleep(delay)
                        else:
                            print(f"        ✗ Rate limit exceeded after {max_retries} retries")
                            raise
                    else:
                        # Non-rate-limit error, re-raise immediately
                        raise

        # Remove any markdown fences if LLM included them
        if fixed_code.startswith('```mermaid'):
            fixed_code = fixed_code[10:]  # Remove ```mermaid\n
        if fixed_code.startswith('```'):
            fixed_code = fixed_code[3:]
        if fixed_code.endswith('```'):
            fixed_code = fixed_code[:-3]

        return fixed_code.strip()

    async def validate_and_fix_block(self, block: MermaidBlock, section_content: Optional[str] = None) -> Tuple[MermaidBlock, bool, str]:
        """
        Validate a mermaid block and fix if invalid.

        Args:
            block: MermaidBlock to validate
            section_content: Optional full section document for context when fixing

        Returns:
            Tuple of (fixed_block, was_fixed, status_message)
        """
        original_code = block.code
        current_code = block.code

        for attempt in range(1, self.max_retries + 1):
            is_valid, error = await self.validate_mermaid(current_code)

            if is_valid:
                if attempt == 1:
                    return block, False, "valid"
                else:
                    # Create new block with fixed code
                    fixed_block = MermaidBlock(
                        code=current_code,
                        start_pos=block.start_pos,
                        end_pos=block.end_pos,
                        section_id=block.section_id
                    )
                    return fixed_block, True, f"fixed after {attempt-1} attempt(s)"

            if attempt < self.max_retries + 1:
                print(f"      Attempt {attempt}/{self.max_retries}: Fixing with LLM...")
                # Pass section_content for additional context
                # error could be None, provide default message
                error_msg = error or "Unknown validation error"
                current_code = self.fix_mermaid_with_llm(current_code, error_msg, section_content)

        # Max retries exceeded - return original with warning
        print(f"      ⚠ Max retries exceeded, marking as invalid")
        final_error = error or "Unknown validation error"
        warning_block = MermaidBlock(
            code=f"[INVALID DIAGRAM - needs manual review]\n%% Error: {final_error}\n%% Original code:\n{original_code}",
            start_pos=block.start_pos,
            end_pos=block.end_pos,
            section_id=block.section_id
        )
        return warning_block, True, "failed - marked for manual review"

    def replace_blocks_in_markdown(self, markdown: str, blocks: List[MermaidBlock],
                                    fixed_blocks: List[MermaidBlock]) -> str:
        """
        Replace original blocks with fixed blocks in markdown.

        Must process in reverse order to preserve positions.

        Args:
            markdown: Original markdown
            blocks: Original blocks (with positions)
            fixed_blocks: Fixed blocks (with updated code)

        Returns:
            Markdown with replaced blocks
        """
        result = markdown

        # Create mapping of original to fixed
        block_map = {b.start_pos: fb for b, fb in zip(blocks, fixed_blocks)}

        # Sort by position in reverse order to preserve offsets
        sorted_positions = sorted(block_map.keys(), reverse=True)

        for pos in sorted_positions:
            original = next(b for b in blocks if b.start_pos == pos)
            fixed = block_map[pos]

            if original.code != fixed.code:
                # Reconstruct the full mermaid block with fences
                original_full = f"```mermaid\n{original.code}\n```"
                fixed_full = f"```mermaid\n{fixed.code}\n```"

                # Replace at exact position
                result = result[:original.start_pos] + fixed_full + result[original.end_pos:]

        return result


async def validate_all_mermaid_in_sections(
    code_explanation: str,
    section_outputs: Dict[str, str],
    llm_config: Dict[str, Any],
    docker_image: str = "mermaid-mcp:test"
) -> Tuple[str, Dict[str, str], MermaidValidationStats]:
    """
    Validate and fix all mermaid diagrams in generated sections.

    This is the main entry point called from generate_documentation().

    Args:
        code_explanation: Phase 1 output (detailed code explanation)
        section_outputs: Phase 2 outputs (dict of section_id -> content)
        llm_config: LLM configuration
        docker_image: Mermaid MCP Docker image name

    Returns:
        Tuple of (fixed_code_explanation, fixed_section_outputs, validation_stats)
    """
    print("\n" + "="*60)
    print("PHASE 2.5: Validating Mermaid Diagrams")
    print("="*60)

    validator = MermaidValidator(docker_image=docker_image, llm_config=llm_config)
    stats: MermaidValidationStats = {
        'total_blocks': 0,
        'valid_blocks': 0,
        'fixed_blocks': 0,
        'failed_blocks': 0,
        'sections_with_mermaid': []
    }

    try:
        await validator.initialize()

        # Process code explanation
        print("\n  → Checking code explanation for mermaid diagrams...")
        code_blocks = validator.extract_mermaid_blocks(code_explanation, "detailed-code-explanation")
        if code_blocks:
            print(f"    Found {len(code_blocks)} mermaid diagram(s)")
            stats['sections_with_mermaid'].append('detailed-code-explanation')

            fixed_code_blocks = []
            for i, block in enumerate(code_blocks, 1):
                print(f"    [{i}/{len(code_blocks)}] Validating diagram...")
                fixed_block, was_fixed, status = await validator.validate_and_fix_block(block)
                fixed_code_blocks.append(fixed_block)
                stats['total_blocks'] += 1

                if status == "valid":
                    stats['valid_blocks'] += 1
                    print(f"      ✓ Valid")
                elif "fixed" in status:
                    stats['fixed_blocks'] += 1
                    print(f"      ✓ {status}")
                else:
                    stats['failed_blocks'] += 1
                    print(f"      ✗ {status}")

            code_explanation = validator.replace_blocks_in_markdown(
                code_explanation, code_blocks, fixed_code_blocks
            )
        else:
            print("    No mermaid diagrams found")

        # Process each section
        fixed_section_outputs = {}
        for section_id, content in section_outputs.items():
            print(f"\n  → Checking section: {section_id}...")
            section_blocks = validator.extract_mermaid_blocks(content, section_id)

            if section_blocks:
                print(f"    Found {len(section_blocks)} mermaid diagram(s)")
                stats['sections_with_mermaid'].append(section_id)

                fixed_section_blocks = []
                for i, block in enumerate(section_blocks, 1):
                    print(f"    [{i}/{len(section_blocks)}] Validating diagram...")
                    fixed_block, was_fixed, status = await validator.validate_and_fix_block(block)
                    fixed_section_blocks.append(fixed_block)
                    stats['total_blocks'] += 1

                    if status == "valid":
                        stats['valid_blocks'] += 1
                        print(f"      ✓ Valid")
                    elif "fixed" in status:
                        stats['fixed_blocks'] += 1
                        print(f"      ✓ {status}")
                    else:
                        stats['failed_blocks'] += 1
                        print(f"      ✗ {status}")

                fixed_section_outputs[section_id] = validator.replace_blocks_in_markdown(
                    content, section_blocks, fixed_section_blocks
                )
            else:
                print("    No mermaid diagrams found")
                fixed_section_outputs[section_id] = content

        # Print summary
        print(f"\n  → Mermaid Validation Summary:")
        print(f"    Total diagrams: {stats['total_blocks']}")
        print(f"    Already valid:  {stats['valid_blocks']}")
        print(f"    Fixed by LLM:   {stats['fixed_blocks']}")
        print(f"    Failed:         {stats['failed_blocks']}")
        if stats['sections_with_mermaid']:
            print(f"    Sections with mermaid: {', '.join(stats['sections_with_mermaid'])}")

        print("\n✓ Phase 2.5 complete")

        return code_explanation, fixed_section_outputs, stats

    finally:
        await validator.cleanup()


def validate_mermaid_sync(
    code_explanation: str,
    section_outputs: Dict[str, str],
    llm_config: Dict[str, Any],
    docker_image: str = "mermaid-mcp:test"
) -> Tuple[str, Dict[str, str], MermaidValidationStats]:
    """
    Synchronous wrapper for mermaid validation.

    Can be called from generate_documentation().

    DEPRECATED: Use validate_section_mermaid_sync() instead for per-section validation.
    """
    return asyncio.run(validate_all_mermaid_in_sections(
        code_explanation=code_explanation,
        section_outputs=section_outputs,
        llm_config=llm_config,
        docker_image=docker_image
    ))


# ============================================================================
# PER-SECTION MERMAID VALIDATION (Called from Phase 2 loop)
# ============================================================================

async def validate_section_mermaid(
    section_id: str,
    section_content: str,
    validator: MermaidValidator
) -> Tuple[str, MermaidSectionStats]:
    """
    Validate and fix mermaid diagrams in a single section.

    Called immediately after each section is generated in Phase 2.
    Uses the full section content as context for LLM fixes.

    Args:
        section_id: Section identifier
        section_content: Full section markdown content
        validator: Initialized MermaidValidator instance

    Returns:
        Tuple of (fixed_section_content, stats_dict)
    """
    stats: MermaidSectionStats = {
        'total': 0,
        'valid': 0,
        'fixed': 0,
        'failed': 0
    }

    # Extract mermaid blocks
    blocks = validator.extract_mermaid_blocks(section_content, section_id)

    if not blocks:
        return section_content, stats

    print(f"    → Found {len(blocks)} mermaid diagram(s), validating...")

    fixed_blocks = []
    for i, block in enumerate(blocks, 1):
        print(f"      [{i}/{len(blocks)}] Validating...")
        # Pass section_content as context for fixing
        fixed_block, was_fixed, status = await validator.validate_and_fix_block(
            block,
            section_content=section_content
        )
        fixed_blocks.append(fixed_block)
        stats['total'] += 1

        if status == "valid":
            stats['valid'] += 1
            print(f"        ✓ Valid")
        elif "fixed" in status:
            stats['fixed'] += 1
            print(f"        ✓ {status}")
        else:
            stats['failed'] += 1
            print(f"        ✗ {status}")

    # Replace blocks in section content
    fixed_content = validator.replace_blocks_in_markdown(
        section_content, blocks, fixed_blocks
    )

    return fixed_content, stats


def validate_section_mermaid_sync(
    section_id: str,
    section_content: str,
    llm_config: Dict[str, Any],
    mcp_client: Optional["MCPClient"] = None,
    docker_image: str = "mermaid-mcp:test",
    fallback_manager: Optional[Any] = None
) -> Tuple[str, MermaidSectionStats]:
    """
    Synchronous wrapper for per-section mermaid validation.

    Called from run_phase2_sections() after each section is generated.

    Args:
        section_id: Section identifier
        section_content: Full section markdown content
        llm_config: LLM configuration
        mcp_client: Optional existing MCP client (to reuse connection)
        docker_image: Mermaid MCP Docker image name
        fallback_manager: Optional LLMFallbackManager for automatic fallback on errors

    Returns:
        Tuple of (fixed_section_content, stats_dict)
    """
    async def _validate() -> Tuple[str, MermaidSectionStats]:
        validator = MermaidValidator(
            docker_image=docker_image,
            llm_config=llm_config,
            fallback_manager=fallback_manager
        )

        # Check if section has any mermaid blocks first (quick check)
        if '```mermaid' not in section_content:
            empty_stats: MermaidSectionStats = {'total': 0, 'valid': 0, 'fixed': 0, 'failed': 0}
            return section_content, empty_stats

        try:
            await validator.initialize()
            return await validate_section_mermaid(section_id, section_content, validator)
        finally:
            await validator.cleanup()

    return asyncio.run(_validate())
