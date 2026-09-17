from unittest.mock import MagicMock, patch
from app.ai_services import get_meal_analysis
from app.schemas import MealAnalysis


def test_get_meal_analysis_uses_supplied_client():
    """Use an injected client instead of creating a real OpenAI client."""

    # Arrange: create fake client and define its expected response.
    fake_client = MagicMock()
    fake_analysis = MealAnalysis(
        name="toast",
        estimated_calories=150,
        protein_grams=4.0,
        carbohydrate_grams=28.0,
        fat_grams=2.0,
    )
    fake_client.responses.parse.return_value.output_parsed = fake_analysis

    # Act: call the function with the fake client to avoid a network request.
    result = get_meal_analysis("toast", fake_client)

    # Assert: verify both the returned result and the outgoing request.
    assert result == fake_analysis
    fake_client.responses.parse.assert_called_once_with(
        model="gpt-5.6-luna",
        input="toast",
        text_format=MealAnalysis,
    )


def test_get_meal_analysis_creates_client_when_not_supplied():
    """Create an OpenAI client when the caller does not inject one."""

    # Arrange: replace OpenAI with a mock to prevent a real network request.
    with patch("app.ai_services.OpenAI") as mock_openai:
        fake_client = mock_openai.return_value
        fake_analysis = MealAnalysis(
            name="toast",
            estimated_calories=150,
            protein_grams=4.0,
            carbohydrate_grams=28.0,
            fat_grams=2.0,
        )

        fake_client.responses.parse.return_value.output_parsed = fake_analysis

        # Act: omit the client so the function follows its production branch.
        result = get_meal_analysis("toast")

        # Assert: verify client creation, request details, and returned output.
        mock_openai.assert_called_once_with()
        assert result == fake_analysis

    fake_client.responses.parse.assert_called_once_with(
        model="gpt-5.6-luna",
        input="toast",
        text_format=MealAnalysis,
        )