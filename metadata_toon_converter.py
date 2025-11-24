#!/usr/bin/env python3
"""
TOON Format Converter for Metadata Files

Converts metadata dictionaries to TOON format for token-efficient LLM transmission.
Only converts metadata types with significant token savings (>20%).

Token Savings (measured with tiktoken):
- CTags Outline: 37.4% reduction
- SuperBOL Symbols: 23.1% reduction
- GnuCOBOL Analysis: 0% reduction (kept as JSON)
"""
import json
import subprocess
import tempfile
from pathlib import Path
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

# Metadata types that benefit from TOON (>20% token savings)
TOON_ELIGIBLE_TYPES = {
    'ctags': 37.4,              # 37.4% token savings
    'superbolsymbols': 23.1,    # 23.1% token savings (normalized form)
}

# Metadata types that should stay as JSON (minimal/no savings)
JSON_ONLY_TYPES = {
    'gnucobol': 0.0,        # 0% token savings
    'superbol_cfg': 0.0,    # Not yet measured, conservative
}


def convert_to_toon(data: Dict[str, Any], metadata_type: str) -> str:
    """
    Convert metadata dictionary to TOON format if beneficial.

    Args:
        data: Metadata dictionary to convert
        metadata_type: Type of metadata ('ctags', 'superbol_symbols', 'gnucobol', etc.)

    Returns:
        TOON-formatted string if beneficial, otherwise JSON string

    Example:
        >>> ctags_data = {"paragraphs": [...], "sections": [...]}
        >>> toon_str = convert_to_toon(ctags_data, 'ctags')
        # Returns TOON format (37.4% smaller)
    """
    # Normalize metadata type (handle variations like superbol-symbols, superbol_symbols, superbolsymbols)
    normalized = metadata_type.lower().replace('_', '').replace('-', '')

    # Map common variations
    if 'superbol' in normalized and 'symbol' in normalized:
        normalized = 'superbolsymbols'
    elif 'ctags' in normalized:
        normalized = 'ctags'
    elif 'gnucobol' in normalized:
        normalized = 'gnucobol'

    # Check if TOON conversion is beneficial
    if normalized not in TOON_ELIGIBLE_TYPES:
        logger.debug(f"Metadata type '{metadata_type}' not eligible for TOON, using JSON")
        return json.dumps(data, indent=2)

    try:
        # Create temporary file for conversion
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp:
            json.dump(data, tmp)
            temp_path = tmp.name

        # Convert using TOON CLI
        result = subprocess.run(
            ['npx', '@toon-format/cli', temp_path],
            capture_output=True,
            text=True,
            timeout=60  # 60 second timeout
        )

        # Cleanup temp file
        Path(temp_path).unlink()

        if result.returncode == 0:
            toon_output = result.stdout
            logger.debug(f"Successfully converted {metadata_type} to TOON format")
            return toon_output
        else:
            logger.warning(f"TOON conversion failed for {metadata_type}: {result.stderr}")
            return json.dumps(data, indent=2)

    except subprocess.TimeoutExpired:
        logger.error(f"TOON conversion timeout for {metadata_type}")
        return json.dumps(data, indent=2)
    except Exception as e:
        logger.error(f"TOON conversion error for {metadata_type}: {e}")
        return json.dumps(data, indent=2)


def should_use_toon(metadata_type: str) -> bool:
    """
    Check if metadata type should be converted to TOON.

    Args:
        metadata_type: Type of metadata

    Returns:
        True if TOON conversion is beneficial
    """
    normalized = metadata_type.lower().replace('_', '').replace('-', '')
    return normalized in TOON_ELIGIBLE_TYPES


def get_expected_savings(metadata_type: str) -> float:
    """
    Get expected token savings percentage for metadata type.

    Args:
        metadata_type: Type of metadata

    Returns:
        Expected savings percentage (0-100)
    """
    normalized = metadata_type.lower().replace('_', '').replace('-', '')
    return TOON_ELIGIBLE_TYPES.get(normalized, 0.0)


# Convenience functions for specific metadata types

def convert_ctags_to_toon(ctags_data: Dict[str, Any]) -> str:
    """Convert CTags metadata to TOON (37.4% savings)"""
    return convert_to_toon(ctags_data, 'ctags')


def convert_superbol_symbols_to_toon(symbols_data: Dict[str, Any]) -> str:
    """Convert SuperBOL symbols to TOON (23.1% savings)"""
    return convert_to_toon(symbols_data, 'superbol_symbols')


def convert_gnucobol_to_json(gnucobol_data: Dict[str, Any]) -> str:
    """Keep GnuCOBOL as JSON (0% TOON savings, not worth it)"""
    return json.dumps(gnucobol_data, indent=2)


if __name__ == '__main__':
    # Test script
    print("TOON Converter Module")
    print("=" * 70)
    print("\nMetadata Types and Expected Savings:")
    print("-" * 70)
    for mtype, savings in TOON_ELIGIBLE_TYPES.items():
        print(f"  {mtype:25s} → {savings:>5.1f}% token savings")
    print("\nJSON-Only Types (no benefit):")
    print("-" * 70)
    for mtype, savings in JSON_ONLY_TYPES.items():
        print(f"  {mtype:25s} → {savings:>5.1f}% token savings")
