"""
Unit tests for Orchestrator Configuration Validator

Tests cover:
- Default configuration values
- Configuration validation
- Loading from YAML dict
- Error handling for invalid configurations
- Retry delay calculations
"""

import pytest
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from orchestrator_config import (
    OrchestratorConfig,
    BatchConfig,
    RayConfig,
    RetryConfig,
    CircuitBreakerConfig,
    ProgressConfig,
    OutputConfig,
    SummaryConfig,
    TreeServerConfig,
    get_default_config,
)


class TestBatchConfig:
    """Tests for BatchConfig."""

    def test_default_values(self):
        """Test default batch configuration values."""
        config = BatchConfig()
        assert config.mode == "batch"
        assert config.size == 10

    def test_valid_batch_mode(self):
        """Test valid batch mode values."""
        config = BatchConfig(mode="batch")
        assert config.validate() == []

        config = BatchConfig(mode="all")
        assert config.validate() == []

    def test_invalid_batch_mode(self):
        """Test invalid batch mode raises validation error."""
        config = BatchConfig(mode="invalid")
        errors = config.validate()
        assert len(errors) == 1
        assert "Invalid batch.mode" in errors[0]

    def test_invalid_batch_size(self):
        """Test invalid batch size raises validation error."""
        config = BatchConfig(size=0)
        errors = config.validate()
        assert len(errors) == 1
        assert "Invalid batch.size" in errors[0]

        config = BatchConfig(size=-1)
        errors = config.validate()
        assert len(errors) == 1


class TestRayConfig:
    """Tests for RayConfig."""

    def test_default_values(self):
        """Test default Ray configuration values."""
        config = RayConfig()
        assert config.local is True
        assert config.num_cpus is None
        assert config.num_gpus is None
        assert config.cluster_address is None

    def test_local_mode_no_address_required(self):
        """Test local mode doesn't require cluster address."""
        config = RayConfig(local=True)
        assert config.validate() == []

    def test_remote_mode_requires_address(self):
        """Test remote mode requires cluster address."""
        config = RayConfig(local=False, cluster_address=None)
        errors = config.validate()
        assert len(errors) == 1
        assert "cluster_address is required" in errors[0]

    def test_remote_mode_with_address(self):
        """Test remote mode with cluster address is valid."""
        config = RayConfig(local=False, cluster_address="ray://head:10001")
        assert config.validate() == []

    def test_invalid_num_cpus(self):
        """Test invalid num_cpus raises validation error."""
        config = RayConfig(num_cpus=0)
        errors = config.validate()
        assert len(errors) == 1
        assert "Invalid ray.num_cpus" in errors[0]

    def test_invalid_memory(self):
        """Test invalid memory raises validation error."""
        config = RayConfig(memory_per_worker_gb=0.1)
        errors = config.validate()
        assert len(errors) == 1
        assert "Invalid ray.memory_per_worker_gb" in errors[0]


class TestRetryConfig:
    """Tests for RetryConfig."""

    def test_default_values(self):
        """Test default retry configuration values."""
        config = RetryConfig()
        assert config.max_attempts == 3
        assert config.initial_delay_seconds == 3.0
        assert config.strategy == "exponential"
        assert config.max_delay_seconds == 60.0

    def test_valid_strategies(self):
        """Test valid retry strategies."""
        config = RetryConfig(strategy="exponential")
        assert config.validate() == []

        config = RetryConfig(strategy="fixed")
        assert config.validate() == []

    def test_invalid_strategy(self):
        """Test invalid strategy raises validation error."""
        config = RetryConfig(strategy="invalid")
        errors = config.validate()
        assert len(errors) == 1
        assert "Invalid retry.strategy" in errors[0]

    def test_invalid_max_attempts(self):
        """Test invalid max_attempts raises validation error."""
        config = RetryConfig(max_attempts=0)
        errors = config.validate()
        assert len(errors) == 1
        assert "Invalid retry.max_attempts" in errors[0]

    def test_max_delay_less_than_initial(self):
        """Test max_delay < initial_delay raises validation error."""
        config = RetryConfig(initial_delay_seconds=10, max_delay_seconds=5)
        errors = config.validate()
        assert len(errors) == 1
        assert "max_delay_seconds must be >=" in errors[0]

    def test_calculate_delay_fixed(self):
        """Test fixed delay calculation."""
        config = RetryConfig(strategy="fixed", initial_delay_seconds=3)
        assert config.calculate_delay(0) == 3
        assert config.calculate_delay(1) == 3
        assert config.calculate_delay(5) == 3

    def test_calculate_delay_exponential(self):
        """Test exponential delay calculation."""
        config = RetryConfig(
            strategy="exponential",
            initial_delay_seconds=3,
            max_delay_seconds=60
        )
        assert config.calculate_delay(0) == 3    # 3 * 2^0 = 3
        assert config.calculate_delay(1) == 6    # 3 * 2^1 = 6
        assert config.calculate_delay(2) == 12   # 3 * 2^2 = 12
        assert config.calculate_delay(3) == 24   # 3 * 2^3 = 24
        assert config.calculate_delay(4) == 48   # 3 * 2^4 = 48
        assert config.calculate_delay(5) == 60   # 3 * 2^5 = 96, capped at 60


class TestCircuitBreakerConfig:
    """Tests for CircuitBreakerConfig."""

    def test_default_values(self):
        """Test default circuit breaker configuration values."""
        config = CircuitBreakerConfig()
        assert config.enabled is True
        assert config.failure_threshold == 5
        assert config.recovery_timeout_seconds == 60.0

    def test_valid_config(self):
        """Test valid circuit breaker config passes validation."""
        config = CircuitBreakerConfig(failure_threshold=3, recovery_timeout_seconds=30)
        assert config.validate() == []

    def test_invalid_failure_threshold(self):
        """Test invalid failure_threshold raises validation error."""
        config = CircuitBreakerConfig(failure_threshold=0)
        errors = config.validate()
        assert len(errors) == 1
        assert "Invalid circuit_breaker.failure_threshold" in errors[0]


class TestProgressConfig:
    """Tests for ProgressConfig."""

    def test_default_values(self):
        """Test default progress configuration values."""
        config = ProgressConfig()
        assert config.reports_dir == "./reports"
        assert config.realtime_updates is True
        assert config.file_name == "project_progress.md"

    def test_progress_file_path(self):
        """Test progress file path property."""
        config = ProgressConfig(reports_dir="./my_reports", file_name="progress.md")
        assert config.progress_file_path == Path("./my_reports/progress.md")

    def test_empty_file_name(self):
        """Test empty file_name raises validation error."""
        config = ProgressConfig(file_name="")
        errors = config.validate()
        assert len(errors) == 1
        assert "file_name cannot be empty" in errors[0]


class TestTreeServerConfig:
    """Tests for TreeServerConfig."""

    def test_requires_docker_image(self):
        """Test that docker_image is required."""
        import pytest
        with pytest.raises(TypeError):
            # docker_image is required, no default
            TreeServerConfig()

    def test_with_docker_image(self):
        """Test tree server configuration with docker_image."""
        config = TreeServerConfig(docker_image="tree-mcp:test")
        assert config.docker_image == "tree-mcp:test"
        assert config.tool == "tree_json_output"
        assert ".cbl" in config.extensions
        assert ".git" in config.exclude_dirs

    def test_empty_docker_image_validation(self):
        """Test that empty docker_image fails validation."""
        config = TreeServerConfig(docker_image="")
        errors = config.validate()
        assert any("docker_image" in e for e in errors)

    def test_valid_tools(self):
        """Test valid tree server tools."""
        for tool in ["tree_basic", "tree_json_output", "tree_xml_output"]:
            config = TreeServerConfig(docker_image="tree-mcp:test", tool=tool)
            assert config.validate() == []

    def test_invalid_tool(self):
        """Test invalid tool raises validation error."""
        config = TreeServerConfig(docker_image="tree-mcp:test", tool="invalid_tool")
        errors = config.validate()
        assert len(errors) == 1
        assert "Invalid tree_server.tool" in errors[0]

    def test_invalid_max_depth(self):
        """Test invalid max_depth raises validation error."""
        config = TreeServerConfig(docker_image="tree-mcp:test", max_depth=0)
        errors = config.validate()
        assert len(errors) == 1
        assert "Invalid tree_server.max_depth" in errors[0]


class TestOrchestratorConfig:
    """Tests for main OrchestratorConfig."""

    def test_default_config(self):
        """Test get_default_config returns valid defaults with required docker_image."""
        config = get_default_config(tree_server_docker_image="tree-mcp:test")
        assert config.enabled is False
        assert config.batch.mode == "batch"
        assert config.ray.local is True
        assert config.retry.max_attempts == 3
        assert config.tree_server.docker_image == "tree-mcp:test"
        errors = config.validate()
        assert errors == []

    def test_config_without_tree_server_fails_validation(self):
        """Test that config without tree_server fails validation."""
        config = OrchestratorConfig()
        errors = config.validate()
        assert any("tree_server" in e for e in errors)

    def test_from_dict_requires_tree_server_docker_image(self):
        """Test creating config from dict requires tree_server.docker_image."""
        import pytest
        config_dict = {
            "orchestrator": {
                "enabled": True
            }
        }
        with pytest.raises(ValueError, match="tree_server.docker_image is required"):
            OrchestratorConfig.from_dict(config_dict)

    def test_from_dict_minimal(self):
        """Test creating config from minimal dict with tree_server."""
        config_dict = {
            "orchestrator": {
                "enabled": True
            },
            "tree_server": {
                "docker_image": "tree-mcp:test"
            }
        }
        config = OrchestratorConfig.from_dict(config_dict)
        assert config.enabled is True
        # All other values should be defaults
        assert config.batch.mode == "batch"
        assert config.ray.local is True

    def test_from_dict_full(self):
        """Test creating config from full dict."""
        config_dict = {
            "orchestrator": {
                "enabled": True,
                "batch": {
                    "mode": "all",
                    "size": 20
                },
                "ray": {
                    "local": False,
                    "cluster_address": "ray://head:10001",
                    "num_cpus": 8
                },
                "retry": {
                    "max_attempts": 5,
                    "initial_delay_seconds": 5,
                    "strategy": "fixed"
                },
                "circuit_breaker": {
                    "enabled": False,
                    "failure_threshold": 10
                },
                "progress": {
                    "reports_dir": "./custom_reports",
                    "file_name": "custom_progress.md"
                },
                "output": {
                    "mirror_structure": False,
                    "docs_dir": "./custom_docs"
                },
                "summary": {
                    "enabled": False
                }
            },
            "tree_server": {
                "docker_image": "tree-mcp:test",
                "tool": "tree_basic",
                "max_depth": 5
            }
        }
        config = OrchestratorConfig.from_dict(config_dict)

        assert config.enabled is True
        assert config.batch.mode == "all"
        assert config.batch.size == 20
        assert config.ray.local is False
        assert config.ray.cluster_address == "ray://head:10001"
        assert config.ray.num_cpus == 8
        assert config.retry.max_attempts == 5
        assert config.retry.strategy == "fixed"
        assert config.circuit_breaker.enabled is False
        assert config.progress.reports_dir == "./custom_reports"
        assert config.output.mirror_structure is False
        assert config.tree_server.docker_image == "tree-mcp:test"
        assert config.summary.enabled is False
        assert config.tree_server.tool == "tree_basic"
        assert config.tree_server.max_depth == 5

    def test_validate_aggregates_errors(self):
        """Test validation aggregates errors from all sub-configs."""
        config = OrchestratorConfig(
            batch=BatchConfig(mode="invalid", size=0),
            ray=RayConfig(local=False, cluster_address=None),
            retry=RetryConfig(strategy="invalid"),
        )
        errors = config.validate()
        # Should have multiple errors from different sub-configs
        assert len(errors) >= 4

    def test_ensure_directories(self, tmp_path):
        """Test ensure_directories creates required directories."""
        config = OrchestratorConfig(
            metadata_dir=str(tmp_path / "metadata"),
            progress=ProgressConfig(reports_dir=str(tmp_path / "reports")),
            output=OutputConfig(docs_dir=str(tmp_path / "docs"))
        )

        config.ensure_directories()

        assert (tmp_path / "metadata").exists()
        assert (tmp_path / "reports").exists()
        assert (tmp_path / "docs").exists()


class TestIntegration:
    """Integration tests for config loading."""

    def test_load_from_yaml_dict(self):
        """Test loading config that mirrors actual YAML structure."""
        # This mirrors the structure in config.example.yaml
        yaml_structure = {
            "orchestrator": {
                "enabled": True,
                "batch": {
                    "mode": "batch",
                    "size": 10
                },
                "ray": {
                    "local": True,
                    "num_cpus": None
                },
                "retry": {
                    "max_attempts": 3,
                    "initial_delay_seconds": 3,
                    "strategy": "exponential",
                    "max_delay_seconds": 60
                },
                "circuit_breaker": {
                    "enabled": True,
                    "failure_threshold": 5,
                    "recovery_timeout_seconds": 60
                },
                "progress": {
                    "reports_dir": "./reports",
                    "realtime_updates": True,
                    "file_name": "project_progress.md"
                },
                "output": {
                    "mirror_structure": True,
                    "docs_dir": "./docs"
                },
                "summary": {
                    "enabled": True,
                    "file_name": "PROJECT_SUMMARY.md",
                    "include_dependency_graph": True,
                    "include_business_logic": True
                }
            },
            "tree_server": {
                "docker_image": "tree-mcp:test",
                "tool": "tree_json_output",
                "max_depth": None,
                "extensions": [".cbl", ".CBL", ".cob", ".COB", ".cpy", ".CPY"],
                "exclude_dirs": [".git", "node_modules", "__pycache__"]
            },
            "output": {
                "metadata_dir": "./metadata"
            }
        }

        config = OrchestratorConfig.from_dict(yaml_structure)
        errors = config.validate()

        assert errors == [], f"Validation errors: {errors}"
        assert config.enabled is True
        assert config.batch.mode == "batch"
        assert config.batch.size == 10
        assert config.metadata_dir == "./metadata"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
