# src/python_logging/config.py
from typing import Literal, Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggingSettings(BaseSettings):
    """Configuration for the python-logging package."""

    log_level: str = "INFO"
    environment: Literal["dev", "prod", "cli"] = "dev"
    otel_exporter_otlp_endpoint: Optional[str] = None
    otel_exporter_otlp_logs_endpoint: Optional[str] = None
    traceparent: Optional[str] = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

settings = LoggingSettings()

