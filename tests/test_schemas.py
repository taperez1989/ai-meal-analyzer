import pytest
from pydantic import ValidationError

from app.schemas import MealAnalysis, MealAnalysisRequest


def test_meal_analysis_accepts_valid_nutrition():
    """Create a meal when every field has the expected type."""

    # Arrange and Act: construct a validated meal-analysis object.
    analysis = MealAnalysis(
        name="toast",
        estimated_calories=150,
        protein_grams=4.0,
        carbohydrate_grams=28.0,
        fat_grams=2.0,
    )

    # Assert: verify Pydantic stored the validated values.
    assert analysis.name == "toast"
    assert analysis.estimated_calories == 150

def test_meal_analysis_rejects_missing_nutrition_data():
    """Reject a meal analysis when a required field is missing."""

    # Act and Assert: expect a validation failure because fat_grams is absent.
    with pytest.raises(ValidationError):
        MealAnalysis(
            name="toast",
            estimated_calories=150,
            protein_grams=4.0,
            carbohydrate_grams=28.0,
        )


def test_meal_request_strips_whitespace():
    """Store a meal description without surrounding spaces."""
    request = MealAnalysisRequest(meal_description="  chicken burrito  ")

    assert request.meal_description == "chicken burrito"


def test_meal_request_rejects_blank_description():
    """Reject a description containing only whitespace."""
    with pytest.raises(ValidationError):
        MealAnalysisRequest(meal_description=" ")
