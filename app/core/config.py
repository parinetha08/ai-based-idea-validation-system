import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
APP_NAME = os.getenv("APP_NAME", "AI Idea Validator")
