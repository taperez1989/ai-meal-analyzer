import app.main as main_module
from app.schemas import MealAnalysis


def test_main_displays_analysis(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: "toast")

    fake_analysis = MealAnalysis(
        name="toast",
        estimated_calories=150,
        protein_grams=4.0,
        carbohydrate_grams=28.0,
        fat_grams=2.0,
    )

    # Supply a complete analysis without making an OpenAI API request.
    monkeypatch.setattr(main_module, "get_meal_analysis", lambda meal_description: fake_analysis)

    main_module.main()

    output = capsys.readouterr().out

    assert "Carbohydrates: 28.0 g" in output