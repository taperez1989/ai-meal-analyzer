from pydantic import BaseModel


class MealAnalysis(BaseModel):
    name: str
    estimated_calories: int
    protein_grams: float
    carbohydrate_grams: float
    fat_grams: float
