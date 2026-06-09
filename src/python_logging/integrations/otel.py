# src/python_logging/integrations/otel.py
import logging
from typing import Any, Dict, Optional

from opentelemetry import trace
from opentelemetry._logs import set_logger_provider
from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter
from opentelemetry.sdk._logs import LoggerProvider
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor

from python_logging.config import settings
from python_logging.integrations.windmill import get_windmill_context


def add_otel_context(
    logger: logging.Logger, method_name: str, event_dict: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Injects OpenTelemetry trace_id and span_id into the log record.
    Falls back to Windmill context if no active OTel span is found.
    """
    # 1. Try to get it from the active OTel span
    span = trace.get_current_span()
    if span and span.get_span_context().is_valid:
        ctx = span.get_span_context()
        event_dict["trace_id"] = format(ctx.trace_id, "032x")
        event_dict["span_id"] = format(ctx.span_id, "016x")
    else:
        # 2. Fallback to the context stored in Windmill TRACEPARENT
        windmill_ctx = get_windmill_context()
        if "trace_id" in windmill_ctx:
            event_dict["trace_id"] = windmill_ctx["trace_id"]
        if "span_id" in windmill_ctx:
            event_dict["span_id"] = windmill_ctx["span_id"]

    return event_dict


def setup_otel_provider() -> Optional[LoggerProvider]:
    """
    Initializes the OpenTelemetry LoggerProvider with an OTLP exporter if configured.
    """
    if not (settings.otel_exporter_otlp_endpoint or settings.otel_exporter_otlp_logs_endpoint):
        return None

    logger_provider = LoggerProvider()
    exporter = OTLPLogExporter()
    logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))
    
    set_logger_provider(logger_provider)
    return logger_provider

