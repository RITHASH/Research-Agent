from dotenv import load_dotenv
import os
import yaml

load_dotenv()

with open("settings.yaml", "r") as file:
    SETTINGS = yaml.safe_load(file)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

MODEL_NAME = SETTINGS["llm"]["model"]
TEMPERATURE = SETTINGS["llm"]["temperature"]

