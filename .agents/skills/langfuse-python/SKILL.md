---
name: langfuse-python
description: Provides specialized context, rules, and tools for implementing, configuring, and debugging langfuse-python. Use this skill whenever modifying langfuse-python configurations or adding related functionality.
---
# langfuse-python

## File Tree

```text
langfuse-python/
├── assets
├── modules
│   └── langfuse-python (See AST Map below)
├── references
├── scripts
└── SKILL.md
```

### AST Map: `modules/langfuse-python`

```python
langfuse\__init__.py:
⋮
│Langfuse = _client_module.Langfuse
│
⋮

langfuse\_client\attributes.py:
⋮
│def _serialize(obj: Any) -> Optional[str]:
⋮
│def _flatten_and_serialize_metadata_values(
│    metadata: Optional[Dict[str, Any]],
│) -> Optional[Dict[str, str]]:
│    if metadata is None:
⋮
│    def flatten_value(path: str, value: Any) -> None:
⋮

langfuse\_client\client.py:
⋮
│class Langfuse:
│    """Main client for Langfuse tracing and platform features.
│
│    This class provides an interface for creating and managing traces, spans,
│    and generations in Langfuse as well as interacting with the Langfuse API.
│
│    The client features a thread-safe singleton pattern for each unique public API key,
│    ensuring consistent trace context propagation across your application. It implements
│    efficient batching of spans with configurable flush settings and includes background
│    thread management for media uploads and score ingestion.
│
⋮
│    @overload
│    def start_observation(
│        self,
│        *,
│        trace_context: Optional[TraceContext] = None,
│        name: str,
│        as_type: Literal["agent"],
│        input: Optional[Any] = None,
│        output: Optional[Any] = None,
│        metadata: Optional[Any] = None,
│        version: Optional[str] = None,
⋮
│    def start_observation(
│        self,
│        *,
│        trace_context: Optional[TraceContext] = None,
│        name: str,
│        as_type: ObservationTypeLiteralNoEvent = "span",
│        input: Optional[Any] = None,
│        output: Optional[Any] = None,
│        metadata: Optional[Any] = None,
│        version: Optional[str] = None,
⋮

langfuse\_client\constants.py:
⋮
│def get_observation_types_list(
│    literal_type: Any,
⋮

langfuse\_client\datasets.py:
⋮
│class DatasetClient:
│    """Class for managing datasets in Langfuse.
│
│    Attributes:
│        id (str): Unique identifier of the dataset.
│        name (str): Name of the dataset.
│        description (Optional[str]): Description of the dataset.
│        metadata (Optional[typing.Any]): Additional metadata of the dataset.
│        project_id (str): Identifier of the project to which the dataset belongs.
│        created_at (datetime): Timestamp of dataset creation.
│        updated_at (datetime): Timestamp of the last update to the dataset.
⋮
│    def run_experiment(
│        self,
│        *,
│        name: str,
│        run_name: Optional[str] = None,
│        description: Optional[str] = None,
│        task: TaskFunction,
│        evaluators: List[EvaluatorFunction] = [],
│        composite_evaluator: Optional[CompositeEvaluatorFunction] = None,
│        run_evaluators: List[RunEvaluatorFunction] = [],
⋮

langfuse\_client\get_client.py:
⋮
│def get_client(*, public_key: Optional[str] = None) -> Langfuse:
⋮

langfuse\_client\resource_manager.py:
⋮
│class LangfuseResourceManager:
│    """Thread-safe singleton that provides access to the OpenTelemetry tracer and processors.
│
│    This class implements a thread-safe singleton pattern keyed by the public API key,
│    ensuring that only one tracer instance exists per API key combination. It manages
│    the lifecycle of the OpenTelemetry tracer provider, span processors, and resource
│    attributes, as well as background threads for media uploads and score ingestion.
│
│    The tracer is responsible for:
│    1. Setting up the OpenTelemetry tracer with appropriate sampling and configuration
│    2. Managing the span processor for exporting spans to the Langfuse API
⋮
│    @staticmethod
│    def get_current_span() -> Any:
⋮

langfuse\_client\span.py:
⋮
│class LangfuseObservationWrapper:
│    """Abstract base class for all Langfuse span types.
│
│    This class provides common functionality for all Langfuse span types, including
│    media processing, attribute management, and scoring. It wraps an OpenTelemetry
│    span and extends it with Langfuse-specific features.
│
│    Attributes:
│        _otel_span: The underlying OpenTelemetry span
│        _langfuse_client: Reference to the parent Langfuse client
│        trace_id: The trace ID for this span
⋮
│    @overload
│    def start_observation(
│        self,
│        *,
│        name: str,
│        as_type: Literal["span"],
│        input: Optional[Any] = None,
│        output: Optional[Any] = None,
│        metadata: Optional[Any] = None,
│        version: Optional[str] = None,
│        level: Optional[SpanLevel] = None,
⋮
│    @overload
│    def start_observation(
│        self,
│        *,
│        name: str,
│        as_type: Literal["generation"],
│        input: Optional[Any] = None,
│        output: Optional[Any] = None,
│        metadata: Optional[Any] = None,
│        version: Optional[str] = None,
│        level: Optional[SpanLevel] = None,
⋮
│    @overload
│    def start_observation(
│        self,
│        *,
│        name: str,
│        as_type: Literal["agent"],
│        input: Optional[Any] = None,
│        output: Optional[Any] = None,
│        metadata: Optional[Any] = None,
│        version: Optional[str] = None,
│        level: Optional[SpanLevel] = None,
⋮
│    @overload
│    def start_observation(
│        self,
│        *,
│        name: str,
│        as_type: Literal["tool"],
│        input: Optional[Any] = None,
│        output: Optional[Any] = None,
│        metadata: Optional[Any] = None,
│        version: Optional[str] = None,
│        level: Optional[SpanLevel] = None,
⋮
│    @overload
│    def start_observation(
│        self,
│        *,
│        name: str,
│        as_type: Literal["chain"],
│        input: Optional[Any] = None,
│        output: Optional[Any] = None,
│        metadata: Optional[Any] = None,
│        version: Optional[str] = None,
│        level: Optional[SpanLevel] = None,
⋮
│    @overload
│    def start_observation(
│        self,
│        *,
│        name: str,
│        as_type: Literal["retriever"],
│        input: Optional[Any] = None,
│        output: Optional[Any] = None,
│        metadata: Optional[Any] = None,
│        version: Optional[str] = None,
│        level: Optional[SpanLevel] = None,
⋮
│    @overload
│    def start_observation(
│        self,
│        *,
│        name: str,
│        as_type: Literal["evaluator"],
│        input: Optional[Any] = None,
│        output: Optional[Any] = None,
│        metadata: Optional[Any] = None,
│        version: Optional[str] = None,
│        level: Optional[SpanLevel] = None,
⋮
│    @overload
│    def start_observation(
│        self,
│        *,
│        name: str,
│        as_type: Literal["embedding"],
│        input: Optional[Any] = None,
│        output: Optional[Any] = None,
│        metadata: Optional[Any] = None,
│        version: Optional[str] = None,
│        level: Optional[SpanLevel] = None,
⋮
│    @overload
│    def start_observation(
│        self,
│        *,
│        name: str,
│        as_type: Literal["guardrail"],
│        input: Optional[Any] = None,
│        output: Optional[Any] = None,
│        metadata: Optional[Any] = None,
│        version: Optional[str] = None,
│        level: Optional[SpanLevel] = None,
⋮
│    @overload
│    def start_observation(
│        self,
│        *,
│        name: str,
│        as_type: Literal["event"],
│        input: Optional[Any] = None,
│        output: Optional[Any] = None,
│        metadata: Optional[Any] = None,
│        version: Optional[str] = None,
│        level: Optional[SpanLevel] = None,
⋮
│    def start_observation(
│        self,
│        *,
│        name: str,
│        as_type: ObservationTypeLiteral = "span",
│        input: Optional[Any] = None,
│        output: Optional[Any] = None,
│        metadata: Optional[Any] = None,
│        version: Optional[str] = None,
│        level: Optional[SpanLevel] = None,
⋮

langfuse\_client\span_filter.py:
⋮
│def is_langfuse_span(span: ReadableSpan) -> bool:
⋮
│def is_genai_span(span: ReadableSpan) -> bool:
⋮
│def is_known_llm_instrumentor(span: ReadableSpan) -> bool:
⋮

langfuse\_task_manager\media_upload_queue.py:
⋮
│class UploadMediaJob(TypedDict):
⋮

langfuse\_utils\__init__.py:
⋮
│def _create_prompt_context(
│    prompt: typing.Optional[PromptClient] = None,
⋮

langfuse\_utils\environment.py:
⋮
│common_release_envs = [
│    # Render
│    "RENDER_GIT_COMMIT",
│    # GitLab CI
│    "CI_COMMIT_SHA",
│    # CircleCI
│    "CIRCLE_SHA1",
│    # Heroku
│    "SOURCE_VERSION",
│    # Travis CI
⋮
│def get_common_release_envs() -> Optional[str]:
⋮

langfuse\_utils\serializer.py:
⋮
│class EventSerializer(JSONEncoder):
│    _MAX_DEPTH = 20
│
⋮
│    @staticmethod
│    def is_js_safe_integer(value: int) -> bool:
⋮
│def serialize_datetime(v: dt.datetime) -> str:
│    def _serialize_zoned_datetime(v: dt.datetime) -> str:
│        if v.tzinfo is not None and v.tzinfo.tzname(None) == dt.timezone.utc.tzname(
│            None
│        ):
│            # UTC is a special case where we use "Z" at the end instead of "+00:00"
│            return v.isoformat().replace("+00:00", "Z")
│        else:
│            # Delegate to the typical +/- offset format
⋮

langfuse\_version.py:
⋮
│@lru_cache(maxsize=1)
│def get_langfuse_version() -> str:
⋮

langfuse\api\annotation_queues\types\delete_annotation_queue_assignment_response.py:
⋮
│class DeleteAnnotationQueueAssignmentResponse(UniversalBaseModel):
⋮

langfuse\api\annotation_queues\types\delete_annotation_queue_item_response.py:
⋮
│class DeleteAnnotationQueueItemResponse(UniversalBaseModel):
⋮

langfuse\api\annotation_queues\types\paginated_annotation_queue_items.py:
⋮
│class PaginatedAnnotationQueueItems(UniversalBaseModel):
⋮

langfuse\api\annotation_queues\types\paginated_annotation_queues.py:
⋮
│class PaginatedAnnotationQueues(UniversalBaseModel):
⋮

langfuse\api\annotation_queues\types\update_annotation_queue_item_request.py:
⋮
│class UpdateAnnotationQueueItemRequest(UniversalBaseModel):
⋮

langfuse\api\blob_storage_integrations\types\blob_storage_integration_deletion_response.py:
⋮
│class BlobStorageIntegrationDeletionResponse(UniversalBaseModel):
⋮

langfuse\api\blob_storage_integrations\types\blob_storage_integrations_response.py:
⋮
│class BlobStorageIntegrationsResponse(UniversalBaseModel):
⋮

langfuse\api\comments\types\create_comment_response.py:
⋮
│class CreateCommentResponse(UniversalBaseModel):
⋮

langfuse\api\comments\types\get_comments_response.py:
⋮
│class GetCommentsResponse(UniversalBaseModel):
⋮

langfuse\api\commons\errors\access_denied_error.py:
⋮
│class AccessDeniedError(ApiError):
⋮

langfuse\api\commons\errors\method_not_allowed_error.py:
⋮
│class MethodNotAllowedError(ApiError):
⋮

langfuse\api\commons\errors\not_found_error.py:
⋮
│class NotFoundError(ApiError):
⋮

langfuse\api\commons\errors\unauthorized_error.py:
⋮
│class UnauthorizedError(ApiError):
⋮

langfuse\api\commons\types\config_category.py:
⋮
│class ConfigCategory(UniversalBaseModel):
⋮

langfuse\api\commons\types\create_score_value.py:
⋮
│CreateScoreValue = typing.Union[float, str]

langfuse\api\commons\types\map_value.py:
⋮
│MapValue = typing.Union[
│    typing.Optional[str],
│    typing.Optional[int],
│    typing.Optional[float],
│    typing.Optional[bool],
│    typing.Optional[typing.List[str]],
⋮

langfuse\api\commons\types\model_price.py:
⋮
│class ModelPrice(UniversalBaseModel):
⋮

langfuse\api\commons\types\numeric_score.py:
⋮
│class NumericScore(BaseScore):
⋮

langfuse\api\commons\types\numeric_score_v1.py:
⋮
│class NumericScoreV1(BaseScoreV1):
⋮

langfuse\api\commons\types\session_with_traces.py:
⋮
│class SessionWithTraces(Session):
⋮

langfuse\api\core\api_error.py:
⋮
│class ApiError(Exception):
⋮

langfuse\api\core\datetime_utils.py:
⋮
│def serialize_datetime(v: dt.datetime) -> str:
│    """
│    Serialize a datetime including timezone info.
│
│    Uses the timezone info provided if present, otherwise uses the current runtime's timezone info.
│
│    UTC datetimes end in "Z" while all other timezones are represented as offset from UTC, e.g. +05
⋮
│    def _serialize_zoned_datetime(v: dt.datetime) -> str:
⋮

langfuse\api\core\enum.py:
⋮
│if sys.version_info >= (3, 11):
│    from enum import StrEnum
│else:
│
│    class StrEnum(str, enum.Enum):
⋮

langfuse\api\core\force_multipart.py:
⋮
│class ForceMultipartDict(Dict[str, Any]):
⋮

langfuse\api\core\http_response.py:
⋮
│class HttpResponse(Generic[T], BaseHttpResponse):
⋮
│class AsyncHttpResponse(Generic[T], BaseHttpResponse):
⋮

langfuse\api\core\http_sse\_exceptions.py:
⋮
│class SSEError(httpx.TransportError):
⋮

langfuse\api\core\jsonable_encoder.py:
⋮
│def jsonable_encoder(
│    obj: Any, custom_encoder: Optional[Dict[Any, Callable[[Any], Any]]] = None
│) -> Any:
│    custom_encoder = custom_encoder or {}
⋮
│    def fallback_serializer(o: Any) -> Any:
⋮

langfuse\api\core\pydantic_utilities.py:
⋮
│def parse_obj_as(type_: Type[T], object_: Any) -> T:
⋮
│class UniversalBaseModel(pydantic.BaseModel):
│    if IS_PYDANTIC_V2:
│        model_config: ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(  # type: ignore[typeddic
│            # Allow fields beginning with `model_` to be used in the model
│            protected_namespaces=(),
│        )
│
│        @pydantic.model_serializer(mode="plain", when_used="json")  # type: ignore[attr-defined]
│        def serialize_model(self) -> Any:  # type: ignore[name-defined]
│            serialized = self.dict()  # type: ignore[attr-defined]
│            data = {
⋮
│    @classmethod
│    def model_construct(
│        cls: Type["Model"], _fields_set: Optional[Set[str]] = None, **values: Any
⋮
│    def json(self, **kwargs: Any) -> str:
⋮
│    def dict(self, **kwargs: Any) -> Dict[str, Any]:
⋮
│def deep_union_pydantic_dicts(
│    source: Dict[str, Any], destination: Dict[str, Any]
⋮
│def update_forward_refs(model: Type["Model"], **localns: Any) -> None:
⋮

langfuse\api\core\query_encoder.py:
⋮
│def traverse_query_dict(
│    dict_flat: Dict[str, Any], key_prefix: Optional[str] = None
⋮

langfuse\api\core\request_options.py:
⋮
│class RequestOptions(typing.TypedDict, total=False):
⋮

langfuse\api\core\serialization.py:
⋮
│class FieldMetadata:
⋮
│def convert_and_respect_annotation_metadata(
│    *,
│    object_: typing.Any,
│    annotation: typing.Any,
│    inner_type: typing.Optional[typing.Any] = None,
│    direction: typing.Literal["read", "write"],
⋮
│def _convert_mapping(
│    object_: typing.Mapping[str, object],
│    expected_type: typing.Any,
│    direction: typing.Literal["read", "write"],
⋮
│def _get_annotation(type_: typing.Any) -> typing.Optional[typing.Any]:
⋮
│def _remove_annotations(type_: typing.Any) -> typing.Any:
⋮
│def _get_alias_to_field_name(
│    field_to_hint: typing.Dict[str, typing.Any],
⋮
│def _get_field_to_alias_name(
│    field_to_hint: typing.Dict[str, typing.Any],
⋮
│def _get_alias_from_type(type_: typing.Any) -> typing.Optional[str]:
⋮
│def _alias_key(
│    key: str,
│    type_: typing.Any,
│    direction: typing.Literal["read", "write"],
│    aliases_to_field_names: typing.Dict[str, str],
⋮

langfuse\api\dataset_items\types\delete_dataset_item_response.py:
⋮
│class DeleteDatasetItemResponse(UniversalBaseModel):
⋮

langfuse\api\dataset_items\types\paginated_dataset_items.py:
⋮
│class PaginatedDatasetItems(UniversalBaseModel):
⋮

langfuse\api\dataset_run_items\types\paginated_dataset_run_items.py:
⋮
│class PaginatedDatasetRunItems(UniversalBaseModel):
⋮

langfuse\api\datasets\types\delete_dataset_run_response.py:
⋮
│class DeleteDatasetRunResponse(UniversalBaseModel):
⋮

langfuse\api\datasets\types\paginated_dataset_runs.py:
⋮
│class PaginatedDatasetRuns(UniversalBaseModel):
⋮

langfuse\api\datasets\types\paginated_datasets.py:
⋮
│class PaginatedDatasets(UniversalBaseModel):
⋮

langfuse\api\health\types\health_response.py:
⋮
│class HealthResponse(UniversalBaseModel):
⋮

langfuse\api\ingestion\types\base_event.py:
⋮
│class BaseEvent(UniversalBaseModel):
⋮

langfuse\api\ingestion\types\create_event_body.py:
⋮
│class CreateEventBody(OptionalObservationBody):
⋮

langfuse\api\ingestion\types\create_event_event.py:
⋮
│class CreateEventEvent(BaseEvent):
⋮

langfuse\api\ingestion\types\create_generation_event.py:
⋮
│class CreateGenerationEvent(BaseEvent):
⋮

langfuse\api\ingestion\types\create_observation_event.py:
⋮
│class CreateObservationEvent(BaseEvent):
⋮

langfuse\api\ingestion\types\create_span_event.py:
⋮
│class CreateSpanEvent(BaseEvent):
⋮

langfuse\api\ingestion\types\ingestion_error.py:
⋮
│class IngestionError(UniversalBaseModel):
⋮

langfuse\api\ingestion\types\ingestion_response.py:
⋮
│class IngestionResponse(UniversalBaseModel):
⋮

langfuse\api\ingestion\types\ingestion_success.py:
⋮
│class IngestionSuccess(UniversalBaseModel):
⋮

langfuse\api\ingestion\types\score_event.py:
⋮
│class ScoreEvent(BaseEvent):
⋮

langfuse\api\ingestion\types\sdk_log_body.py:
⋮
│class SdkLogBody(UniversalBaseModel):
⋮

langfuse\api\ingestion\types\sdk_log_event.py:
⋮
│class SdkLogEvent(BaseEvent):
⋮

langfuse\api\ingestion\types\trace_event.py:
⋮
│class TraceEvent(BaseEvent):
⋮

langfuse\api\ingestion\types\update_event_body.py:
⋮
│class UpdateEventBody(OptionalObservationBody):
⋮

langfuse\api\ingestion\types\update_generation_event.py:
⋮
│class UpdateGenerationEvent(BaseEvent):
⋮

langfuse\api\ingestion\types\update_observation_event.py:
⋮
│class UpdateObservationEvent(BaseEvent):
⋮

langfuse\api\ingestion\types\update_span_event.py:
⋮
│class UpdateSpanEvent(BaseEvent):
⋮

langfuse\api\legacy\metrics_v1\types\metrics_response.py:
⋮
│class MetricsResponse(UniversalBaseModel):
⋮

langfuse\api\legacy\observations_v1\types\observations.py:
⋮
│class Observations(UniversalBaseModel):
⋮

langfuse\api\legacy\observations_v1\types\observations_views.py:
⋮
│class ObservationsViews(UniversalBaseModel):
⋮

langfuse\api\legacy\score_v1\types\create_score_response.py:
⋮
│class CreateScoreResponse(UniversalBaseModel):
⋮

langfuse\api\llm_connections\types\delete_llm_connection_response.py:
⋮
│class DeleteLlmConnectionResponse(UniversalBaseModel):
⋮

langfuse\api\llm_connections\types\paginated_llm_connections.py:
⋮
│class PaginatedLlmConnections(UniversalBaseModel):
⋮

langfuse\api\metrics\types\metrics_v2response.py:
⋮
│class MetricsV2Response(UniversalBaseModel):
⋮

langfuse\api\models\types\paginated_models.py:
⋮
│class PaginatedModels(UniversalBaseModel):
⋮

langfuse\api\observations\types\observations_v2meta.py:
⋮
│class ObservationsV2Meta(UniversalBaseModel):
⋮

langfuse\api\observations\types\observations_v2response.py:
⋮
│class ObservationsV2Response(UniversalBaseModel):
⋮

langfuse\api\opentelemetry\types\otel_attribute.py:
⋮
│class OtelAttribute(UniversalBaseModel):
⋮

langfuse\api\opentelemetry\types\otel_resource.py:
⋮
│class OtelResource(UniversalBaseModel):
⋮

langfuse\api\opentelemetry\types\otel_scope.py:
⋮
│class OtelScope(UniversalBaseModel):
⋮

langfuse\api\opentelemetry\types\otel_scope_span.py:
⋮
│class OtelScopeSpan(UniversalBaseModel):
⋮

langfuse\api\opentelemetry\types\otel_trace_response.py:
⋮
│class OtelTraceResponse(UniversalBaseModel):
⋮

langfuse\api\organizations\types\memberships_response.py:
⋮
│class MembershipsResponse(UniversalBaseModel):
⋮

langfuse\api\organizations\types\organization_projects_response.py:
⋮
│class OrganizationProjectsResponse(UniversalBaseModel):
⋮

langfuse\api\projects\types\api_key_deletion_response.py:
⋮
│class ApiKeyDeletionResponse(UniversalBaseModel):
⋮

langfuse\api\projects\types\organization.py:
⋮
│class Organization(UniversalBaseModel):
⋮

langfuse\api\projects\types\project_deletion_response.py:
⋮
│class ProjectDeletionResponse(UniversalBaseModel):
⋮

langfuse\api\projects\types\projects.py:
⋮
│class Projects(UniversalBaseModel):
⋮

langfuse\api\prompts\types\chat_prompt.py:
⋮
│class ChatPrompt(BasePrompt):
⋮

langfuse\api\prompts\types\prompt_meta_list_response.py:
⋮
│class PromptMetaListResponse(UniversalBaseModel):
⋮

langfuse\api\prompts\types\text_prompt.py:
⋮
│class TextPrompt(BasePrompt):
⋮

langfuse\api\scim\types\empty_response.py:
⋮
│class EmptyResponse(UniversalBaseModel):
⋮

langfuse\api\scim\types\schema_resource.py:
⋮
│class SchemaResource(UniversalBaseModel):
⋮

langfuse\api\scim\types\scim_email.py:
⋮
│class ScimEmail(UniversalBaseModel):
⋮

langfuse\api\scim\types\scim_feature_support.py:
⋮
│class ScimFeatureSupport(UniversalBaseModel):
⋮

langfuse\api\scim\types\scim_name.py:
⋮
│class ScimName(UniversalBaseModel):
⋮

langfuse\api\score_configs\types\score_configs.py:
⋮
│class ScoreConfigs(UniversalBaseModel):
⋮

langfuse\api\scores\types\get_scores_response.py:
⋮
│class GetScoresResponse(UniversalBaseModel):
⋮

langfuse\api\scores\types\get_scores_response_data_boolean.py:
⋮
│class GetScoresResponseDataBoolean(BooleanScore):
⋮

langfuse\api\scores\types\get_scores_response_data_categorical.py:
⋮
│class GetScoresResponseDataCategorical(CategoricalScore):
⋮

langfuse\api\scores\types\get_scores_response_data_correction.py:
⋮
│class GetScoresResponseDataCorrection(CorrectionScore):
⋮

langfuse\api\scores\types\get_scores_response_data_numeric.py:
⋮
│class GetScoresResponseDataNumeric(NumericScore):
⋮

langfuse\api\scores\types\get_scores_response_data_text.py:
⋮
│class GetScoresResponseDataText(TextScore):
⋮

langfuse\api\scores_v3\types\boolean_score_v3.py:
⋮
│class BooleanScoreV3(BaseScoreV3):
⋮

langfuse\api\scores_v3\types\categorical_score_v3.py:
⋮
│class CategoricalScoreV3(BaseScoreV3):
⋮

langfuse\api\scores_v3\types\correction_score_v3.py:
⋮
│class CorrectionScoreV3(BaseScoreV3):
⋮

langfuse\api\scores_v3\types\get_scores_v3meta.py:
⋮
│class GetScoresV3Meta(UniversalBaseModel):
⋮

langfuse\api\scores_v3\types\get_scores_v3response.py:
⋮
│class GetScoresV3Response(UniversalBaseModel):
⋮

langfuse\api\scores_v3\types\numeric_score_v3.py:
⋮
│class NumericScoreV3(BaseScoreV3):
⋮

langfuse\api\scores_v3\types\score_subject_experiment_v3.py:
⋮
│class ScoreSubjectExperimentV3(UniversalBaseModel):
⋮

langfuse\api\scores_v3\types\score_subject_session_v3.py:
⋮
│class ScoreSubjectSessionV3(UniversalBaseModel):
⋮

langfuse\api\scores_v3\types\score_subject_trace_v3.py:
⋮
│class ScoreSubjectTraceV3(UniversalBaseModel):
⋮

langfuse\api\scores_v3\types\text_score_v3.py:
⋮
│class TextScoreV3(BaseScoreV3):
⋮

langfuse\api\sessions\types\paginated_sessions.py:
⋮
│class PaginatedSessions(UniversalBaseModel):
⋮

langfuse\api\trace\types\delete_trace_response.py:
⋮
│class DeleteTraceResponse(UniversalBaseModel):
⋮

langfuse\api\trace\types\sort.py:
⋮
│class Sort(UniversalBaseModel):
⋮

langfuse\api\trace\types\traces.py:
⋮
│class Traces(UniversalBaseModel):
⋮

langfuse\api\unstable\commons\types\array_options_evaluation_rule_filter.py:
⋮
│class ArrayOptionsEvaluationRuleFilter(UniversalBaseModel):
⋮

langfuse\api\unstable\commons\types\boolean_evaluation_rule_filter.py:
⋮
│class BooleanEvaluationRuleFilter(UniversalBaseModel):
⋮

langfuse\api\unstable\commons\types\category_options_evaluation_rule_filter.py:
⋮
│class CategoryOptionsEvaluationRuleFilter(UniversalBaseModel):
⋮

langfuse\api\unstable\commons\types\date_time_evaluation_rule_filter.py:
⋮
│class DateTimeEvaluationRuleFilter(UniversalBaseModel):
⋮

langfuse\api\unstable\commons\types\evaluator_model_config.py:
⋮
│class EvaluatorModelConfig(UniversalBaseModel):
⋮

langfuse\api\unstable\commons\types\evaluator_output_field_definition.py:
⋮
│class EvaluatorOutputFieldDefinition(UniversalBaseModel):
⋮

langfuse\api\unstable\commons\types\null_evaluation_rule_filter.py:
⋮
│class NullEvaluationRuleFilter(UniversalBaseModel):
⋮

langfuse\api\unstable\commons\types\number_evaluation_rule_filter.py:
⋮
│class NumberEvaluationRuleFilter(UniversalBaseModel):
⋮

langfuse\api\unstable\commons\types\number_object_evaluation_rule_filter.py:
⋮
│class NumberObjectEvaluationRuleFilter(UniversalBaseModel):
⋮

langfuse\api\unstable\commons\types\string_evaluation_rule_filter.py:
⋮
│class StringEvaluationRuleFilter(UniversalBaseModel):
⋮

langfuse\api\unstable\commons\types\string_object_evaluation_rule_filter.py:
⋮
│class StringObjectEvaluationRuleFilter(UniversalBaseModel):
⋮

langfuse\api\unstable\commons\types\string_options_evaluation_rule_filter.py:
⋮
│class StringOptionsEvaluationRuleFilter(UniversalBaseModel):
⋮

langfuse\api\unstable\errors\errors\access_denied_error.py:
⋮
│class AccessDeniedError(ApiError):
⋮

langfuse\api\unstable\errors\errors\method_not_allowed_error.py:
⋮
│class MethodNotAllowedError(ApiError):
⋮

langfuse\api\unstable\errors\errors\not_found_error.py:
⋮
│class NotFoundError(ApiError):
⋮

langfuse\api\unstable\errors\errors\unauthorized_error.py:
⋮
│class UnauthorizedError(ApiError):
⋮

langfuse\api\unstable\errors\types\public_api_error.py:
⋮
│class PublicApiError(UniversalBaseModel):
⋮

langfuse\api\unstable\errors\types\public_api_validation_issue.py:
⋮
│class PublicApiValidationIssue(UniversalBaseModel):
⋮

langfuse\api\unstable\evaluation_rules\types\code_evaluation_rule_evaluator_reference.py:
⋮
│class CodeEvaluationRuleEvaluatorReference(UniversalBaseModel):
⋮

langfuse\api\unstable\evaluation_rules\types\delete_evaluation_rule_response.py:
⋮
│class DeleteEvaluationRuleResponse(UniversalBaseModel):
⋮

langfuse\api\unstable\evaluation_rules\types\evaluation_rule_evaluator.py:
⋮
│class EvaluationRuleEvaluator(UniversalBaseModel):
⋮

langfuse\api\unstable\evaluation_rules\types\evaluation_rule_evaluator_reference.py:
⋮
│class EvaluationRuleEvaluatorReference(UniversalBaseModel):
⋮

langfuse\api\unstable\evaluation_rules\types\evaluation_rules.py:
⋮
│class EvaluationRules(UniversalBaseModel):
⋮

langfuse\api\unstable\evaluation_rules\types\llm_as_judge_evaluation_rule_evaluator_reference.py:
⋮
│class LlmAsJudgeEvaluationRuleEvaluatorReference(UniversalBaseModel):
⋮

langfuse\api\unstable\evaluation_rules\types\update_evaluation_rule_request.py:
⋮
│class UpdateEvaluationRuleRequest(UniversalBaseModel):
⋮

langfuse\api\unstable\evaluators\raw_client.py:
⋮
│class RawEvaluatorsClient:
│    def __init__(self, *, client_wrapper: SyncClientWrapper):
⋮
│    def get(
│        self,
│        evaluator_id: str,
│        *,
│        request_options: typing.Optional[RequestOptions] = None,
⋮
│class AsyncRawEvaluatorsClient:
│    def __init__(self, *, client_wrapper: AsyncClientWrapper):
⋮
│    async def get(
│        self,
│        evaluator_id: str,
│        *,
│        request_options: typing.Optional[RequestOptions] = None,
⋮

langfuse\api\unstable\evaluators\types\delete_evaluator_response.py:
⋮
│class DeleteEvaluatorResponse(UniversalBaseModel):
⋮

langfuse\api\unstable\evaluators\types\evaluators.py:
⋮
│class Evaluators(UniversalBaseModel):
⋮

langfuse\langchain\CallbackHandler.py:
⋮
│class _PendingResumeTraceContextStore:
│    def __init__(self, max_size: int) -> None:
│        self._max_size = max_size
⋮
│    def keys(self) -> List[str]:
⋮

langfuse\media.py:
⋮
│class LangfuseMedia:
│    """A class for wrapping media objects for upload to Langfuse.
│
│    This class handles the preparation and formatting of media content for Langfuse,
│    supporting both base64 data URIs and raw content bytes.
│
│    Args:
│        obj (Optional[object]): The source object to be wrapped. Can be accessed via the `obj` attr
│        base64_data_uri (Optional[str]): A base64-encoded data URI containing the media content
│            and content type (e.g., "data:image/jpeg;base64,/9j/4AAQ...").
│        content_type (Optional[str]): The MIME type of the media content when providing raw bytes.
⋮
│    @staticmethod
│    def parse_reference_string(reference_string: str) -> ParsedMediaReference:
⋮

langfuse\openai.py:
⋮
│@dataclass
│class OpenAiDefinition:
⋮
│class OpenAiArgsExtractor:
│    def __init__(
│        self,
│        metadata: Optional[Any] = None,
│        name: Optional[str] = None,
│        langfuse_prompt: Optional[
│            Any
│        ] = None,  # we cannot use prompt because it's an argument of the old OpenAI completions AP
│        langfuse_public_key: Optional[str] = None,
│        trace_id: Optional[str] = None,
│        parent_observation_id: Optional[str] = None,
⋮
│    def get_langfuse_args(self) -> Any:
⋮
│    def get_openai_args(self) -> Any:
⋮

langfuse\types.py:
⋮
│SpanLevel = Literal["DEBUG", "DEFAULT", "WARNING", "ERROR"]
│
│ScoreDataType = Literal["NUMERIC", "CATEGORICAL", "BOOLEAN", "TEXT", "CORRECTION"]
│
⋮
│ExperimentScoreType = Literal["NUMERIC", "CATEGORICAL", "BOOLEAN"]
│
⋮
│class MaskFunction(Protocol):
│    """A function that masks data.
│
│    Keyword Args:
│        data: The data to mask.
│
│    Returns:
│        The masked data that must be serializable to JSON.
⋮
│    def __call__(self, *, data: Any, **kwargs: Dict[str, Any]) -> Any: ...
│
⋮
│class MaskOtelSpansFunction(Protocol):
│    """Function protocol for export-stage OpenTelemetry span masking.
│
│    `mask_otel_spans` runs after Langfuse decides which spans this client should
│    export and after export-stage media handling has converted supported media
│    payloads into Langfuse media references. It affects only the spans exported
│    by this Langfuse client. If the same OpenTelemetry spans are sent to another
│    exporter, that exporter receives its own unmodified copy.
│
│    The function is synchronous. It usually runs on the OpenTelemetry batch span
│    processor worker thread; during `flush()` and shutdown it may run on the
⋮
│    def __call__(
│        self, *, params: MaskOtelSpansParams
⋮
│class ParsedMediaReference(TypedDict):
⋮
│class TraceContext(TypedDict):
⋮

tests\unit\test_openai_prompt_extraction.py:
⋮
│def test_openai_value_serialization_fallback_stays_json_safe():
│    class UnknownLeaf:
│        def __str__(self):
⋮
│    class FallbackModel(BaseModel):
│        created_at: datetime
⋮
│        def model_dump(self, *args, **kwargs):
⋮

tests\unit\test_version.py:
⋮
│def test_package_version_matches_distribution_metadata():
⋮
```
