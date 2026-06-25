import logging
from unittest import mock
from hypothesis import given, strategies as st

from lume.service import add_otel_context, remove_otel_context


@given(
    st.dictionaries(
        st.text(), st.text() | st.integers() | st.none() | st.floats(allow_nan=False)
    )
)
def test_remove_otel_context_never_crashes(event_dict):
    """
    Property-based test to ensure remove_otel_context handles arbitrary dictionaries
    safely without crashing.
    """
    # Create a copy since hypothesis strategies return values we shouldn't mutate
    # (though remove_otel_context copies internally, good practice)
    input_dict = event_dict.copy()

    result = remove_otel_context(logging.getLogger(), "info", input_dict)

    # Assert keys are gone if they were there
    assert "trace_id" not in result
    assert "span_id" not in result

    # Assert other keys remain
    for key, value in input_dict.items():
        if key not in ("trace_id", "span_id"):
            assert result[key] == value


@mock.patch("lume.service.settings")
@given(
    st.dictionaries(
        st.text(), st.text() | st.integers() | st.none() | st.floats(allow_nan=False)
    )
)
def test_add_otel_context_never_crashes(mock_settings, event_dict):
    """
    Property-based test to ensure add_otel_context handles arbitrary dictionaries
    safely and injects correct context.
    """
    # Arrange
    mock_settings.trace_id = "test_trace_id"
    mock_settings.span_id = "test_span_id"
    input_dict = event_dict.copy()

    with mock.patch("lume.service.trace.get_current_span", return_value=None):
        # Act
        result = add_otel_context(logging.getLogger(), "info", input_dict)

        # Assert
        assert result["trace_id"] == "test_trace_id"
        assert result["span_id"] == "test_span_id"

        # Assert other keys remain
        for key, value in event_dict.items():
            if key not in ("trace_id", "span_id"):
                assert result[key] == value
