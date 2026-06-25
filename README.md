# Lume

Lume is a unified observability and telemetry bootstrapper for Python. It provides structured, environment-agnostic logging alongside native vendor facades for Sentry, PostHog, Langfuse, and OpenTelemetry. Built on top of `structlog`, `rich`, and `opentelemetry`, Lume allows you to configure your entire observability stack with a single function call while maintaining direct access to underlying native SDKs.

## Features

- **Unified Bootstrapper**: One call to `setup_logging()` configures your entire telemetry stack (Logging, Sentry, PostHog, Langfuse, and OpenTelemetry) based on the presence of environment variables.
- **Submodule Vendor Re-export**: Access Sentry, PostHog, and Langfuse natively directly through `lume` (e.g., `from lume import sentry_sdk`). This preserves original typings and API surfaces while keeping dependency versions centralized in this package.
- **Structured Logging**: Powered by `structlog` for consistent, machine-readable logs.
- **Decoupled Transports**: 
  - **Terminal Transport (stdout)**: Always active, beautifully formatted with `rich`.
  - **Bifurcated OpenTelemetry (Network)**: OTLP exporters spin up *strictly* when running inside Windmill (detected via `WM_TOKEN` and `WM_WORKSPACE`), ensuring no idle exporters in local/dev environments.
- **Context Injection**: Automatically injects `trace_id` and `span_id` from OpenTelemetry into log records.
- **Configuration via Env Vars**: Easy configuration using `pydantic-settings`.

## Installation

You can install this package directly from the GitHub repository using `pip`:

```bash
pip install git+https://github.com/aurumorinc/python-logging.git
```

*(Note: While the repository is `python-logging`, the importable package is `lume`)*

## Configuration

Configuration is handled via environment variables (or a `.env` file) using `pydantic-settings`.

| Environment Variable | Default | Description |
| :--- | :--- | :--- |
| `LOG_LEVEL` | `INFO` | The logging level (e.g., `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`). |
| `SENTRY_DSN` | `None` | The DSN for Sentry. If provided, Sentry will be automatically initialized. |
| `POSTHOG_API_KEY` | `None` | Project API Key for PostHog. If provided, PostHog will be automatically configured. |
| `POSTHOG_HOST` | `https://us.i.posthog.com` | Host URL for PostHog. |
| `LANGFUSE_PUBLIC_KEY` | `None` | Public Key for Langfuse. |
| `LANGFUSE_SECRET_KEY` | `None` | Secret Key for Langfuse. If both keys are provided, Langfuse is initialized. |
| `LANGFUSE_HOST` | `https://cloud.langfuse.com` | Host URL for Langfuse. |
| `WM_TOKEN` | `None` | Windmill Workspace Token. Required for Windmill OTEL. |
| `WM_WORKSPACE` | `None` | Windmill Workspace Name. Required for Windmill OTEL. |
| `WM_BASE_URL` | `None` | Base URL for Windmill, used for resolving OTEL endpoints. |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `None` | Fallback OTLP endpoint for exporting traces. |
| `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT`| `None` | Fallback specific OTLP endpoint for exporting logs. |

## Usage

**CRITICAL RULE:** You must call `setup_logging()` **exactly once** at the very entry point of your application (e.g., in your `main.py`, `app.py`, or CLI entry script). Because it configures the global logging and observability state, you do *not* need to call it in every file.

### Integrating with Project Settings (Pydantic)

If your project already uses `pydantic-settings`, you can easily merge the telemetry configuration into your main settings class by inheriting from `LoggingSettings`. This allows you to validate all environment variables (both app-specific and logging-specific) in one place.

```python
from pydantic_settings import BaseSettings
from lume.config import LoggingSettings
from lume.logging import setup_logging

# Inherit from LoggingSettings to include logging configuration
class AppSettings(LoggingSettings, BaseSettings):
    app_name: str = "my-awesome-app"
    database_url: str

# Instantiate your combined settings
settings = AppSettings()

# Pass the combined settings to setup_logging
setup_logging(settings)
```

### Basic Logging Usage

**In your entry point file (e.g., `main.py`):**
```python
from lume.logging import setup_logging

# 1. Initialize global logging and telemetry state (call exactly once)
setup_logging()
```

**In any other file in your project:**
```python
from lume.logging import get_logger

# 2. Get a logger instance for this module
logger = get_logger(__name__)

# 3. Log messages with structured data
logger.info("user_logged_in", user_id=123, ip_address="192.168.1.1")

try:
    1 / 0
except ZeroDivisionError:
    logger.exception("calculation_failed", operation="division")
```

### Context Variables

You can bind context variables to a logger so they are included in all subsequent log calls from that logger.

```python
from lume.logging import get_logger

logger = get_logger(__name__).bind(request_id="req-abc-123")

logger.info("processing_request") 
# Includes: request_id="req-abc-123"

logger.info("request_completed", status=200) 
# Includes: request_id="req-abc-123", status=200
```

### Vendor Facades

`lume` exports Sentry, PostHog, and Langfuse directly. You do not need to install these dependencies manually in your consumer application; they are natively managed and exposed by `lume`.

```python
from lume import sentry_sdk, posthog, langfuse, observe

# Sentry
sentry_sdk.capture_message("Something went wrong")

# PostHog
posthog.capture("user_123", "event_name", properties={"key": "value"})

# Langfuse (via decorator)
@observe(as_type="generation")
def my_llm_call(prompt):
    return "LLM Response"
```

### OpenTelemetry & Windmill Integration

If you configure `WM_TOKEN` and `WM_WORKSPACE`, logs and traces will automatically be exported to the Windmill platform.

`lume` will also automatically extract the active `trace_id` and `span_id` and inject them into your log records. When running inside Windmill, it automatically extracts tracing contexts from the environment.

## Terminal Output

Lume uses `rich.logging.RichHandler` for beautiful, structured formatting in the terminal.

**Configuration:**
```bash
export LOG_LEVEL=INFO
```

**Code:**
```python
logger.info("Starting data synchronization...")
logger.warning("Rate limit approaching", current=95, max=100)
```

**Output Example:**
```text
[14:38:01] INFO     Starting data synchronization...
           WARNING  Rate limit approaching                             current=95 max=100
```
*(Note: The actual output will be beautifully formatted and colorized by `rich`, with aligned timestamps, levels, and structured key-value pairs)*

## Development

To set up the project for development:

1. Ensure you have Python 3.11+ installed.
2. Install dependencies (using `pdm`):
   ```bash
   pdm install
   ```
3. Run tests:
   ```bash
   pdm run pytest
   ```

## Release Process

This project uses [Release Please](https://github.com/googleapis/release-please) to automate versioning and changelog generation.

To trigger a release:
1. Merge your changes into the `main` branch using [Conventional Commits](https://www.conventionalcommits.org/) (e.g., `feat: add new feature`, `fix: resolve bug`).
2. Release Please will automatically create or update a Release PR.
3. When you are ready to release, merge the Release PR. This will tag the release and update the changelog.
