from openai import OpenAI
import os
client = OpenAI(
    # This is the default and can be omitted
    # api_key=os.environ.get("OPENAI_API_KEY"),
    # curl https://w2rx8m79w8bce1-11434.proxy.runpod.net/api/tags
    # base_url='http://localhost:11434/v1/',
    # base_url='https://w2rx8m79w8bce1-11434.proxy.runpod.net/v1/',
    # required but ignored
    # api_key='ollama',
)
model="gpt-4o-mini"
# model="phi3.5"