import os
from dotenv import load_dotenv
from gradio.themes.builder_app import history
from openai import OpenAI
import gradio as gr

load_dotenv(override=True)
baseUrl = os.getenv("BASE_URL")
model = os.getenv("MODEL_LLAMA_3_2")

ollama = OpenAI(base_url=baseUrl, api_key="ollama")
system_message = (
    "You are a helpful assistant that responds in markdown without code blocks"
)


def chat(message, history):
    histories = [{"role": h["role"], "content": h["content"]} for h in history]
    messages = (
        [{"role": "system", "content": system_message}]
        + histories
        + [{"role": "user", "content": message}]
    )
    stream = ollama.chat.completions.create(model=model, messages=messages, stream=True)
    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result


if __name__ == "__main__":
    gr.ChatInterface(fn=chat).launch()
