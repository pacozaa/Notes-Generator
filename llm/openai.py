from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
import os
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)
model="gpt-4o-mini"