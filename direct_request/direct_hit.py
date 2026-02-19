import requests
from dotenv import load_dotenv
import os

load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")

header = { "Authorization": f"Bearer {openai_api_key}", "Content": "application/json"};
payload = {"model": "gpt-5-nano", "messages": [{"role": "user", "content": "tell me a joke"}]};

response = requests.post("https://api.openai.com/v1/chat/completions", json=payload, headers=header);
print(response.json())