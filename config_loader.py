"""
Configuration Loader for COBOL Documentation Agent

Loads and parses YAML configuration files with:
- Environment variable substitution
- Validation of required fields
- Default values
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, Any, Optional


class ConfigLoader:
    """Loads and validates YAML configuration for the agent"""

    def __init__(self, config_path: str):
        """
        Initialize config loader

        Args:
            config_path: Path to YAML configuration file
        """
        self.config_path = Path(config_path)
        self.config: Optional[Dict[str, Any]] = None

    def _ensure_loaded(self) -> Dict[str, Any]:
        """
        Ensure configuration is loaded

        Returns:
            Loaded configuration dictionary

        Raises:
            RuntimeError: If config hasn't been loaded yet
        """
        if self.config is None:
            raise RuntimeError("Configuration not loaded. Call load() first.")
        return self.config

    def load(self) -> Dict[str, Any]:
        """
        Load and parse configuration file

        Returns:
            Parsed configuration dictionary

        Raises:
            FileNotFoundError: If config file doesn't exist
            ValueError: If config is invalid
        """
        if not self.config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")

        with open(self.config_path, 'r') as f:
            raw_config = yaml.safe_load(f)

        if not raw_config:
            raise ValueError(f"Configuration file is empty: {self.config_path}")

        # Expand environment variables and store
        expanded_config: Dict[str, Any] = self._expand_env_vars(raw_config)
        self.config = expanded_config

        # Validate required sections
        self._validate_config()

        # Return the loaded config (type checker knows this is Dict[str, Any])
        return expanded_config

    def _expand_env_vars(self, obj: Any) -> Any:
        """
        Recursively expand environment variables in config

        Supports ${VAR_NAME} syntax

        Args:
            obj: Configuration object (dict, list, str, etc.)

        Returns:
            Object with environment variables expanded
        """
        if isinstance(obj, dict):
            return {k: self._expand_env_vars(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._expand_env_vars(item) for item in obj]
        elif isinstance(obj, str):
            # Match ${VAR_NAME} pattern
            pattern = r'\$\{([^}]+)\}'
            matches = re.findall(pattern, obj)

            for var_name in matches:
                env_value = os.environ.get(var_name, '')
                if not env_value:
                    print(f"⚠ Warning: Environment variable not set: {var_name}")
                obj = obj.replace(f'${{{var_name}}}', env_value)

            return obj
        else:
            return obj

    def _validate_config(self) -> None:
        """Validate that required configuration sections exist"""
        config = self._ensure_loaded()
        required_sections = ['source', 'output', 'llm']

        for section in required_sections:
            if section not in config:
                raise ValueError(f"Missing required configuration section: {section}")

    def get_source_config(self) -> Dict[str, Any]:
        """Get source files configuration"""
        config = self._ensure_loaded()
        return config.get('source', {})

    def get_language_config(self) -> str:
        """
        Get the language setting from source configuration.

        Reads source.language from config, defaulting to 'cobol'
        for backward compatibility.

        Returns:
            Language identifier string (e.g., 'cobol', 'dotnet')
        """
        source_config = self.get_source_config()
        return source_config.get('language', 'cobol')

    def get_file_filter_config(self) -> Dict[str, Any]:
        """
        Get file filtering configuration from source section.

        Returns configuration for filtering which files to process:
        - extensions_include: List of extensions to include (e.g., ['.c74', '.XMOD'])
        - extensions_exclude: List of extensions to exclude (e.g., ['.xgn'])
        - exclude_files: List of file patterns to exclude (e.g., ['TEST*', '*-BACKUP.*'])
        - include_files: List of file patterns to include (overrides all other filters)

        Priority order:
        1. include_files (if set, ONLY these files)
        2. extensions_include OR extensions_exclude
        3. exclude_files (remove matches)

        Returns:
            Dictionary with file filter configuration
        """
        config = self._ensure_loaded()
        source_config = config.get('source', {})

        # Extract filter settings from source config
        extensions_config = source_config.get('extensions', {})

        return {
            'extensions_include': extensions_config.get('include', []),
            'extensions_exclude': extensions_config.get('exclude', []),
            'exclude_files': source_config.get('exclude_files', []),
            'include_files': source_config.get('include_files', []),
        }

    def get_output_config(self) -> Dict[str, Any]:
        """Get output paths configuration"""
        config = self._ensure_loaded()
        return config.get('output', {})

    def get_checksum_config(self) -> Dict[str, Any]:
        """Get checksum validation configuration"""
        config = self._ensure_loaded()
        return config.get('validate_checksums', {})

    def get_metadata_config(self) -> Dict[str, Any]:
        """Get metadata generation configuration"""
        config = self._ensure_loaded()
        return config.get('metadata', {})

    def get_template_config(self) -> Dict[str, Any]:
        """Get template configuration"""
        config = self._ensure_loaded()
        return config.get('template', {})

    def get_llm_config(self) -> Dict[str, Any]:
        """Get LLM provider configuration"""
        config = self._ensure_loaded()
        return config.get('llm', {})

    def get_logging_config(self) -> Dict[str, Any]:
        """Get logging configuration"""
        config = self._ensure_loaded()
        return config.get('logging', {})

    def get_servers_config(self) -> Dict[str, Any]:
        """Get MCP servers configuration"""
        config = self._ensure_loaded()
        return config.get('servers', {})

    def get_source_extraction_config(self) -> Dict[str, Any]:
        """Get source code extraction configuration (Phase 1)"""
        config = self._ensure_loaded()
        return config.get('source_extraction', {})

    def get_program_map_config(self) -> Dict[str, Any]:
        """
        Get program map configuration.

        Returns configuration for program map generation including:
        - top_n_paragraphs: Number of top paragraphs to include (-1 for all)
        - top_n_data_items: Number of top data items to include (-1 for all)
        - show_all: Whether to show all elements (overrides top_n settings)
        - dynamic_limits: Configuration for automatic size-based limits
        - tiered_details: Configuration for tiered detail levels

        Returns:
            Dictionary with program map configuration, or defaults if not set
        """
        config = self._ensure_loaded()
        pm_config = config.get('program_map', {})

        # Build result with defaults
        result = {
            'top_n_paragraphs': pm_config.get('top_n_paragraphs', 30),
            'top_n_data_items': pm_config.get('top_n_data_items', 20),
            'show_all': pm_config.get('show_all', False)
        }

        # Include dynamic_limits if present
        if 'dynamic_limits' in pm_config:
            result['dynamic_limits'] = pm_config['dynamic_limits']

        # Include tiered_details if present
        if 'tiered_details' in pm_config:
            result['tiered_details'] = pm_config['tiered_details']

        # Include mandatory_elements if present
        if 'mandatory_elements' in pm_config:
            result['mandatory_elements'] = pm_config['mandatory_elements']

        return result

    def get_workflow_config(self) -> Dict[str, Any]:
        """
        Get workflow configuration.

        Returns configuration for workflow behavior:
        - auto_start_phase2: Whether to auto-start Phase 2 after Phase 1 (default: True)

        Returns:
            Dictionary with workflow configuration
        """
        config = self._ensure_loaded()
        wf_config = config.get('workflow', {})

        return {
            'auto_start_phase2': wf_config.get('auto_start_phase2', True),
        }

    def get_run_logging_config(self) -> Dict[str, Any]:
        """
        Get run logging configuration.

        Run logging is always enabled — all artifacts go into a centralized
        per-run directory. These flags control optional sub-features:
        - console_tee: Whether to tee stdout/stderr to files (default: True)
        - capture_requests: Whether to route debug requests into run dir (default: True)
        - capture_traces: Whether to route LLM traces into run dir (default: True)

        Returns:
            Dictionary with run logging configuration
        """
        config = self._ensure_loaded()
        rl_config = config.get('run_logging', {})

        return {
            'console_tee': rl_config.get('console_tee', True),
            'capture_requests': rl_config.get('capture_requests', True),
            'capture_traces': rl_config.get('capture_traces', True),
        }

    def get_full_context_config(self) -> Dict[str, Any]:
        """
        Get full context mode configuration.

        Full context mode sends complete source code + metadata + program map
        to the LLM for each section, enabling more comprehensive documentation.

        Returns configuration for full context mode including:
        - enabled: Whether full context mode is enabled (default: False)
        - sections: List of section IDs that should use full context

        Returns:
            Dictionary with full context configuration, with defaults if not set
        """
        config = self._ensure_loaded()
        fc_config = config.get('full_context', {})

        # Default sections for full context mode
        default_sections = [
            'executive-summary',
            'key-responsibilities',
            'business-logic',
            'overview',
            'data-flow-analysis',
        ]

        # Build result with defaults
        enabled = fc_config.get('enabled', False)

        result = {
            'enabled': enabled,
            # If enabled but no sections specified, use defaults
            # If disabled, use empty list
            'sections': fc_config.get('sections', default_sections if enabled else []),
        }

        # Include program_map_overrides if present
        if 'program_map_overrides' in fc_config:
            result['program_map_overrides'] = fc_config['program_map_overrides']

        # Include context_chaining configuration (US-4.1)
        chaining_config = fc_config.get('context_chaining', {})
        result['context_chaining'] = {
            'enabled': chaining_config.get('enabled', False),
            'max_tokens': chaining_config.get('max_tokens', None),
        }

        # Include max_message_chars for API limit protection
        # OpenAI API has ~10MB message limit, default to 9MB for safety
        result['max_message_chars'] = fc_config.get('max_message_chars', 9000000)

        return result

    def to_agent_params(self) -> Dict[str, Any]:
        """
        Convert configuration to agent function parameters

        Returns:
            Dictionary of parameters for generate_documentation()
        """
        source_config = self.get_source_config()
        output_config = self.get_output_config()
        checksum_config = self.get_checksum_config()
        metadata_config = self.get_metadata_config()
        template_config = self.get_template_config()

        # Determine program name and workspace
        mode = source_config.get('mode', 'single')
        program_name = source_config.get('program_name')
        source_files = source_config.get('source_files')

        # Get full context config
        full_context_config = self.get_full_context_config()

        # Build parameters
        params = {
            'program_name': program_name,
            'workspace_path': source_files if mode == 'batch' else '..',
            'metadata_dir': output_config.get('metadata_dir', '../output'),
            'template_path': template_config.get('path', './cobol-doc-template.yaml'),
            'output_dir': output_config.get('docs_path', '../docs'),
            'generate_metadata': metadata_config.get('generate', True),
            'skip_existing_metadata': metadata_config.get('skip_existing', True),
            'source_checksum_path': checksum_config.get('source_checksum_file_path', './source-checksum.yaml'),
            'metadata_checksum_path': checksum_config.get('metadata_checksum_file_path', './metadata-checksum.yaml'),
            # Full context mode parameters
            'use_full_context_mode': full_context_config['enabled'],
            'full_context_sections': full_context_config['sections'],
        }

        return params

    def get_batch_mode_info(self) -> tuple[bool, Optional[str]]:
        """
        Check if running in batch mode

        Returns:
            Tuple of (is_batch_mode, source_path)
        """
        source_config = self.get_source_config()
        mode = source_config.get('mode', 'single')
        source_files = source_config.get('source_files')

        if mode == 'batch' and source_files:
            return True, source_files
        else:
            return False, None


def load_config(config_path: str) -> ConfigLoader:
    """
    Convenience function to load configuration

    Args:
        config_path: Path to YAML configuration file

    Returns:
        Loaded ConfigLoader instance
    """
    loader = ConfigLoader(config_path)
    loader.load()
    return loader


# Example usage
if __name__ == "__main__":
    # Test config loader
    import sys

    if len(sys.argv) > 1:
        config_file = sys.argv[1]
    else:
        config_file = "config.minimal.yaml"

    try:
        print(f"Loading configuration from: {config_file}")
        print("="*70)

        loader = load_config(config_file)

        print("\n📋 Configuration Summary:")
        print(f"  Source mode: {loader.get_source_config().get('mode')}")
        print(f"  Source files: {loader.get_source_config().get('source_files')}")
        print(f"  Program name: {loader.get_source_config().get('program_name')}")
        print(f"  Metadata dir: {loader.get_output_config().get('metadata_dir')}")
        print(f"  Docs path: {loader.get_output_config().get('docs_path')}")
        print(f"  Generate metadata: {loader.get_metadata_config().get('generate')}")
        print(f"  LLM provider: {loader.get_llm_config().get('provider')}")
        print(f"  LLM model: {loader.get_llm_config().get('model')}")

        print("\n✅ Configuration loaded successfully!")

        print("\n🔧 Agent Parameters:")
        params = loader.to_agent_params()
        for key, value in params.items():
            print(f"  {key}: {value}")

    except Exception as e:
        print(f"\n❌ Error loading configuration: {e}")
        import traceback
        traceback.print_exc()
