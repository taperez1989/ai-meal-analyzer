from unittest.mock import MagicMock
from app.ai_services import get_meal_analysis


def test_get_meal_analysis_uses_supplied_client():
    fake_client = MagicMock()
    fake_client.responses.create.return_value.output_text = "Fake meal analysis"

    result = get_meal_analysis("toast", fake_client)

    assert result == "Fake meal analysis"