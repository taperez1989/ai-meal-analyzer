
from dotenv import load_dotenv
from openai import OpenAI
from app.schemas import MealAnalysis

load_dotenv()


def get_meal_analysis(meal_description, client=None):
    # Tests can supply a fake client; production creates the real client.
    if client is None:
        client = OpenAI()

    response = client.responses.parse(
        model="gpt-5.6-luna",
        input=meal_description,
        text_format=MealAnalysis,
    )

    return response.output_parsed
