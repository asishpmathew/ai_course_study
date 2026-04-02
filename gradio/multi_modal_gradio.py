import os
import tempfile

import gradio as gr
import pyttsx3
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
baseUrl = os.getenv("BASE_URL")
model = os.getenv("MODEL_MIXTRAL")


# Initialize speech engine
engine = pyttsx3.init()

ollama = OpenAI(base_url=baseUrl, api_key="ollama")

system_message = """
You are a helpful assistant. make your response in 100 words
"""

def chat(message):
    messages = [{"role": "system", "content": system_message}] + [{"role": "user", "content": message}]
    response = ollama.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content

def chat_with_audio(message):
    """Process chat message and return both text and audio"""
    # Get text response
    text_response = chat(message)
    
    # Generate audio file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        audio_path = tmp_file.name
    
    engine.save_to_file(text_response, audio_path)
    engine.runAndWait()
    
    return text_response, audio_path

# Create Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Multi-Modal Chat Assistant")
    gr.Markdown("Ask a question and get both text and audio responses!")
    
    with gr.Row():
        input_text = gr.Textbox(label="Your Message", placeholder="Type your message here...")
    
    with gr.Row():
        submit_btn = gr.Button("Submit", variant="primary")
    
    with gr.Row():
        output_text = gr.Textbox(label="Response", lines=5)
    
    with gr.Row():
        audio_output = gr.Audio(autoplay=True)
    
    submit_btn.click(
        fn=chat_with_audio,
        inputs=input_text,
        outputs=[output_text, audio_output]
    )
    
    input_text.submit(
        fn=chat_with_audio,
        inputs=input_text,
        outputs=[output_text, audio_output]
    )

if __name__ == "__main__":
    demo.launch()