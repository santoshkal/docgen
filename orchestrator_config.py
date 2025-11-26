"""
Orchestrator Configuration Validator and Loader

This module provides configuration validation and default value handling
for the orchestrator enhancement. It ensures all required settings are
present and valid before starting parallel agent execution.
"""

import os
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


@dataclass
class BatchConfig:
    """Batch processing configuration."""
    mode: str = "batch"  # "batch" or "all"
    size: int = 10

    def validate(self) -> List[str]:
        """Validate batch configuration. Returns list of errors."""
        errors = []
        if self.mode not in ("batch", "all"):
            errors.append(f"Invalid batch.mode: '{self.mode}'. Must be 'batch' or 'all'")
        if self.size < 1:
            errors.append(f"Invalid batch.size: {self.size}. Must be >= 1")
        if self.size > 100:
            logger.warning(f"Large batch size ({self.size}) may cause memory issues")
        return errors


@dataclass
class RayConfig:
    """Ray distributed execution configuration."""
    local: bool = True
    num_cpus: Optional[int] = None
    num_gpus: Optional[int] = None
    memory_per_worker_gb: Optional[float] = None
    object_store_memory_gb: Optional[float] = None
    cluster_address: Optional[str] = None

    def validate(self) -> List[str]:
        """Validate Ray configuration. Returns list of errors."""
        errors = []
        if not self.local and not self.cluster_address:
            errors.append("ray.cluster_address is required when ray.local = false")
        if self.num_cpus is not None and self.num_cpus < 1:
            errors.append(f"Invalid ray.num_cpus: {self.num_cpus}. Must be >= 1")
        if self.num_gpus is not None and self.num_gpus < 0:
            errors.append(f"Invalid ray.num_gpus: {self.num_gpus}. Must be >= 0")
        if self.memory_per_worker_gb is not None and self.memory_per_worker_gb < 0.5:
            errors.append(f"Invalid ray.memory_per_worker_gb: {self.memory_per_worker_gb}. Must be >= 0.5")
        return errors


@dataclass
class RetryConfig:
    """Retry and error handling configuration."""
    max_attempts: int = 3
    initial_delay_seconds: float = 3.0
    strategy: str = "exponential"  # "exponential" or "fixed"
    max_delay_seconds: float = 60.0

    def validate(self) -> List[str]:
        """Validate retry configuration. Returns list of errors."""
        errors = []
        if self.max_attempts < 1:
            errors.append(f"Invalid retry.max_attempts: {self.max_attempts}. Must be >= 1")
        if self.initial_delay_seconds < 0:
            errors.append(f"Invalid retry.initial_delay_seconds: {self.initial_delay_seconds}. Must be >= 0")
        if self.strategy not in ("exponential", "fixed"):
            errors.append(f"Invalid retry.strategy: '{self.strategy}'. Must be 'exponential' or 'fixed'")
        if self.max_delay_seconds < self.initial_delay_seconds:
            errors.append("retry.max_delay_seconds must be >= retry.initial_delay_seconds")
        return errors

    def calculate_delay(self, attempt: int) -> float:
        """Calculate delay for given retry attempt (0-indexed)."""
        if self.strategy == "fixed":
            return self.initial_delay_seconds

        # Exponential backoff: initial * 2^attempt
        delay = self.initial_delay_seconds * (2 ** attempt)
        return min(delay, self.max_delay_seconds)


@dataclass
class CircuitBreakerConfig:
    """Circuit breaker configuration."""
    enabled: bool = True
    failure_threshold: int = 5
    recovery_timeout_seconds: float = 60.0

    def validate(self) -> List[str]:
        """Validate circuit breaker configuration. Returns list of errors."""
        errors = []
        if self.failure_threshold < 1:
            errors.append(f"Invalid circuit_breaker.failure_threshold: {self.failure_threshold}. Must be >= 1")
        if self.recovery_timeout_seconds < 1:
            errors.append(f"Invalid circuit_breaker.recovery_timeout_seconds: {self.recovery_timeout_seconds}. Must be >= 1")
        return errors


@dataclass
class ProgressConfig:
    """Progress tracking configuration."""
    reports_dir: str = "./reports"
    realtime_updates: bool = True
    file_name: str = "project_progress.md"

    def validate(self) -> List[str]:
        """Validate progress configuration. Returns list of errors."""
        errors = []
        if not self.file_name:
            errors.append("progress.file_name cannot be empty")
        if not self.file_name.endswith(".md"):
            logger.warning(f"progress.file_name '{self.file_name}' does not end with .md")
        return errors

    @property
    def progress_file_path(self) -> Path:
        """Get full path to progress file."""
        return Path(self.reports_dir) / self.file_name


@dataclass
class OutputConfig:
    """Output organization configuration."""
    mirror_structure: bool = True
    docs_dir: str = "./docs"

    def validate(self) -> List[str]:
        """Validate output configuration. Returns list of errors."""
        errors = []
        if not self.docs_dir:
            errors.append("output.docs_dir cannot be empty")
        return errors


@dataclass
class SummaryConfig:
    """Project summary generation configuration."""
    enabled: bool = True
    file_name: str = "PROJECT_SUMMARY.md"
    include_dependency_graph: bool = True
    include_business_logic: bool = True

    def validate(self) -> List[str]:
        """Validate summary configuration. Returns list of errors."""
        errors = []
        if self.enabled and not self.file_name:
            errors.append("summary.file_name cannot be empty when summary.enabled = true")
        return errors


@dataclass
class TreeServerConfig:
    """Tree MCP server configuration."""
    docker_image: str  # Required - must be set in config.yaml
    tool: str = "tree_json_output"
    max_depth: Optional[int] = None
    extensions: List[str] = field(default_factory=lambda: [
        ".cbl", ".CBL", ".cob", ".COB", ".cpy", ".CPY", ".c74", ".C74"
    ])
    exclude_dirs: List[str] = field(default_factory=lambda: [
        ".git", "node_modules", "__pycache__", ".venv"
    ])

    def validate(self) -> List[str]:
        """Validate tree server configuration. Returns list of errors."""
        errors = []
        if self.tool not in ("tree_basic", "tree_json_output", "tree_xml_output"):
            errors.append(f"Invalid tree_server.tool: '{self.tool}'. Must be 'tree_basic', 'tree_json_output', or 'tree_xml_output'")
        if self.max_depth is not None and self.max_depth < 1:
            errors.append(f"Invalid tree_server.max_depth: {self.max_depth}. Must be >= 1 or null")
        if not self.docker_image:
            errors.append("tree_server.docker_image is required - no default, must be set in config.yaml")
        return errors


@dataclass
class OrchestratorConfig:
    """Main orchestrator configuration."""
    enabled: bool = False
    batch: BatchConfig = field(default_factory=BatchConfig)
    ray: RayConfig = field(default_factory=RayConfig)
    retry: RetryConfig = field(default_factory=RetryConfig)
    circuit_breaker: CircuitBreakerConfig = field(default_factory=CircuitBreakerConfig)
    progress: ProgressConfig = field(default_factory=ProgressConfig)
    output: OutputConfig = field(default_factory=OutputConfig)
    summary: SummaryConfig = field(default_factory=SummaryConfig)
    tree_server: Optional[TreeServerConfig] = None  # Required - must be loaded from config

    # Metadata directory (centralized location for MCP outputs)
    metadata_dir: str = "./metadata"

    def validate(self) -> List[str]:
        """
        Validate entire orchestrator configuration.
        Returns list of all validation errors.
        """
        errors = []

        # Validate all sub-configurations
        errors.extend(self.batch.validate())
        errors.extend(self.ray.validate())
        errors.extend(self.retry.validate())
        errors.extend(self.circuit_breaker.validate())
        errors.extend(self.progress.validate())
        errors.extend(self.output.validate())
        errors.extend(self.summary.validate())

        # tree_server is required
        if self.tree_server is None:
            errors.append("tree_server configuration is required - must be set in config.yaml")
        else:
            errors.extend(self.tree_server.validate())

        # Validate metadata_dir
        if not self.metadata_dir:
            errors.append("metadata_dir cannot be empty")

        return errors

    def ensure_directories(self) -> None:
        """Create required directories if they don't exist."""
        dirs_to_create = [
            self.metadata_dir,
            self.progress.reports_dir,
            self.output.docs_dir,
        ]

        for dir_path in dirs_to_create:
            path = Path(dir_path)
            if not path.exists():
                path.mkdir(parents=True, exist_ok=True)
                logger.info(f"Created directory: {path}")

    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> "OrchestratorConfig":
        """
        Create OrchestratorConfig from a dictionary (parsed YAML).

        Args:
            config_dict: Dictionary containing orchestrator configuration

        Returns:
            OrchestratorConfig instance with validated settings
        """
        orch_dict = config_dict.get("orchestrator", {})
        tree_dict = config_dict.get("tree_server", {})

        # Parse batch config
        batch_dict = orch_dict.get("batch", {})
        batch_config = BatchConfig(
            mode=batch_dict.get("mode", "batch"),
            size=batch_dict.get("size", 10),
        )

        # Parse ray config
        ray_dict = orch_dict.get("ray", {})
        ray_config = RayConfig(
            local=ray_dict.get("local", True),
            num_cpus=ray_dict.get("num_cpus"),
            num_gpus=ray_dict.get("num_gpus"),
            memory_per_worker_gb=ray_dict.get("memory_per_worker_gb"),
            object_store_memory_gb=ray_dict.get("object_store_memory_gb"),
            cluster_address=ray_dict.get("cluster_address"),
        )

        # Parse retry config
        retry_dict = orch_dict.get("retry", {})
        retry_config = RetryConfig(
            max_attempts=retry_dict.get("max_attempts", 3),
            initial_delay_seconds=retry_dict.get("initial_delay_seconds", 3.0),
            strategy=retry_dict.get("strategy", "exponential"),
            max_delay_seconds=retry_dict.get("max_delay_seconds", 60.0),
        )

        # Parse circuit breaker config
        cb_dict = orch_dict.get("circuit_breaker", {})
        circuit_breaker_config = CircuitBreakerConfig(
            enabled=cb_dict.get("enabled", True),
            failure_threshold=cb_dict.get("failure_threshold", 5),
            recovery_timeout_seconds=cb_dict.get("recovery_timeout_seconds", 60.0),
        )

        # Parse progress config
        progress_dict = orch_dict.get("progress", {})
        progress_config = ProgressConfig(
            reports_dir=progress_dict.get("reports_dir", "./reports"),
            realtime_updates=progress_dict.get("realtime_updates", True),
            file_name=progress_dict.get("file_name", "project_progress.md"),
        )

        # Parse output config
        output_dict = orch_dict.get("output", {})
        output_config = OutputConfig(
            mirror_structure=output_dict.get("mirror_structure", True),
            docs_dir=output_dict.get("docs_dir", "./docs"),
        )

        # Parse summary config
        summary_dict = orch_dict.get("summary", {})
        summary_config = SummaryConfig(
            enabled=summary_dict.get("enabled", True),
            file_name=summary_dict.get("file_name", "PROJECT_SUMMARY.md"),
            include_dependency_graph=summary_dict.get("include_dependency_graph", True),
            include_business_logic=summary_dict.get("include_business_logic", True),
        )

        # Parse tree server config
        default_extensions = [".cbl", ".CBL", ".cob", ".COB", ".cpy", ".CPY", ".c74", ".C74"]
        default_exclude_dirs = [".git", "node_modules", "__pycache__", ".venv"]

        # docker_image is required - no default
        tree_docker_image = tree_dict.get("docker_image")
        if not tree_docker_image:
            raise ValueError("tree_server.docker_image is required in config.yaml - no default value")

        tree_config = TreeServerConfig(
            docker_image=tree_docker_image,
            tool=tree_dict.get("tool", "tree_json_output"),
            max_depth=tree_dict.get("max_depth"),
            extensions=tree_dict.get("extensions", default_extensions),
            exclude_dirs=tree_dict.get("exclude_dirs", default_exclude_dirs),
        )

        return cls(
            enabled=orch_dict.get("enabled", False),
            batch=batch_config,
            ray=ray_config,
            retry=retry_config,
            circuit_breaker=circuit_breaker_config,
            progress=progress_config,
            output=output_config,
            summary=summary_config,
            tree_server=tree_config,
            metadata_dir=config_dict.get("output", {}).get("metadata_dir", "./metadata"),
        )


def load_orchestrator_config(config_path: str) -> OrchestratorConfig:
    """
    Load and validate orchestrator configuration from YAML file.

    Args:
        config_path: Path to YAML configuration file

    Returns:
        Validated OrchestratorConfig instance

    Raises:
        FileNotFoundError: If config file doesn't exist
        ValueError: If configuration validation fails
    """
    import yaml

    config_path = Path(config_path)
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path, "r") as f:
        config_dict = yaml.safe_load(f)

    # Create config from dict
    config = OrchestratorConfig.from_dict(config_dict)

    # Validate
    errors = config.validate()
    if errors:
        error_msg = "Configuration validation failed:\n" + "\n".join(f"  - {e}" for e in errors)
        raise ValueError(error_msg)

    logger.info(f"Loaded orchestrator configuration from {config_path}")
    return config


def get_default_config(tree_server_docker_image: str) -> OrchestratorConfig:
    """
    Get default orchestrator configuration with required tree_server.docker_image.

    Args:
        tree_server_docker_image: Docker image for tree server (required)

    Returns:
        OrchestratorConfig with default values and provided tree_server config
    """
    return OrchestratorConfig(
        tree_server=TreeServerConfig(docker_image=tree_server_docker_image)
    )


# Export all config classes
__all__ = [
    "OrchestratorConfig",
    "BatchConfig",
    "RayConfig",
    "RetryConfig",
    "CircuitBreakerConfig",
    "ProgressConfig",
    "OutputConfig",
    "SummaryConfig",
    "TreeServerConfig",
    "load_orchestrator_config",
    "get_default_config",
]
