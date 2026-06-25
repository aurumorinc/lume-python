# src/lume/logging.py
import logging
from typing import Optional

import structlog
from opentelemetry.sdk._logs import LoggingHandler

from lume.config import (
    LoggingSettings,
    settings as default_settings,
)
from lume.service import (
    add_otel_context,
    get_console_format,
    setup_otel_provider,
)

# Export get_logger for use throughout the application
get_logger = structlog.get_logger


def setup_logging(settings: Optional[LoggingSettings] = None) -> None:
    """
    Configures structlog and routes standard logging through it.
    Also initializes Sentry, PostHog, Langfuse, and OpenTelemetry (if in Windmill).
    """
    if settings is None:
        settings = default_settings

    # 1. Sentry Setup
    if settings.sentry_dsn:
        from lume.integrations.sentry import sentry_sdk

        sentry_sdk.init(dsn=settings.sentry_dsn)

    # 2. PostHog Setup
    if settings.posthog_api_key:
        from lume.integrations.posthog import posthog

        posthog.project_api_key = settings.posthog_api_key
        posthog.host = settings.posthog_host

    # 3. Langfuse Setup
    if settings.langfuse_public_key:
        from lume.integrations.langfuse import langfuse

        langfuse.Langfuse(
            public_key=settings.langfuse_public_key,
            secret_key=settings.langfuse_secret_key,
            host=settings.langfuse_host,
        )

    # Determine log level
    log_level_name = settings.log_level.upper()
    log_level = getattr(logging, log_level_name, logging.INFO)

    # Shared processors
    from typing import List, Any

    shared_processors: List[Any] = [
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        add_otel_context,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
    ]

    format_processors, handlers = get_console_format()

    # Configure structlog
    structlog_processors = shared_processors + [
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter
    ]

    structlog.configure(
        processors=structlog_processors,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    # Configure standard logging handlers
    root_logger = logging.getLogger()
    root_logger.handlers.clear()
    root_logger.setLevel(log_level)

    # Add stdout transport handlers
    for handler in handlers:
        formatter = structlog.stdlib.ProcessorFormatter(
            processors=format_processors,
            foreign_pre_chain=shared_processors,
        )
        handler.setFormatter(formatter)
        root_logger.addHandler(handler)

    # 4. Windmill OTEL Logic
    logger_provider = setup_otel_provider(settings)
    if logger_provider:
        otlp_handler = LoggingHandler(level=log_level, logger_provider=logger_provider)
        root_logger.addHandler(otlp_handler)
