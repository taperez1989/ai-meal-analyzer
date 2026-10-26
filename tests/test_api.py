from fastapi.testclient import TestClient

import app.api as api_module
from app.schemas import MealAnalysis


def test_analyze_meal_returns_analysis(monkeypatch):
    """Return a structured HTTP response without an OpenAI request."""
    fake_analysis = MealAnalysis(
        name="toast",
        estimated_calories=150,
        protein_grams=4.0,
        carbohydrate_grams=28.0,
        fat_grams=2.0,
    )

    monkeypatch.setattr(
        api_module, "get_meal_analysis", lambda meal_description: fake_analysis
    )
    client = TestClient(api_module.app)

    response = client.post("/analyze", json={"meal_description": "toast"})

    assert response.status_code == 200
    assert response.json() == fake_analysis.model_dump()
