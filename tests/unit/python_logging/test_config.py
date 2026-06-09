import os
from unittest import mock

from python_logging.config import LoggingSettings


def test_logging_settings_defaults():
    settings = LoggingSettings()
    assert settings.log_level == "INFO"
    assert settings.environment == "dev"
    assert settings.otel_exporter_otlp_endpoint is None
    assert settings.otel_exporter_otlp_logs_endpoint is None


@mock.patch.dict(os.environ, {"LOG_LEVEL": "DEBUG", "ENVIRONMENT": "prod", "OTEL_EXPORTER_OTLP_ENDPOINT": "http://localhost:4317"})
def test_logging_settings_from_env():
    settings = LoggingSettings()
    assert settings.log_level == "DEBUG"
    assert settings.environment == "prod"
    assert settings.otel_exporter_otlp_endpoint == "http://localhost:4317"
