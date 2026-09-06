
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def get_meal_analysis(meal_description, client=None):
    # Tests can supply a fake client; production creates the real client.
    if client is None:
        client = OpenAI()

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=meal_description,
    )

    return response.output_text
