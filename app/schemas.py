from pydantic import BaseModel, ConfigDict


class MealAnalysis(BaseModel):
    name: str
    estimated_calories: int
    protein_grams: float
    carbohydrate_grams: float
    fat_grams: float


class MealAnalysisRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, str_min_length=1)
    meal_description: str
