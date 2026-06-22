---
name: posthog
description: Provides specialized context, rules, and tools for implementing, configuring, and debugging posthog. Use this skill whenever modifying posthog configurations or adding related functionality.
---
# posthog

## File Tree

```text
posthog/
├── assets
├── modules
│   └── posthog-python (See AST Map below)
├── references
├── scripts
└── SKILL.md
```

### AST Map: `modules/posthog-python`

```python
.github\scripts\check_crap_threshold.py:
⋮
│def covered_lines_for_file(coverage_file: Path, source_file: Path) -> set[int]:
⋮

.github\scripts\test_check_public_api.py:
⋮
│def load_check_public_api():
⋮
│def test_attribute_details_uses_placeholder_values() -> None:
⋮

bin\docs_scripts\doc_constant.py:
⋮
│DOCUMENTATION_METADATA = {
│    "hogRef": "0.3",
│    "slugPrefix": "posthog-python",
│    "specUrl": "https://github.com/PostHog/posthog-python",
⋮
│DOCSTRING_PATTERNS = {
│    "examples_section": r"Examples:\s*\n(.*?)(?=\n\s*\n\s*Category:|\Z)",
│    "args_section": r"Args:\s*\n(.*?)(?=\n\s*\n\s*Examples:|\n\s*\n\s*Details:|\n\s*\n\s*Category:|
│    "details_section": r"Details:\s*\n(.*?)(?=\n\s*\n\s*Examples:|\n\s*\n\s*Category:|\Z)",
│    "category_section": r"Category:\s*\n\s*(.+?)\s*(?:\n|$)",
│    "code_block": r"```(?:python)?\n(.*?)```",
│    "param_description": r"^\s*{param_name}:\s*(.+?)(?=\n\s*\w+:|\Z)",
│    "args_marker": r"\n\s*Args:\s*\n",
│    "examples_marker": r"\n\s*Examples:\s*\n",
│    "details_marker": r"\n\s*Details:\s*\n",
⋮
│OUTPUT_CONFIG: Dict[str, Union[str, int]] = {
│    "output_dir": "./references",
│    "filename": f"posthog-python-references-{VERSION}.json",
│    "filename_latest": "posthog-python-references-latest.json",
│    "indent": 2,
⋮
│DOC_DEFAULTS = {
│    "showDocs": True,
│    "releaseTag": "public",
│    "return_type_void": "None",
│    "max_optional_params": 3,
⋮

bin\docs_scripts\generate_json_schemas.py:
⋮
│def get_type_name(type_annotation) -> str:
⋮

examples\redis_flag_cache.py:
⋮
│class RedisFlagCache(FlagDefinitionCacheProvider):
⋮

integration_tests\django5\testdjango\asgi.py:
⋮
│application = get_asgi_application()

integration_tests\django5\testdjango\urls.py:
⋮
│urlpatterns = [
│    path("admin/", admin.site.urls),
│    path("test/async-user", views.test_async_user),
│    path("test/sync-user", views.test_sync_user),
│    path("test/async-exception", views.test_async_exception),
│    path("test/sync-exception", views.test_sync_exception),
⋮

integration_tests\django5\testdjango\views.py:
⋮
│async def test_async_user(request):
⋮
│def test_sync_user(request):
⋮
│async def test_async_exception(request):
⋮
│def test_sync_exception(request):
⋮

integration_tests\django5\testdjango\wsgi.py:
⋮
│application = get_wsgi_application()

posthog\__init__.py:
⋮
│def new_context(
│    fresh: bool = False,
│    capture_exceptions: Optional[bool] = None,
│    client: Optional[Client] = None,
⋮
│def identify_context(distinct_id: str):
⋮
│debug = False  # type: bool
⋮
│privacy_mode = False  # type: bool
⋮
│def set(**kwargs: Unpack[OptionalSetArgs]) -> Optional[str]:
⋮
│def capture_exception(
│    exception: Optional[ExceptionArg] = None,
│    **kwargs: Unpack[OptionalCaptureArgs],
⋮
│def join() -> None:
⋮
│def setup() -> Client:
⋮
│def _proxy(method, *args, **kwargs):
⋮

posthog\_async_utils.py:
⋮
│class _BackgroundEventLoopRunner:
│    """Run awaitables to completion on a reusable background event loop."""
│
⋮
│    def close(self) -> None:
⋮

posthog\_logging.py:
⋮
│class _PostHogLogPrefixFilter(logging.Filter):
⋮

posthog\ai\anthropic\anthropic.py:
⋮
│class Anthropic(anthropic.Anthropic):
⋮
│class WrappedMessages(Messages):
│    _client: Anthropic
│
│    def create(
│        self,
│        posthog_distinct_id: Optional[str] = None,
│        posthog_trace_id: Optional[str] = None,
│        posthog_properties: Optional[Dict[str, Any]] = None,
│        posthog_privacy_mode: bool = False,
│        posthog_groups: Optional[Dict[str, Any]] = None,
│        **kwargs: Any,
⋮

posthog\ai\anthropic\anthropic_async.py:
⋮
│class AsyncWrappedMessages(AsyncMessages):
│    _client: AsyncAnthropic
│
│    async def create(
│        self,
│        posthog_distinct_id: Optional[str] = None,
│        posthog_trace_id: Optional[str] = None,
│        posthog_properties: Optional[Dict[str, Any]] = None,
│        posthog_privacy_mode: bool = False,
│        posthog_groups: Optional[Dict[str, Any]] = None,
│        **kwargs: Any,
⋮

posthog\ai\anthropic\anthropic_converter.py:
⋮
│def format_anthropic_streaming_content(
│    content_blocks: List[StreamingContentBlock],
⋮
│def extract_anthropic_web_search_count(response: Any) -> int:
⋮

posthog\ai\claude_agent_sdk\__init__.py:
⋮
│def instrument(
│    client: Optional[Client] = None,
│    distinct_id: Optional[Union[str, Callable[[ResultMessage], Optional[str]]]] = None,
│    privacy_mode: bool = False,
│    groups: Optional[Dict[str, Any]] = None,
│    properties: Optional[Dict[str, Any]] = None,
⋮

posthog\ai\claude_agent_sdk\client.py:
⋮
│class PostHogClaudeSDKClient:
│    """Wraps ClaudeSDKClient for stateful multi-turn conversations with PostHog instrumentation.
│
│    Usage:
│        async with PostHogClaudeSDKClient(options, posthog_client=ph, posthog_distinct_id="user") a
│            await client.query("Hello")
│            async for msg in client.receive_response():
│                ...  # turn 1, emits $ai_generation events
│            await client.query("Follow up")
│            async for msg in client.receive_response():
│                ...  # turn 2, same trace, has conversation history
⋮
│    async def receive_response(self):
⋮
│    async def set_model(self, model: Optional[str] = None) -> None:
⋮

posthog\ai\claude_agent_sdk\processor.py:
⋮
│class _GenerationTracker:
│    """Tracks StreamEvent boundaries to reconstruct per-generation metrics.
│
│    Each message_start -> message_stop cycle in the Anthropic streaming protocol
│    represents one API call (one generation).
⋮
│    def process_stream_event(self, event: "StreamEvent") -> None:
⋮
│    def set_model(self, model: str) -> None:
⋮
│    def has_completed_generation(self) -> bool:
⋮
│    def pop_generation(self) -> _GenerationData:
⋮
│class PostHogClaudeAgentProcessor:
│    """Wraps claude_agent_sdk.query() to emit PostHog LLM analytics events.
│
│    Emits:
│    - $ai_generation: one per Anthropic API call (reconstructed from StreamEvents)
│    - $ai_span: one per tool use (ToolUseBlock in AssistantMessage)
│    - $ai_trace: one per query() call (on ResultMessage)
⋮
│    def _with_privacy_mode(self, value: Any) -> Any:
⋮
│    def _capture_event(
│        self,
│        event: str,
│        properties: Dict[str, Any],
│        distinct_id: Optional[str] = None,
│        groups: Optional[Dict[str, Any]] = None,
⋮
│def _ensure_serializable(obj: Any) -> Any:
⋮

posthog\ai\gateway.py:
⋮
│def is_posthog_ai_gateway_url(base_url: Any) -> bool:
⋮
│def warn_if_posthog_ai_gateway(base_url: Any) -> None:
⋮
│def warn_if_posthog_ai_gateway_otel_attributes(
│    attributes: Optional[Mapping[str, Any]],
⋮

posthog\ai\gemini\__init__.py:
⋮
│class _GenAI:
⋮
│genai = _GenAI()
│
⋮

posthog\ai\gemini\gemini.py:
⋮
│class Client:
⋮
│class Models:
│    """
│    Models interface that mimics genai.Client().models with PostHog tracking.
⋮
│    def generate_content(
│        self,
│        model: str,
│        contents,
│        posthog_distinct_id: Optional[str] = None,
│        posthog_trace_id: Optional[str] = None,
│        posthog_properties: Optional[Dict[str, Any]] = None,
│        posthog_privacy_mode: Optional[bool] = None,
│        posthog_groups: Optional[Dict[str, Any]] = None,
│        **kwargs: Any,
⋮
│    def generate_content_stream(
│        self,
│        model: str,
│        contents,
│        posthog_distinct_id: Optional[str] = None,
│        posthog_trace_id: Optional[str] = None,
│        posthog_properties: Optional[Dict[str, Any]] = None,
│        posthog_privacy_mode: Optional[bool] = None,
│        posthog_groups: Optional[Dict[str, Any]] = None,
│        **kwargs: Any,
⋮
│    def embed_content(
│        self,
│        model: str,
│        contents,
│        posthog_distinct_id: Optional[str] = None,
│        posthog_trace_id: Optional[str] = None,
│        posthog_properties: Optional[Dict[str, Any]] = None,
│        posthog_privacy_mode: Optional[bool] = None,
│        posthog_groups: Optional[Dict[str, Any]] = None,
│        **kwargs: Any,
⋮

posthog\ai\gemini\gemini_async.py:
⋮
│class AsyncClient:
⋮
│class AsyncModels:
│    """
│    Async Models interface that mimics genai.Client().aio.models with PostHog tracking.
⋮
│    async def generate_content_stream(
│        self,
│        model: str,
│        contents,
│        posthog_distinct_id: Optional[str] = None,
│        posthog_trace_id: Optional[str] = None,
│        posthog_properties: Optional[Dict[str, Any]] = None,
│        posthog_privacy_mode: Optional[bool] = None,
│        posthog_groups: Optional[Dict[str, Any]] = None,
│        **kwargs: Any,
⋮

posthog\ai\gemini\gemini_converter.py:
⋮
│def extract_gemini_stop_reason(response: Any) -> Optional[str]:
⋮
│def extract_gemini_system_instruction(config: Any) -> Optional[str]:
⋮
│def format_gemini_input(contents: Any) -> List[FormattedMessage]:
⋮
│def extract_gemini_web_search_count(response: Any) -> int:
⋮

posthog\ai\langchain\callbacks.py:
⋮
│class CallbackHandler(BaseCallbackHandler):
⋮

posthog\ai\openai\openai.py:
⋮
│class OpenAI(openai.OpenAI):
⋮
│class WrappedResponses(_OpenAIWrapperResource):
│    """Wrapper for OpenAI responses that tracks usage in PostHog."""
│
│    def create(
│        self,
│        posthog_distinct_id: Optional[str] = None,
│        posthog_trace_id: Optional[str] = None,
│        posthog_properties: Optional[Dict[str, Any]] = None,
│        posthog_privacy_mode: bool = False,
│        posthog_groups: Optional[Dict[str, Any]] = None,
│        **kwargs: Any,
⋮
│class WrappedCompletions(_OpenAIWrapperResource):
│    """Wrapper for OpenAI chat completions that tracks usage in PostHog."""
│
⋮
│    def create(
│        self,
│        posthog_distinct_id: Optional[str] = None,
│        posthog_trace_id: Optional[str] = None,
│        posthog_properties: Optional[Dict[str, Any]] = None,
│        posthog_privacy_mode: bool = False,
│        posthog_groups: Optional[Dict[str, Any]] = None,
│        **kwargs: Any,
⋮
│class WrappedEmbeddings(_OpenAIWrapperResource):
│    """Wrapper for OpenAI embeddings that tracks usage in PostHog."""
│
│    def create(
│        self,
│        posthog_distinct_id: Optional[str] = None,
│        posthog_trace_id: Optional[str] = None,
│        posthog_properties: Optional[Dict[str, Any]] = None,
│        posthog_privacy_mode: bool = False,
│        posthog_groups: Optional[Dict[str, Any]] = None,
│        **kwargs: Any,
⋮

posthog\ai\openai\openai_async.py:
⋮
│class WrappedResponses(_OpenAIWrapperResource):
│    """Async wrapper for OpenAI responses that tracks usage in PostHog."""
│
│    async def create(
│        self,
│        posthog_distinct_id: Optional[str] = None,
│        posthog_trace_id: Optional[str] = None,
│        posthog_properties: Optional[Dict[str, Any]] = None,
│        posthog_privacy_mode: bool = False,
│        posthog_groups: Optional[Dict[str, Any]] = None,
│        **kwargs: Any,
⋮
│class WrappedCompletions(_OpenAIWrapperResource):
│    """Async wrapper for OpenAI chat completions that tracks usage in PostHog."""
│
⋮
│    async def create(
│        self,
│        posthog_distinct_id: Optional[str] = None,
│        posthog_trace_id: Optional[str] = None,
│        posthog_properties: Optional[Dict[str, Any]] = None,
│        posthog_privacy_mode: bool = False,
│        posthog_groups: Optional[Dict[str, Any]] = None,
│        **kwargs: Any,
⋮
│class WrappedEmbeddings(_OpenAIWrapperResource):
│    """Async wrapper for OpenAI embeddings that tracks usage in PostHog."""
│
│    async def create(
│        self,
│        posthog_distinct_id: Optional[str] = None,
│        posthog_trace_id: Optional[str] = None,
│        posthog_properties: Optional[Dict[str, Any]] = None,
│        posthog_privacy_mode: bool = False,
│        posthog_groups: Optional[Dict[str, Any]] = None,
│        **kwargs: Any,
⋮

posthog\ai\openai\openai_converter.py:
⋮
│def extract_openai_web_search_count(response: Any) -> int:
⋮

posthog\ai\openai\wrapper_utils.py:
⋮
│def warn_on_fallback(wrapper_name: str, name: str) -> None:
⋮

posthog\ai\openai_agents\__init__.py:
⋮
│def instrument(
│    client: Optional[Client] = None,
│    distinct_id: Optional[Union[str, Callable[[Trace], Optional[str]]]] = None,
│    privacy_mode: bool = False,
│    groups: Optional[Dict[str, Any]] = None,
│    properties: Optional[Dict[str, Any]] = None,
⋮

posthog\ai\openai_agents\processor.py:
⋮
│class PostHogTracingProcessor(TracingProcessor):
│    """
│    A tracing processor that sends OpenAI Agents SDK traces to PostHog.
│
│    This processor implements the TracingProcessor interface from the OpenAI Agents SDK
│    and maps agent traces, spans, and generations to PostHog's LLM analytics events.
│
│    Example:
│        ```python
│        from agents import Agent, Runner
│        from agents.tracing import add_trace_processor
⋮
│    def force_flush(self) -> None:
⋮

posthog\ai\otel\exporter.py:
⋮
│class PostHogTraceExporter(SpanExporter):
│    """Span exporter that filters AI spans and forwards them to PostHog.
│
│    Wraps an OTLPSpanExporter configured for PostHog's OTLP endpoint. Spans
│    that are not AI-related are silently dropped, returning SUCCESS immediately.
│
│    Usage::
│
│        from opentelemetry.sdk.trace import TracerProvider
│        from opentelemetry.sdk.trace.export import BatchSpanProcessor
│        from posthog.ai.otel import PostHogTraceExporter
│
⋮
│    def force_flush(self, timeout_millis: Optional[int] = None) -> bool:
⋮

posthog\ai\otel\processor.py:
⋮
│class PostHogSpanProcessor(SpanProcessor):
│    """Span processor that filters AI spans and exports them to PostHog.
│
│    Wraps a BatchSpanProcessor and OTLPSpanExporter internally, configured
│    to send to PostHog's OTLP traces endpoint. Only spans identified as
│    AI-related (by name or attribute prefix) are forwarded for export.
│
│    Usage::
│
│        from opentelemetry.sdk.trace import TracerProvider
│        from posthog.ai.otel import PostHogSpanProcessor
│
⋮
│    def force_flush(self, timeout_millis: Optional[int] = None) -> bool:
⋮

posthog\ai\otel\spans.py:
⋮
│DEFAULT_HOST = "https://us.i.posthog.com"
│
│AI_SPAN_PREFIXES = ("gen_ai.", "llm.", "ai.", "traceloop.")
│
⋮
│def is_ai_span(span: "ReadableSpan") -> bool:
⋮

posthog\ai\prompts.py:
⋮
│@dataclass(frozen=True)
│class PromptResult:
⋮
│class CachedPrompt:
⋮
│class Prompts:
│    """
│    Fetch and compile LLM prompts from PostHog.
│
│    Can be initialized with a PostHog client or with direct options.
│
│    Examples:
│        ```python
│        from posthog import Posthog
│        from posthog.ai.prompts import Prompts
│
⋮
│    @overload
│    def get(
│        self,
│        name: str,
│        *,
│        with_metadata: Literal[True],
│        cache_ttl_seconds: Optional[int] = ...,
│        fallback: Optional[str] = ...,
│        version: Optional[int] = ...,
⋮
│    @overload
│    def get(
│        self,
│        name: str,
│        *,
│        with_metadata: Literal[False],
│        cache_ttl_seconds: Optional[int] = ...,
│        fallback: Optional[str] = ...,
│        version: Optional[int] = ...,
⋮
│    @overload
│    def get(
│        self,
│        name: str,
│        *,
│        cache_ttl_seconds: Optional[int] = ...,
│        fallback: Optional[str] = ...,
│        version: Optional[int] = ...,
⋮
│    def get(
│        self,
│        name: str,
│        *,
│        with_metadata: Optional[bool] = None,
│        cache_ttl_seconds: Optional[int] = None,
│        fallback: Optional[str] = None,
│        version: Optional[int] = None,
⋮
│    def compile(self, prompt: str, variables: PromptVariables) -> str:
⋮

posthog\ai\sanitization.py:
⋮
│def is_base64_data_url(text: str) -> bool:
⋮
│def is_valid_url(text: str) -> bool:
⋮
│def is_raw_base64(text: str) -> bool:
⋮
│def redact_base64_data_url(value: Any) -> Any:
⋮
│def process_messages(messages: Any, transform_content_func) -> Any:
│    if not messages:
⋮
│    def process_content(content: Any) -> Any:
⋮
│    def process_message(msg: Any) -> Any:
⋮
│def sanitize_gemini_part(part: Any) -> Any:
⋮
│def process_gemini_item(item: Any) -> Any:
⋮
│def sanitize_anthropic(data: Any) -> Any:
⋮
│def sanitize_gemini(data: Any) -> Any:
⋮

posthog\ai\stream.py:
⋮
│class AsyncStreamWrapper(Generic[T]):
⋮

posthog\ai\types.py:
⋮
│class FormattedTextContent(TypedDict):
⋮
│class FormattedFunctionCall(TypedDict, total=False):
⋮
│class FormattedImageContent(TypedDict):
⋮
│FormattedContentItem = Union[
│    FormattedTextContent,
│    FormattedFunctionCall,
│    FormattedImageContent,
│    Dict[str, Any],  # Fallback for unknown content types
⋮
│class FormattedMessage(TypedDict):
⋮
│class TokenUsage(TypedDict, total=False):
⋮
│class ProviderResponse(TypedDict, total=False):
⋮
│class StreamingContentBlock(TypedDict, total=False):
⋮
│class ToolInProgress(TypedDict):
⋮
│class StreamingEventData(TypedDict):
⋮

posthog\ai\utils.py:
⋮
│def _get_tokens_source(
│    sdk_tags: Dict[str, Any], posthog_properties: Optional[Dict[str, Any]]
⋮
│def serialize_raw_usage(raw_usage: Any) -> Optional[Dict[str, Any]]:
⋮
│def merge_usage_stats(
│    target: TokenUsage, source: TokenUsage, mode: str = "incremental"
⋮
│def get_model_params(kwargs: Dict[str, Any]) -> Dict[str, Any]:
⋮
│def extract_available_tool_calls(provider: str, kwargs: Dict[str, Any]):
⋮
│def merge_system_prompt(
│    kwargs: Dict[str, Any], provider: str
⋮
│def call_llm_and_track_usage(
│    posthog_distinct_id: Optional[str],
│    ph_client: PostHogClient,
│    provider: str,
│    posthog_trace_id: Optional[str],
│    posthog_properties: Optional[Dict[str, Any]],
│    posthog_privacy_mode: bool,
│    posthog_groups: Optional[Dict[str, Any]],
│    base_url: str,
│    call_method: Callable[..., Any],
⋮
│def with_privacy_mode(ph_client: PostHogClient, privacy_mode: bool, value: Any):
⋮
│def capture_streaming_event(
│    ph_client: PostHogClient,
│    event_data: StreamingEventData,
⋮

posthog\bucketed_rate_limiter.py:
⋮
│def _clamp_to_range(value, min_value: Number, max_value: Number, label: str) -> Number:
⋮
│class BucketedRateLimiter:
│    """Token bucket rate limiter that tracks a separate bucket per key.
│
│    Each key starts with a full bucket of ``bucket_size`` tokens and every
│    call to :meth:`consume_rate_limit` consumes one token. ``refill_rate``
│    tokens are restored per elapsed ``refill_interval_seconds`` (whole
│    intervals only, fractional elapsed time is carried over), capped at
│    ``bucket_size``.
│
│    The call that empties a bucket is itself reported as rate limited — a
│    burst over a fresh bucket lets ``bucket_size - 1`` events through before
⋮
│    def consume_rate_limit(self, key: Hashable) -> bool:
⋮

posthog\client.py:
⋮
│class Client(object):
│    """
│    This is the SDK reference for the PostHog Python SDK.
│    You can learn more about example usage in the [Python SDK documentation](/docs/libraries/python
│    You can also follow [Flask](/docs/libraries/flask) and [Django](/docs/libraries/django)
│    guides to integrate PostHog into your project.
│
│    For long-running applications, create one client during application startup
│    and reuse it for the lifetime of the process. This keeps background queues
│    predictable and makes shutdown flushing straightforward. Multiple clients are
│    still supported for intentional multi-project or multi-host setups.
│
⋮
│    def _set_before_send(self, before_send):
⋮
│    def new_context(self, fresh=False, capture_exceptions: Optional[bool] = None):
⋮
│    def get_tags(self) -> Dict[str, Any]:
⋮
│    def identify_context(self, distinct_id: str) -> None:
⋮
│    @no_throw()
│    def capture(
│        self, event: str, **kwargs: Unpack[OptionalCaptureArgs]
⋮
│    @no_throw()
│    def set(self, **kwargs: Unpack[OptionalSetArgs]) -> Optional[str]:
⋮
│    def capture_exception(
│        self,
│        exception: Optional[ExceptionArg],
│        **kwargs: Unpack[OptionalCaptureArgs],
⋮
│    def join(self) -> None:
⋮

posthog\consumer.py:
⋮
│class Consumer(Thread):
⋮

posthog\contexts.py:
⋮
│class ContextScope:
│    def __init__(
│        self,
│        parent=None,
│        fresh: bool = False,
│        capture_exceptions: bool = True,
│        client: Optional["Client"] = None,
⋮
│    def set_session_id(self, session_id: str):
⋮
│    def set_distinct_id(self, distinct_id: str):
⋮
│    def set_device_id(self, device_id: str):
⋮
│    def set_code_variables_mask_patterns(self, mask_patterns: list):
⋮
│    def set_code_variables_ignore_patterns(self, ignore_patterns: list):
⋮
│    def set_code_variables_mask_url_credentials(self, enabled: bool):
⋮
│    def get_session_id(self) -> Optional[str]:
⋮
│    def get_distinct_id(self) -> Optional[str]:
⋮
│    def get_device_id(self) -> Optional[str]:
⋮
│    def collect_tags(self) -> Dict[str, Any]:
⋮
│    def get_capture_exception_code_variables(self) -> Optional[bool]:
⋮
│    def get_code_variables_mask_patterns(self) -> Optional[list]:
⋮
│    def get_code_variables_ignore_patterns(self) -> Optional[list]:
⋮
│    def get_code_variables_mask_url_credentials(self) -> Optional[bool]:
⋮
│@contextmanager
│def new_context(
│    fresh: bool = False,
│    capture_exceptions: Optional[bool] = None,
│    client: Optional["Client"] = None,
⋮
│def identify_context(distinct_id: str) -> None:
⋮
│def get_context_session_id() -> Optional[str]:
⋮
│def get_context_distinct_id() -> Optional[str]:
⋮

posthog\exception_capture.py:
⋮
│class ExceptionCapture:
│    log = logging.getLogger("posthog")
│
⋮
│    def close(self):
⋮
│    def capture_exception(self, exception, metadata=None):
⋮

posthog\exception_utils.py:
⋮
│class VariableSizeLimiter:
⋮
│class AnnotatedValue:
⋮
│def get_type_name(cls):
⋮
│def get_type_module(cls):
⋮
│def should_hide_frame(frame: "FrameType") -> bool:
⋮
│def iter_stacks(tb):
⋮
│def get_lines_from_file(
│    filename,  # type: str
│    lineno,  # type: int
│    max_length=None,  # type: Optional[int]
│    loader=None,  # type: Optional[Any]
│    module=None,  # type: Optional[str]
⋮
│def get_source_context(
│    frame,  # type: FrameType
│    tb_lineno,  # type: int
│    max_value_length=None,  # type: Optional[int]
⋮
│def safe_str(value):
⋮
│def safe_repr(value):
⋮
│def filename_for_module(module, abs_path):
⋮
│def serialize_frame(
│    frame,
│    tb_lineno=None,
│    max_value_length=None,
⋮
│def get_errno(exc_value):
⋮
│def get_error_message(exc_value):
⋮
│def single_exception_from_error_tuple(
│    exc_type,  # type: Optional[type]
│    exc_value,  # type: Optional[BaseException]
│    tb,  # type: Optional[TracebackType]
│    mechanism=None,  # type: Optional[Dict[str, Any]]
│    exception_id=None,  # type: Optional[int]
│    parent_id=None,  # type: Optional[int]
│    source=None,  # type: Optional[str]
⋮
│if HAS_CHAINED_EXCEPTIONS:
│
│    def walk_exception_chain(exc_info):
│        # type: (ExcInfo) -> Iterator[ExcInfo]
│        exc_type, exc_value, tb = exc_info
│
│        seen_exceptions = []
│        seen_exception_ids = set()  # type: Set[int]
│
│        while (
│            exc_type is not None
│            and exc_value is not None
⋮
│else:
│
│    def walk_exception_chain(exc_info):
│        # type: (ExcInfo) -> Iterator[ExcInfo]
⋮
│def exceptions_from_error(
│    exc_type,  # type: Optional[type]
│    exc_value,  # type: Optional[BaseException]
│    tb,  # type: Optional[TracebackType]
│    mechanism=None,  # type: Optional[Dict[str, Any]]
│    exception_id=0,  # type: int
│    parent_id=0,  # type: int
│    source=None,  # type: Optional[str]
⋮
│def iter_event_stacktraces(event):
⋮
│def set_in_app_in_frames(frames, in_app_exclude, in_app_include, project_root=None):
⋮
│def exc_info_from_error(error):
⋮
│def construct_artificial_traceback(e):
⋮
│def strip_string(value, max_length=None):
⋮
│def attach_code_variables_to_frames(
│    all_exceptions, exc_info, mask_patterns, ignore_patterns, mask_url_credentials=True
⋮

posthog\feature_flag_evaluations.py:
⋮
│class FeatureFlagEvaluations:
⋮

posthog\feature_flags.py:
⋮
│class InconclusiveMatchError(Exception):
⋮

posthog\integrations\celery.py:
⋮
│class PosthogCeleryIntegration:
│    """Celery integration that captures task lifecycle events and exceptions.
│
│    Args:
│        client: Optional ``Client`` instance. When provided, all events and
│            exceptions are captured through this client rather than the
│            global ``posthog`` module. Don't skip this if using a custom flag
│            definition cache provider, and pass the custom ``Client`` instance
│            here initialized with the custom provider so fork safety for that
│            provider is handled correctly.
│        capture_exceptions: Whether to capture task exceptions via
⋮
│    def instrument(self) -> None:
⋮

posthog\request.py:
⋮
│@dataclass
│class GetResponse:
⋮
│class HTTPAdapterWithSocketOptions(HTTPAdapter):
│    """HTTPAdapter with configurable socket options."""
│
⋮
│    def init_poolmanager(self, *args, **kwargs):
⋮
│def set_socket_options(socket_options: Optional[SocketOptions]) -> None:
⋮
│def normalize_host(host: Optional[str]) -> str:
⋮
│def is_ai_event(event_name) -> bool:
⋮
│def batch_post(
│    api_key: str,
│    host: Optional[str] = None,
│    gzip: bool = False,
│    timeout: int = 15,
│    path: str = EVENTS_ENDPOINT,
│    **kwargs,
⋮
│def get(
│    api_key: str,
│    url: str,
│    host: Optional[str] = None,
│    timeout: Optional[int] = None,
│    etag: Optional[str] = None,
⋮
│class APIError(Exception):
⋮
│class QuotaLimitError(APIError):
⋮

posthog\test\__init__.py:
⋮
│def all_names():
⋮

posthog\test\ai\langchain\test_callbacks.py:
⋮
│try:
⋮
│except ImportError:
│
│    class FakeListLLM:
⋮
│    class HumanMessage:
⋮

posthog\test\ai\utils.py:
⋮
│class RecordingAsyncStream:
│    """Mock provider async stream that is iterable and records when closed.
│
│    Mirrors the real ``openai.AsyncStream`` / ``anthropic.AsyncStream``: it
│    supports ``async for`` and exposes an async ``close()`` plus a ``response``
│    attribute, so tests can assert both iteration and that the underlying
│    stream is closed on context exit.
⋮
│    def __aiter__(self):
⋮
│    async def close(self):
⋮

posthog\test\conftest.py:
⋮
│@pytest.fixture(autouse=True)
│def disable_client_atexit_join(monkeypatch):
⋮

posthog\test\test_code_variables.py:
⋮
│def make_config(
│    *, patterns=DEFAULT_CODE_VARIABLES_MASK_PATTERNS, ignore=(), mask_urls=True
⋮
│def encode(value, *, limiter=None, **kwargs):
⋮
│class TestObjectTraversal:
│    """Custom objects are decomposed into their real fields, so a `password` attribute
⋮
│    def test_plain_object_is_decomposed_via_its_dict(self):
│        # obj.username="alice", obj.api_key=<secret>
│        class Credentials:
│            def __init__(self):
│                self.username = "alice"
⋮
│    def test_sensitively_named_cached_property_is_not_leaked(self):
⋮
│        class Client:
│            @functools.cached_property
│            def api_key(self):
│                return "sk_live_xyz"
│
│            def __repr__(self):
⋮

posthog\test\test_utils.py:
⋮
│class FakeRedis:
│    def __init__(self, fail=False):
│        self.store = {}
│        self.fail = fail
│        self.setex_calls = []
│        self.scan_calls = []
⋮
│    def get(self, key):
⋮
│    def set(self, key, value):
⋮
│    def scan(self, cursor, match=None, count=None):
⋮
│    def delete(self, *keys):
⋮
│class TestUtils(unittest.TestCase):
│    @parameterized.expand(
│        [
│            ("naive datetime should be naive", True),
│            ("timezone-aware datetime should not be naive", False),
│        ]
⋮
│    def test_clean_pydantic(self):
│        class ModelV2(BaseModel):
│            foo: str
│            bar: int
⋮
│        class ModelDumpOnly:
│            def model_dump(self):
⋮
│    def test_clean_pydantic_like_class(self) -> None:
│        class Dummy:
│            def model_dump(self, required_param: str) -> dict:
⋮
│    def test_coerce_unicode(self):
│        assert utils._coerce_unicode("already unicode") == "already unicode"
⋮
│        class UndecodableBytes(bytes):
│            def decode(self, *args, **kwargs):
⋮
│class TestFlagCache(unittest.TestCase):
│    def setUp(self):
│        self.cache = utils.FlagCache(max_size=3, default_ttl=1)
│        self.flag_result = FeatureFlagResult.from_value_and_payload(
│            "test-flag", True, None
⋮
│    def test_stale_cache_passes_current_time_and_max_age(self):
│        class StrictEntry:
│            flag_result = "stale-result"
│
│            def is_stale_but_usable(self, current_time, max_stale_age=3600):
│                assert current_time == 1234
│                assert max_stale_age == 99
⋮

posthog\types.py:
⋮
│@dataclass(frozen=True)
│class FlagReason:
│    """Reason metadata returned by the feature flag API.
│
│    Attributes:
│        code: Machine-readable reason code.
│        condition_index: Matching condition index, when available.
│        description: Human-readable reason description.
⋮
│    @classmethod
│    def from_json(cls, resp: Any) -> Optional["FlagReason"]:
⋮
│@dataclass(frozen=True)
│class LegacyFlagMetadata:
⋮
│@dataclass(frozen=True)
│class FlagMetadata:
│    """Feature flag metadata returned by the feature flag API.
│
│    Attributes:
│        id: Numeric feature flag ID.
│        payload: Payload configured for the matched flag value, if any.
│        version: Feature flag version.
│        description: Feature flag description.
⋮
│    @classmethod
│    def from_json(cls, resp: Any) -> Union["FlagMetadata", LegacyFlagMetadata]:
⋮
│@dataclass(frozen=True)
│class FeatureFlag:
│    """Detailed feature flag evaluation returned by the flags API.
│
│    Attributes:
│        key: Feature flag key.
│        enabled: Whether the flag is enabled for the evaluated user or group.
│        variant: Variant key for multivariate flags, otherwise ``None``.
│        reason: Optional reason metadata explaining the result.
│        metadata: Payload and other metadata returned by the API.
⋮
│    def get_value(self) -> FlagValue:
⋮
│    @classmethod
│    def from_json(cls, resp: Any) -> "FeatureFlag":
⋮
│    @classmethod
│    def from_value_and_payload(
│        cls, key: str, value: FlagValue, payload: Any
⋮
│@dataclass(frozen=True)
│class FeatureFlagResult:
│    """
│    The result of calling a feature flag which includes the flag result, variant, and payload.
│
│    Attributes:
│        key (str): The unique identifier of the feature flag.
│        enabled (bool): Whether the feature flag is enabled for the current context.
│        variant (Optional[str]): The variant value if the flag is enabled and has variants, None ot
│        payload (Optional[Any]): Additional data associated with the feature flag, if any.
│        reason (Optional[str]): A description of why the flag was enabled or disabled, if available
⋮
│    def get_value(self) -> FlagValue:
⋮
│    @classmethod
│    def from_value_and_payload(
│        cls, key: str, value: Union[FlagValue, None], payload: Any
⋮
│def to_values(response: FlagsResponse) -> Optional[dict[str, FlagValue]]:
⋮
│def to_payloads(response: FlagsResponse) -> Optional[dict[str, str]]:
⋮

posthog\utils.py:
⋮
│def is_naive(dt: datetime) -> bool:
⋮
│def total_seconds(delta: timedelta) -> float:
⋮
│def guess_timezone(dt: datetime) -> datetime:
⋮
│def remove_trailing_slash(host: str) -> str:
⋮
│def clean(item):
⋮
│def _clean_dict(dict_):
⋮
│def _coerce_unicode(cmplx: Any) -> Optional[str]:
⋮
│def is_valid_regex(value) -> bool:
⋮
│class SizeLimitedDict(defaultdict):
⋮
│class FlagCacheEntry:
│    def __init__(self, flag_result, flag_definition_version, timestamp=None):
│        self.flag_result = flag_result
│        self.flag_definition_version = flag_definition_version
⋮
│    def is_valid(self, current_time, ttl, current_flag_version):
⋮
│    def is_stale_but_usable(self, current_time, max_stale_age=CACHE_STALE_TTL):
⋮
│class FlagCache:
│    def __init__(self, max_size=CACHE_MAX_SIZE, default_ttl=CACHE_TTL):
│        self.cache = {}  # distinct_id -> {flag_key: FlagCacheEntry}
│        self.access_times = {}  # distinct_id -> last_access_time
│        self.max_size = max_size
⋮
│    def get_cached_flag(self, distinct_id, flag_key, current_flag_version):
⋮
│    def get_stale_cached_flag(self, distinct_id, flag_key, max_stale_age=None):
⋮
│    def set_cached_flag(
│        self, distinct_id, flag_key, flag_result, flag_definition_version
⋮
│    def invalidate_version(self, old_version):
⋮
│    def clear(self):
⋮
│class RedisFlagCache:
│    def __init__(
│        self,
│        redis_client,
│        default_ttl=CACHE_TTL,
│        stale_ttl=CACHE_STALE_TTL,
│        key_prefix=CACHE_KEY_PREFIX,
⋮
│    def _get_cache_key(self, distinct_id, flag_key):
⋮
│    def _serialize_entry(self, flag_result, flag_definition_version, timestamp=None):
⋮
│    def _deserialize_entry(self, data):
⋮
│    def get_cached_flag(self, distinct_id, flag_key, current_flag_version):
⋮
│    def get_stale_cached_flag(self, distinct_id, flag_key, max_stale_age=None):
⋮
│    def set_cached_flag(
│        self, distinct_id, flag_key, flag_result, flag_definition_version
⋮
│    def invalidate_version(self, old_version):
⋮
│    def _key_has_version(self, key, old_version):
⋮
│    def clear(self):
⋮
│def convert_to_datetime_aware(date_obj):
⋮
│def str_icontains(source, search):
⋮
│def str_iequals(value, comparand):
⋮
│def _platform_release():
⋮
│def get_os_info():
⋮
│def system_context() -> dict[str, Any]:
⋮

posthog\version.py:
│VERSION = "7.20.2"

sdk_compliance_adapter\adapter.py:
⋮
│@app.route("/capture", methods=["POST"])
│def capture():
⋮
```
