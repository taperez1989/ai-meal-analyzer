# AI Meal Analyzer
AI Meal Analyzer accepts a meal description and returns estimated calories, protein, carbohydrates, and fat. It provides both a command-line interface and a FastAPI endpoint.

## Setup

Run these commands from the project root in Git Bash.

```bash
py -m venv .venv
source .venv/Scripts/activate
py -m pip install -e ".[dev]"
```

## Run the API locally

```bash
py -m uvicorn app.api:app --reload
```

Open the [interactive API docs](http://127.0.0.1:8000/docs).

## API key

Real meal analysis requires an OpenAI API key. Create a `.env` file in the project root containing:

```dotenv
OPENAI_API_KEY=your_key_here
```

The automated tests use mocks and do not call OpenAI. Never commit a real API key.

## Run the command-line app

```bash
py -m app.main
```

## Run the tests

```bash
py -m pytest -v
```
