# src/python_logging/main.py
import logging
from typing import Optional

import structlog
from opentelemetry.sdk._logs import LoggingHandler

from python_logging.config import settings
from python_logging.environments import get_cli_config, get_dev_config, get_prod_config
from python_logging.integrations.otel import add_otel_context, setup_otel_provider

# Export get_logger for use throughout the application
get_logger = structlog.get_logger


def setup_logging() -> None:
    """
    Configures structlog and routes standard logging through it based on the environment.
    Uses the global settings object from python_logging.config.
    """
    # Determine log level
    log_level_name = settings.log_level.upper()
    log_level = getattr(logging, log_level_name, logging.INFO)

    # Shared processors for all environments
    shared_processors = [
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        add_otel_context,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
    ]

    # Get environment-specific processors and handlers
    if settings.environment == "prod":
        env_processors, handlers = get_prod_config()
    elif settings.environment == "cli":
        env_processors, handlers = get_cli_config()
    else:
        env_processors, handlers = get_dev_config()

    # Configure structlog
    if settings.environment == "cli":
        structlog_processors = shared_processors + env_processors
    else:
        structlog_processors = shared_processors + [structlog.stdlib.ProcessorFormatter.wrap_for_formatter]

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

    # Add environment-specific handlers
    for handler in handlers:
        # For non-CLI environments, we need to wrap the handler with structlog's formatter
        if settings.environment != "cli":
            formatter = structlog.stdlib.ProcessorFormatter(
                processor=env_processors[0],
                foreign_pre_chain=shared_processors,
            )
            handler.setFormatter(formatter)
        
        root_logger.addHandler(handler)

    # Setup OpenTelemetry OTLP handler if configured
    logger_provider = setup_otel_provider()
    if logger_provider:
        otlp_handler = LoggingHandler(level=log_level, logger_provider=logger_provider)
        root_logger.addHandler(otlp_handler)
