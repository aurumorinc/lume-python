# python-logging

Org-level Python logging package providing structured, environment-aware logging with OpenTelemetry and Windmill integrations. Built on top of `structlog`, `rich`, and `opentelemetry`.

## Features

- **Structured Logging**: Powered by `structlog` for consistent, machine-readable logs.
- **Environment-Aware**: Automatically adapts log output based on the environment (`dev`, `prod`, `cli`).
- **OpenTelemetry Integration**: Automatically injects `trace_id` and `span_id` into log records and supports exporting logs via OTLP.
- **Windmill Integration**: Extracts trace context from the `TRACEPARENT` environment variable as a fallback.
- **Rich CLI Output**: Beautiful, readable terminal output with tracebacks using `rich`.
- **Configuration via Env Vars**: Easy configuration using `pydantic-settings`.

## Installation

You can install this package directly from the GitHub repository using `pip`:

```bash
pip install git+https://github.com/aurumorinc/python-logging.git
```

## Configuration

Configuration is handled via environment variables (or a `.env` file) using `pydantic-settings`.

| Environment Variable | Default | Description |
| :--- | :--- | :--- |
| `LOG_LEVEL` | `INFO` | The logging level (e.g., `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`). |
| `ENVIRONMENT` | `dev` | The execution environment. Must be one of: `dev`, `prod`, `cli`. |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `None` | The OTLP endpoint for exporting logs (and other telemetry). |
| `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT` | `None` | The specific OTLP endpoint for exporting logs. |
| `TRACEPARENT` | `None` | W3C Trace Context string, used by Windmill for distributed tracing. |

## Usage

### Basic Usage

Initialize the logging system once at the entry point of your application, then use `get_logger` to create logger instances.

```python
from python_logging.main import setup_logging, get_logger

# 1. Initialize logging (call this once at startup)
setup_logging()

# 2. Get a logger instance
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
from python_logging.main import get_logger

logger = get_logger(__name__).bind(request_id="req-abc-123")

logger.info("processing_request") 
# Includes: request_id="req-abc-123"

logger.info("request_completed", status=200) 
# Includes: request_id="req-abc-123", status=200
```

### OpenTelemetry Integration

If you are using OpenTelemetry for distributed tracing, `python-logging` will automatically extract the active `trace_id` and `span_id` and inject them into your log records.

If you configure `OTEL_EXPORTER_OTLP_ENDPOINT` or `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT`, logs will also be exported to your OTLP collector automatically.

```python
from opentelemetry import trace
from python_logging.main import setup_logging, get_logger

setup_logging()
logger = get_logger(__name__)
tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("my_operation"):
    # This log will automatically include trace_id and span_id
    logger.info("operation_started")
```

### Windmill Integration

When running inside Windmill, OpenTelemetry spans might not be actively managed in the Python process, but Windmill passes the trace context via the `TRACEPARENT` environment variable. `python-logging` automatically detects this and injects the `trace_id` and `span_id` into your logs.

```bash
export TRACEPARENT="00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01"
```

```python
from python_logging.main import setup_logging, get_logger

setup_logging()
logger = get_logger(__name__)

# This log will include trace_id="0af7651916cd43dd8448eb211c80319c" and span_id="b7ad6b7169203331"
logger.info("running_in_windmill")
```

## Environments & Log Output Examples

The output format changes drastically based on the `ENVIRONMENT` variable to best suit the execution context.

### Development (`ENVIRONMENT=dev`)

Optimized for local development. Uses `structlog.dev.ConsoleRenderer` to provide colorized, easy-to-read output in the terminal.

**Configuration:**
```bash
export ENVIRONMENT=dev
export LOG_LEVEL=DEBUG
```

**Code:**
```python
logger.debug("database_query", table="users", duration_ms=15.2)
logger.info("user_created", user_id=42)
```

**Output Example:**
```text
2026-05-20T14:32:10.123456Z [debug    ] database_query                 duration_ms=15.2 table=users
2026-05-20T14:32:10.124567Z [info     ] user_created                   user_id=42
```
*(Note: The actual output will be colorized in your terminal)*

### Production (`ENVIRONMENT=prod`)

Optimized for log aggregators (Datadog, ELK, Splunk, etc.). Uses `structlog.processors.JSONRenderer` to output strict JSON.

**Configuration:**
```bash
export ENVIRONMENT=prod
export LOG_LEVEL=INFO
```

**Code:**
```python
logger.info("payment_processed", amount=100.00, currency="USD", order_id="ord-789")
```

**Output Example:**
```json
{"amount": 100.0, "currency": "USD", "order_id": "ord-789", "level": "info", "logger": "my_module", "timestamp": "2026-05-20T14:35:22.987654Z", "event": "payment_processed"}
```

### CLI (`ENVIRONMENT=cli`)

Optimized for command-line interfaces and scripts where you want beautiful, rich formatting for the end-user. Uses `rich.logging.RichHandler`.

**Configuration:**
```bash
export ENVIRONMENT=cli
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
*(Note: The actual output will be beautifully formatted and colorized by `rich`, with aligned timestamps and levels)*

## Development

To set up the project for development:

1. Ensure you have Python 3.9+ installed.
2. Install dependencies (using `pdm`, `hatch`, or `pip`):
   ```bash
   pip install -e ".[dev]"
   ```
3. Run tests:
   ```bash
   pytest
   ```
