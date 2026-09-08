from unittest.mock import MagicMock, patch
from app.ai_services import get_meal_analysis


def test_get_meal_analysis_uses_supplied_client():
    """Use an injected client instead of creating a real OpenAI client."""

    # Arrange: create fake client and define its expected response.
    fake_client = MagicMock()
    fake_client.responses.create.return_value.output_text = "Fake meal analysis"

    # Act: call the function with the fake client to avoid a network request.
    result = get_meal_analysis("toast", fake_client)

    # Assert: verify both the returned result and the outgoing request.
    assert result == "Fake meal analysis"
    fake_client.responses.create.assert_called_once_with(
        model="gpt-5.6-luna",
        input="toast",
    )


def test_get_meal_analysis_creates_client_when_not_supplied():
    """Create an OpenAI client when the caller does not inject one."""

    # Arrange: replace OpenAI with a mock to prevent a real network request.
    with patch("app.ai_services.OpenAI") as mock_openai:
        fake_client = mock_openai.return_value

        fake_client.responses.create.return_value.output_text = "Fake meal analysis"

    # Act: omit the client so the function follows its production branch.
        result = get_meal_analysis("toast")

    # Assert: verify client creation, request details, and returned output.
        mock_openai.assert_called_once_with()
        assert result == "Fake meal analysis"

    fake_client.responses.create.assert_called_once_with(
        model="gpt-5.6-luna",
        input="toast",
    )