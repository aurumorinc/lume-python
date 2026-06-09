import logging
from unittest import mock

from python_logging.main import setup_logging


@mock.patch("python_logging.main.settings")
@mock.patch("python_logging.main.structlog.configure")
def test_setup_logging_dev(mock_configure, mock_settings):
    mock_settings.environment = "dev"
    mock_settings.log_level = "INFO"
    mock_settings.otel_exporter_otlp_endpoint = None
    mock_settings.otel_exporter_otlp_logs_endpoint = None
    setup_logging()
    
    mock_configure.assert_called_once()
    root_logger = logging.getLogger()
    assert len(root_logger.handlers) >= 1
    assert isinstance(root_logger.handlers[0], logging.StreamHandler)


@mock.patch("python_logging.main.settings")
@mock.patch("python_logging.main.structlog.configure")
def test_setup_logging_prod(mock_configure, mock_settings):
    mock_settings.environment = "prod"
    mock_settings.log_level = "INFO"
    mock_settings.otel_exporter_otlp_endpoint = None
    mock_settings.otel_exporter_otlp_logs_endpoint = None
    setup_logging()
    
    mock_configure.assert_called_once()
    root_logger = logging.getLogger()
    assert len(root_logger.handlers) >= 1
    assert isinstance(root_logger.handlers[0], logging.StreamHandler)


@mock.patch("python_logging.main.settings")
@mock.patch("python_logging.main.structlog.configure")
def test_setup_logging_cli(mock_configure, mock_settings):
    mock_settings.environment = "cli"
    mock_settings.log_level = "INFO"
    mock_settings.otel_exporter_otlp_endpoint = None
    mock_settings.otel_exporter_otlp_logs_endpoint = None
    setup_logging()
    
    mock_configure.assert_called_once()
    root_logger = logging.getLogger()
    assert len(root_logger.handlers) >= 1
    # The handler should be a RichHandler
    from rich.logging import RichHandler
    assert isinstance(root_logger.handlers[0], RichHandler)
