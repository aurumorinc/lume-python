from unittest import mock

from python_logging.integrations.windmill import get_windmill_context


@mock.patch("python_logging.integrations.windmill.settings")
def test_get_windmill_context_valid(mock_settings):
    mock_settings.traceparent = "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01"
    context = get_windmill_context()
    assert context == {
        "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
        "span_id": "00f067aa0ba902b7",
    }


@mock.patch("python_logging.integrations.windmill.settings")
def test_get_windmill_context_missing(mock_settings):
    mock_settings.traceparent = None
    context = get_windmill_context()
    assert context == {}


@mock.patch("python_logging.integrations.windmill.settings")
def test_get_windmill_context_invalid(mock_settings):
    mock_settings.traceparent = "invalid-format"
    context = get_windmill_context()
    assert context == {}
