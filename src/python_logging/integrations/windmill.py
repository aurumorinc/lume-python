# src/python_logging/integrations/windmill.py
from typing import Dict

from python_logging.config import settings


def get_windmill_context() -> Dict[str, str]:
    """
    Extracts trace_id and span_id from the TRACEPARENT environment variable.
    
    Returns:
        A dictionary containing 'trace_id' and 'span_id' if found, otherwise an empty dictionary.
    """
    traceparent = settings.traceparent
    if traceparent:
        parts = traceparent.split("-")
        if len(parts) >= 3:
            return {
                "trace_id": parts[1],
                "span_id": parts[2],
            }
    return {}
