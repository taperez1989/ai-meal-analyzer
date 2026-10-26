from fastapi import FastAPI

from app.ai_services import get_meal_analysis
from app.schemas import MealAnalysis, MealAnalysisRequest


app = FastAPI()


@app.post("/analyze", response_model=MealAnalysis)
def analyze_meal(request: MealAnalysisRequest):
    return get_meal_analysis(request.meal_description)
