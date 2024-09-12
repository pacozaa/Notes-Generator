from openai import OpenAI
import os
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)
model="gpt-4o-mini"