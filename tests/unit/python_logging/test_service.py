import logging
from unittest import mock


from python_logging.service import (
    add_otel_context,
    remove_otel_context,
    setup_otel_provider,
)


def test_add_otel_context_with_active_span():
    from opentelemetry.sdk.trace import TracerProvider

    provider = TracerProvider()
    tracer = provider.get_tracer(__name__)

    with tracer.start_as_current_span("test_span") as span:
        # We need to set the current span in the context manually for the test
        # or use the tracer properly. start_as_current_span does this.
        ctx = span.get_span_context()
        event_dict = {}

        # Mock trace.get_current_span to return our span since the global provider isn't set
        with mock.patch(
            "python_logging.service.trace.get_current_span", return_value=span
        ):
            result = add_otel_context(logging.getLogger(), "info", event_dict)

            assert result["trace_id"] == format(ctx.trace_id, "032x")
            assert result["span_id"] == format(ctx.span_id, "016x")


@mock.patch("python_logging.service.settings")
def test_add_otel_context_fallback_to_settings(mock_settings):
    mock_settings.trace_id = "settings_trace"
    mock_settings.span_id = "settings_span"

    event_dict = {}
    result = add_otel_context(logging.getLogger(), "info", event_dict)

    assert result["trace_id"] == "settings_trace"
    assert result["span_id"] == "settings_span"


@mock.patch("python_logging.service.settings")
def test_setup_otel_provider_no_endpoint(mock_settings):
    mock_settings.otel_exporter_otlp_endpoint = None
    mock_settings.otel_exporter_otlp_logs_endpoint = None
    provider = setup_otel_provider()
    assert provider is None


@mock.patch("python_logging.service.settings")
def test_setup_otel_provider_with_endpoint(mock_settings):
    mock_settings.otel_exporter_otlp_endpoint = "http://localhost:4317"
    mock_settings.otel_exporter_otlp_logs_endpoint = None
    provider = setup_otel_provider()
    assert provider is not None


def test_remove_otel_context():
    event_dict = {
        "event": "test message",
        "trace_id": "test_trace_id",
        "span_id": "test_span_id",
        "other_key": "value",
    }
    
    result = remove_otel_context(logging.getLogger(), "info", event_dict)
    
    # Verify the keys were removed in the result
    assert "trace_id" not in result
    assert "span_id" not in result
    assert result["event"] == "test message"
    assert result["other_key"] == "value"
    
    # Verify the original dictionary was NOT mutated
    assert "trace_id" in event_dict
    assert "span_id" in event_dict

