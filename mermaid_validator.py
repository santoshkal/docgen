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
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

from mcp_use import MCPClient


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

    def __init__(self, docker_image: str = "mermaid-mcp:test", llm_config: Dict[str, Any] = None):
        """
        Initialize the Mermaid validator.

        Args:
            docker_image: Docker image name for Mermaid MCP server
            llm_config: LLM configuration for fixing invalid diagrams
        """
        self.docker_image = docker_image
        self.llm_config = llm_config or {}
        self.mcp_client: MCPClient = None
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

    def fix_mermaid_with_llm(self, invalid_code: str, error: str) -> str:
        """
        Use LLM to fix invalid mermaid diagram.

        Args:
            invalid_code: The invalid mermaid code
            error: Error message from validator

        Returns:
            Fixed mermaid code
        """
        from langchain_core.messages import HumanMessage, SystemMessage
        from langchain_openai import ChatOpenAI

        # Create LLM instance
        llm = ChatOpenAI(
            model=self.llm_config.get('model', 'gpt-4.1'),
            api_key=self.llm_config.get('api_key'),
            temperature=0.1  # Low temperature for deterministic fixes
        )

        system_prompt = """You are a Mermaid diagram syntax expert. Your task is to fix invalid Mermaid diagram code so it renders in VSCode Mermaid preview.

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

        response = llm.invoke(messages)
        fixed_code = response.content.strip()

        # Remove any markdown fences if LLM included them
        if fixed_code.startswith('```mermaid'):
            fixed_code = fixed_code[10:]  # Remove ```mermaid\n
        if fixed_code.startswith('```'):
            fixed_code = fixed_code[3:]
        if fixed_code.endswith('```'):
            fixed_code = fixed_code[:-3]

        return fixed_code.strip()

    async def validate_and_fix_block(self, block: MermaidBlock) -> Tuple[MermaidBlock, bool, str]:
        """
        Validate a mermaid block and fix if invalid.

        Args:
            block: MermaidBlock to validate

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
                current_code = self.fix_mermaid_with_llm(current_code, error)

        # Max retries exceeded - return original with warning
        print(f"      ⚠ Max retries exceeded, marking as invalid")
        warning_block = MermaidBlock(
            code=f"[INVALID DIAGRAM - needs manual review]\n%% Error: {error}\n%% Original code:\n{original_code}",
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
) -> Tuple[str, Dict[str, str], Dict[str, Any]]:
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
    stats = {
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
) -> Tuple[str, Dict[str, str], Dict[str, Any]]:
    """
    Synchronous wrapper for mermaid validation.

    Can be called from generate_documentation().
    """
    return asyncio.run(validate_all_mermaid_in_sections(
        code_explanation=code_explanation,
        section_outputs=section_outputs,
        llm_config=llm_config,
        docker_image=docker_image
    ))
