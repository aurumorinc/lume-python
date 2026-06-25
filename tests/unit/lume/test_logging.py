# tests/unit/lume/test_logging.py
import logging
from io import StringIO
from unittest import mock


from lume.config import LoggingSettings
from lume.logging import get_logger, setup_logging


@mock.patch("lume.logging.structlog.configure", spec=True)
@mock.patch("lume.logging.setup_otel_provider", spec=True)
def test_setup_logging(mock_setup_otel, mock_configure):
    """Test setup_logging attaches the expected RichHandler."""
    # Arrange
    mock_setup_otel.return_value = None
    settings = LoggingSettings()

    # Act
    setup_logging(settings)

    # Assert
    mock_configure.assert_called_once()
    from rich.logging import RichHandler

    root_logger = logging.getLogger()
    assert len(root_logger.handlers) == 1
    assert isinstance(root_logger.handlers[0], RichHandler)


@mock.patch("lume.logging.structlog.configure", spec=True)
@mock.patch("lume.logging.setup_otel_provider", spec=True)
def test_setup_logging_with_otel(mock_setup_otel, mock_configure):
    """Test setup_logging adds OTLP handler when provider is available."""
    # Arrange
    mock_provider = mock.Mock()
    mock_setup_otel.return_value = mock_provider
    settings = LoggingSettings()

    # Act
    setup_logging(settings)

    # Assert
    from opentelemetry.sdk._logs import LoggingHandler

    root_logger = logging.getLogger()
    assert len(root_logger.handlers) == 2

    from rich.logging import RichHandler

    handler_types = [type(h) for h in root_logger.handlers]
    assert RichHandler in handler_types
    assert LoggingHandler in handler_types


@mock.patch("lume.logging.structlog.configure", spec=True)
@mock.patch("lume.logging.setup_otel_provider", spec=True)
@mock.patch("lume.integrations.sentry.sentry_sdk", create=True)
@mock.patch("lume.integrations.posthog.posthog", create=True)
@mock.patch("lume.integrations.langfuse.langfuse.Langfuse", create=True)
def test_setup_logging_initializes_vendors(
    mock_langfuse, mock_posthog, mock_sentry, mock_setup_otel, mock_configure
):
    """Test setup_logging correctly passes config to integration SDKs."""
    # Arrange
    mock_setup_otel.return_value = None
    settings = LoggingSettings(
        sentry_dsn="https://sentry",
        posthog_api_key="ph_key",
        langfuse_public_key="lf_pub",
        langfuse_secret_key="lf_sec",
    )

    # Act
    setup_logging(settings)

    # Assert
    mock_sentry.init.assert_called_once_with(dsn="https://sentry")
    assert mock_posthog.project_api_key == "ph_key"
    mock_langfuse.assert_called_once_with(
        public_key="lf_pub",
        secret_key="lf_sec",
        host="https://cloud.langfuse.com",
    )


@mock.patch("lume.logging.structlog.configure", spec=True)
@mock.patch("lume.logging.setup_otel_provider", spec=True)
@mock.patch("lume.integrations.sentry.sentry_sdk", create=True)
@mock.patch("lume.integrations.posthog.posthog", create=True)
@mock.patch("lume.integrations.langfuse.langfuse.Langfuse", create=True)
def test_setup_logging_zero_config(
    mock_langfuse, mock_posthog, mock_sentry, mock_setup_otel, mock_configure
):
    """Test setup_logging safely bypasses missing SDK configurations."""
    # Arrange
    mock_setup_otel.return_value = None
    settings = LoggingSettings()

    # Act
    setup_logging(settings)

    # Assert
    mock_sentry.init.assert_not_called()
    mock_langfuse.assert_not_called()


def test_console_output_is_clean():
    """
    Integration test to verify that the terminal output does NOT
    contain trace_id, span_id, _record, or _from_structlog keys.
    """
    # Arrange
    from rich.console import Console

    out = StringIO()
    settings = LoggingSettings()

    setup_logging(settings)
    root_logger = logging.getLogger()
    for handler in root_logger.handlers:
        from rich.logging import RichHandler

        if isinstance(handler, RichHandler):
            handler.console = Console(file=out, color_system=None)

    # Act
    logger = get_logger("test_clean")
    logger.info("This is a clean log message")

    # Assert
    output_str = out.getvalue()
    assert "_record" not in output_str
    assert "_from_structlog" not in output_str
    assert "trace_id" not in output_str
    assert "span_id" not in output_str
    assert "This is a clean log message" in output_str


def test_setup_logging_idempotency():
    """Verify that multiple calls to setup_logging do not exponentially multiply handlers."""
    # Arrange
    settings = LoggingSettings()

    # Act
    setup_logging(settings)
    handler_count_pass_one = len(logging.getLogger().handlers)

    setup_logging(settings)
    handler_count_pass_two = len(logging.getLogger().handlers)

    # Assert
    assert handler_count_pass_one > 0
    assert handler_count_pass_one == handler_count_pass_two
