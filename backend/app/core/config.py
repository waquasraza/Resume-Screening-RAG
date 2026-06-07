from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print("API KEY FOUND:", OPENAI_API_KEY is not None)