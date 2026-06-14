from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
import gradio as gr

load_dotenv(override=True)
openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

PDF_PATH = Path(__file__).parent / "me" / "linkedin.pdf"
SUMMARY_PATH = Path(__file__).parent / "me" / "summary.txt"
model_name="gemma4:e4b"

name = "Ed Donner" # my name
system_prompt = f"You are acting as {name}. You are answering questions on {name}'s website, \
particularly questions related to {name}'s career, background, skills and experience. \
Your responsibility is to represent {name} for interactions on the website as faithfully as possible. \
You are given a summary of {name}'s background and LinkedIn profile which you can use to answer questions. \
Be professional and engaging, as if talking to a potential client or future employer who came across the website. \
If you don't know the answer, say so."


def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def load_summary(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

summary = load_summary(SUMMARY_PATH)
linkedin = load_pdf(PDF_PATH)
system_prompt += f"\n\n## Summary:\n{summary}\n\n## LinkedIn Profile:\n{linkedin}\n\n"
system_prompt += f"With this context, please chat with the user, always staying in character as {name}."

def chat_with_pdf(user_input):
    pdf_text = load_pdf(PDF_PATH)
    prompt = f"You are a helpful assistant that can answer questions about the following text: {pdf_text}. User: {user_input}"
    response = openai.chat.completions.create(model=model_name, messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content


def chat(message, history):
    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model=model_name, messages=messages)
    return response.choices[0].message.content


if __name__ == "__main__":
    gr.ChatInterface(chat).launch()