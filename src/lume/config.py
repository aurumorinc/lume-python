# src/lume/config.py
import secrets
from typing import Optional

from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


def generate_traceparent() -> str:
    """Generates a valid W3C traceparent string."""
    trace_id = secrets.token_hex(16)
    span_id = secrets.token_hex(8)
    return f"00-{trace_id}-{span_id}-01"


def resolve_traceparent() -> str:
    """
    Resolves the traceparent according to precedence:
    1. Windmill environment variable (WM_TRACEPARENT)
    2. Generated fallback
    """
    from lume.integrations.windmill import get_windmill_traceparent

    wm_tp = get_windmill_traceparent()
    if wm_tp:
        return wm_tp
    return generate_traceparent()


class LoggingSettings(BaseSettings):
    """Configuration for the lume package."""

    log_level: str = "INFO"
    otel_exporter_otlp_endpoint: Optional[str] = None
    otel_exporter_otlp_logs_endpoint: Optional[str] = None
    traceparent: str = Field(default_factory=resolve_traceparent)

    sentry_dsn: Optional[str] = None

    posthog_api_key: Optional[str] = None
    posthog_host: str = "https://us.i.posthog.com"

    langfuse_public_key: Optional[str] = None
    langfuse_secret_key: Optional[str] = None
    langfuse_host: str = "https://cloud.langfuse.com"

    wm_token: Optional[str] = None
    wm_workspace: Optional[str] = None
    wm_base_url: Optional[str] = None

    @computed_field  # type: ignore
    @property
    def is_windmill_env(self) -> bool:
        return bool(self.wm_token and self.wm_workspace)

    @computed_field  # type: ignore
    @property
    def trace_id(self) -> str:
        """Extracts the trace_id from the traceparent."""
        return self.traceparent.split("-")[1]

    @computed_field  # type: ignore
    @property
    def span_id(self) -> str:
        """Extracts the span_id from the traceparent."""
        return self.traceparent.split("-")[2]

    model_config = SettingsConfigDict()


settings = LoggingSettings()
