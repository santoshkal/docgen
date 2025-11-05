"""
LLM Call Tracer and Runtime Monitor

Tracks all LLM calls during agent runtime with:
- Call timing (duration per call)
- Token counting (input/output tokens)
- Call metadata (section, pass, model)
- Total statistics

Provides detailed logging and summary reports.
"""

import time
import json
from datetime import datetime
from typing import Dict, Any, List, Optional
from pathlib import Path
from collections import defaultdict


class LLMCallTracer:
    """
    Tracks all LLM calls made during agent runtime.

    Usage:
        tracer = LLMCallTracer("trace.jsonl")

        with tracer.track_call(section_id="executive-summary"):
            response = llm.invoke(messages)
    """

    def __init__(self, log_file: str = "llm_trace.jsonl"):
        """
        Initialize tracer.

        Args:
            log_file: Path to JSONL log file
        """
        self.log_file = Path(log_file)
        self.calls: List[Dict[str, Any]] = []
        self.current_call: Optional[Dict[str, Any]] = None
        self.call_count = 0
        self.total_duration = 0.0
        self.total_input_tokens = 0
        self.total_output_tokens = 0

        # Per-section statistics
        self.section_stats = defaultdict(lambda: {
            'count': 0,
            'duration': 0.0,
            'input_tokens': 0,
            'output_tokens': 0
        })

        # Initialize log file
        self._init_log_file()

    def _init_log_file(self):
        """Create/clear log file and write header."""
        with open(self.log_file, 'w') as f:
            header = {
                'type': 'session_start',
                'timestamp': datetime.now().isoformat(),
                'agent': 'cobol_doc_agent'
            }
            f.write(json.dumps(header) + '\n')

    def estimate_tokens(self, text: str) -> int:
        """
        Estimate token count for text.

        Conservative estimate: 1 token ≈ 4 characters
        """
        if not text:
            return 0
        return len(text) // 4

    def start_call(
        self,
        section_id: str,
        section_title: str = "",
        pass_number: Optional[int] = None,
        chunk_number: Optional[int] = None,
        model: str = "unknown"
    ) -> int:
        """
        Start tracking a new LLM call.

        Returns:
            call_id for this call
        """
        self.call_count += 1

        self.current_call = {
            'call_id': self.call_count,
            'section_id': section_id,
            'section_title': section_title,
            'pass_number': pass_number,
            'chunk_number': chunk_number,
            'model': model,
            'start_time': time.time(),
            'start_timestamp': datetime.now().isoformat()
        }

        return self.call_count

    def end_call(
        self,
        response: Any,
        input_messages: List[Any],
        input_text: Optional[str] = None
    ):
        """
        End tracking current LLM call.

        Args:
            response: LLM response object
            input_messages: List of messages sent to LLM
            input_text: Optional raw input text for token counting
        """
        if not self.current_call:
            return

        end_time = time.time()
        duration = end_time - self.current_call['start_time']

        # Try to get ACTUAL token counts from response metadata
        actual_input_tokens = None
        actual_output_tokens = None
        token_source = "estimated"

        if hasattr(response, 'response_metadata'):
            metadata = response.response_metadata

            # OpenAI format: response_metadata['token_usage']
            if 'token_usage' in metadata:
                token_usage = metadata['token_usage']
                actual_input_tokens = token_usage.get('prompt_tokens')
                actual_output_tokens = token_usage.get('completion_tokens')
                if actual_input_tokens is not None and actual_output_tokens is not None:
                    token_source = "actual_openai"

            # Anthropic format: response_metadata['usage']
            elif 'usage' in metadata:
                usage = metadata['usage']
                actual_input_tokens = usage.get('input_tokens')
                actual_output_tokens = usage.get('output_tokens')
                if actual_input_tokens is not None and actual_output_tokens is not None:
                    token_source = "actual_anthropic"

        # Use actual counts if available, otherwise estimate
        if actual_input_tokens is not None:
            input_tokens = actual_input_tokens
        else:
            # Fallback to estimation
            if input_text:
                input_tokens = self.estimate_tokens(input_text)
            else:
                # Estimate from messages
                input_tokens = sum(
                    self.estimate_tokens(str(msg.content))
                    for msg in input_messages
                )

        if actual_output_tokens is not None:
            output_tokens = actual_output_tokens
        else:
            # Fallback to estimation
            output_text = getattr(response, 'content', str(response))
            output_tokens = self.estimate_tokens(output_text)

        # Get output text length
        output_text = getattr(response, 'content', str(response))

        # Complete call record
        self.current_call.update({
            'end_time': end_time,
            'end_timestamp': datetime.now().isoformat(),
            'duration_seconds': round(duration, 3),
            'input_tokens': input_tokens,
            'output_tokens': output_tokens,
            'total_tokens': input_tokens + output_tokens,
            'token_count_source': token_source,  # "actual_openai", "actual_anthropic", or "estimated"
            'output_length': len(output_text)
        })

        # Update totals
        self.total_duration += duration
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens

        # Update section stats
        section_id = self.current_call['section_id']
        self.section_stats[section_id]['count'] += 1
        self.section_stats[section_id]['duration'] += duration
        self.section_stats[section_id]['input_tokens'] += input_tokens
        self.section_stats[section_id]['output_tokens'] += output_tokens

        # Store call
        self.calls.append(self.current_call.copy())

        # Log to file
        self._log_call(self.current_call)

        # Reset current
        self.current_call = None

    def _log_call(self, call_record: Dict[str, Any]):
        """Write call record to log file."""
        with open(self.log_file, 'a') as f:
            log_entry = {
                'type': 'llm_call',
                **call_record
            }
            f.write(json.dumps(log_entry) + '\n')

    def get_summary(self) -> Dict[str, Any]:
        """
        Get summary statistics.

        Returns:
            Dict with summary statistics
        """
        return {
            'total_calls': self.call_count,
            'total_duration_seconds': round(self.total_duration, 3),
            'total_duration_minutes': round(self.total_duration / 60, 2),
            'total_input_tokens': self.total_input_tokens,
            'total_output_tokens': self.total_output_tokens,
            'total_tokens': self.total_input_tokens + self.total_output_tokens,
            'average_duration_seconds': round(self.total_duration / self.call_count, 3) if self.call_count > 0 else 0,
            'average_input_tokens': round(self.total_input_tokens / self.call_count, 1) if self.call_count > 0 else 0,
            'average_output_tokens': round(self.total_output_tokens / self.call_count, 1) if self.call_count > 0 else 0
        }

    def get_section_summary(self) -> Dict[str, Dict[str, Any]]:
        """Get per-section statistics."""
        return dict(self.section_stats)

    def print_summary(self):
        """Print formatted summary to console."""
        summary = self.get_summary()

        print("\n" + "=" * 80)
        print("LLM CALL TRACE SUMMARY")
        print("=" * 80)
        print(f"\nTotal LLM Calls: {summary['total_calls']}")
        print(f"Total Duration: {summary['total_duration_minutes']} minutes ({summary['total_duration_seconds']} seconds)")
        print(f"Average Call Duration: {summary['average_duration_seconds']} seconds")

        # Token count accuracy
        actual_count = sum(1 for call in self.calls if call.get('token_count_source', '').startswith('actual'))
        estimated_count = len(self.calls) - actual_count
        if actual_count > 0:
            print(f"\nToken Count Accuracy:")
            print(f"  Actual (from LLM):  {actual_count} calls")
            print(f"  Estimated:          {estimated_count} calls")

        print(f"\nToken Usage:")
        print(f"  Input Tokens:  {summary['total_input_tokens']:,}")
        print(f"  Output Tokens: {summary['total_output_tokens']:,}")
        print(f"  Total Tokens:  {summary['total_tokens']:,}")
        print(f"  Avg Input:     {summary['average_input_tokens']:,.1f} tokens/call")
        print(f"  Avg Output:    {summary['average_output_tokens']:,.1f} tokens/call")

        # Section breakdown
        print(f"\n{'-' * 80}")
        print("PER-SECTION BREAKDOWN")
        print(f"{'-' * 80}")
        print(f"{'Section':<40} {'Calls':<8} {'Duration':<12} {'Tokens':<12}")
        print(f"{'-' * 80}")

        section_stats = self.get_section_summary()
        for section_id, stats in sorted(section_stats.items(), key=lambda x: x[1]['duration'], reverse=True):
            duration_str = f"{stats['duration']:.1f}s"
            tokens_str = f"{stats['input_tokens'] + stats['output_tokens']:,}"
            print(f"{section_id:<40} {stats['count']:<8} {duration_str:<12} {tokens_str:<12}")

        print("=" * 80)

    def write_detailed_report(self, report_file: str = "llm_trace_report.txt"):
        """
        Write detailed text report with all calls.

        Args:
            report_file: Path to report file
        """
        with open(report_file, 'w') as f:
            f.write("=" * 80 + "\n")
            f.write("DETAILED LLM CALL TRACE REPORT\n")
            f.write("=" * 80 + "\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write(f"Log File: {self.log_file}\n\n")

            # Summary
            summary = self.get_summary()
            f.write("SUMMARY\n")
            f.write("-" * 80 + "\n")
            f.write(f"Total Calls:       {summary['total_calls']}\n")
            f.write(f"Total Duration:    {summary['total_duration_minutes']} minutes\n")
            f.write(f"Total Input Tokens: {summary['total_input_tokens']:,}\n")
            f.write(f"Total Output Tokens: {summary['total_output_tokens']:,}\n")
            f.write(f"Total Tokens:      {summary['total_tokens']:,}\n\n")

            # Individual calls
            f.write("INDIVIDUAL CALLS\n")
            f.write("-" * 80 + "\n\n")

            for call in self.calls:
                f.write(f"Call #{call['call_id']}\n")
                f.write(f"  Section:       {call['section_id']}")
                if call.get('section_title'):
                    f.write(f" - {call['section_title']}")
                f.write("\n")

                if call.get('pass_number'):
                    f.write(f"  Pass:          {call['pass_number']}\n")
                if call.get('chunk_number'):
                    f.write(f"  Chunk:         {call['chunk_number']}\n")

                f.write(f"  Start:         {call['start_timestamp']}\n")
                f.write(f"  Duration:      {call['duration_seconds']} seconds\n")
                f.write(f"  Input Tokens:  {call['input_tokens']:,}\n")
                f.write(f"  Output Tokens: {call['output_tokens']:,}\n")
                f.write(f"  Output Length: {call['output_length']:,} chars\n")
                f.write("\n")

            f.write("=" * 80 + "\n")

    def write_pretty_json(self, json_file: str = "llm_trace.json"):
        """
        Write pretty-printed JSON file for better readability.

        This provides the same data as JSONL but in a structured,
        human-readable format with proper indentation.

        Args:
            json_file: Path to output JSON file
        """
        # Build structured JSON document
        trace_document = {
            'session_info': {
                'agent': 'cobol_doc_agent',
                'start_timestamp': self.calls[0]['start_timestamp'] if self.calls else datetime.now().isoformat(),
                'end_timestamp': datetime.now().isoformat()
            },
            'summary': self.get_summary(),
            'section_stats': self.get_section_summary(),
            'calls': []
        }

        # Add all calls with cleaned data (remove internal fields)
        for call in self.calls:
            call_data = {
                'call_id': call['call_id'],
                'section_id': call['section_id'],
                'section_title': call['section_title'],
                'model': call['model'],
                'start_timestamp': call['start_timestamp'],
                'end_timestamp': call['end_timestamp'],
                'duration_seconds': call['duration_seconds'],
                'tokens': {
                    'input': call['input_tokens'],
                    'output': call['output_tokens'],
                    'total': call['total_tokens'],
                    'source': call.get('token_count_source', 'estimated')
                },
                'output_length': call['output_length']
            }

            # Add optional fields if present
            if call.get('pass_number'):
                call_data['pass_number'] = call['pass_number']
            if call.get('chunk_number'):
                call_data['chunk_number'] = call['chunk_number']

            trace_document['calls'].append(call_data)

        # Write pretty-printed JSON
        with open(json_file, 'w') as f:
            json.dump(trace_document, f, indent=2, sort_keys=False)

    def finalize(self):
        """
        Finalize tracing session.

        Writes summary to log file and generates reports.
        """
        # Write summary to JSONL log file
        with open(self.log_file, 'a') as f:
            summary_entry = {
                'type': 'session_end',
                'timestamp': datetime.now().isoformat(),
                'summary': self.get_summary(),
                'section_stats': self.get_section_summary()
            }
            f.write(json.dumps(summary_entry) + '\n')

        # Print summary
        self.print_summary()

        # Write detailed text report
        report_file = str(self.log_file).replace('.jsonl', '_report.txt')
        self.write_detailed_report(report_file)

        # Write pretty JSON for readability (NEW!)
        json_file = str(self.log_file).replace('.jsonl', '.json')
        self.write_pretty_json(json_file)

        print(f"\n✓ Trace log written to: {self.log_file} (JSONL format)")
        print(f"✓ Pretty JSON written to: {json_file} (readable format)")
        print(f"✓ Detailed report written to: {report_file}")


# Global tracer instance
_tracer: Optional[LLMCallTracer] = None


def init_tracer(log_file: str = "llm_trace.jsonl") -> LLMCallTracer:
    """
    Initialize global tracer.

    Args:
        log_file: Path to log file

    Returns:
        Tracer instance
    """
    global _tracer
    _tracer = LLMCallTracer(log_file)
    return _tracer


def get_tracer() -> Optional[LLMCallTracer]:
    """Get global tracer instance."""
    return _tracer


def finalize_tracer():
    """Finalize global tracer."""
    if _tracer:
        _tracer.finalize()
