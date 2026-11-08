from fastapi import FastAPI, HTTPException
from openai import RateLimitError

from app.ai_services import get_meal_analysis
from app.schemas import MealAnalysis, MealAnalysisRequest


app = FastAPI()


@app.post("/analyze", response_model=MealAnalysis)
def analyze_meal(request: MealAnalysisRequest):
    try:
        return get_meal_analysis(request.meal_description)
    except RateLimitError:
        raise HTTPException(
            status_code=503,
            detail="Meal analysis is unavailable right now",
        )
