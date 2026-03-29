from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr
import os
from brochure.brochure import stream_brochure

baseUrl = os.getenv("BASE_URL")

ollama = OpenAI(base_url=baseUrl, api_key="ollama")

name_input = gr.Textbox(label="Company name:")
url_input = gr.Textbox(label="Landing page URL including http:// or https://")
model_selector = gr.Dropdown(
    ["llama3.2", "phi3:3.8b"], label="Select model", value="llama3.2"
)
message_output = gr.Markdown(label="Response*****:")

view = gr.Interface(
    fn=stream_brochure,
    title="Brochure Generator2",
    inputs=[name_input, url_input, model_selector],
    outputs=[message_output],
    examples=[
        ["Hugging Face", "https://huggingface.co", "llama3.2"],
        ["Edward Donner", "https://edwarddonner.com", "phi3:3.8b"],
    ],
    flagging_mode="never",
)


if __name__ == "__main__":
    view.launch(inbrowser=True)
