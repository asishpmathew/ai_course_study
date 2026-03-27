import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

from brochure.brochure import stream_brochure

load_dotenv(override=True)


ollama = OpenAI(base_url="http://9.46.101.215:8085/v1", api_key="ollama")

def stream_llama(prompt, model):
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
      ]
    stream = ollama.chat.completions.create(
        model=model,
        messages=messages,
        stream=True
    )
    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result


system_message = "You are a helpful assistant that responds in markdown without code blocks"

message_input = gr.Textbox(label="Your message:", info="Enter a message for llama3.2/phi3", lines=7)
model_selector = gr.Dropdown(["llama3.2", "phi3:3.8b"], label="Select model", value="llama3.2")
message_output = gr.Markdown(label="Response:")

view = gr.Interface(
    fn=stream_llama,
    title="GPT",
    inputs=[message_input, model_selector],
    outputs=[message_output],
    examples=[
        ["Explain the Transformer architecture to a layperson", "llama3.2"],
        ["Explain the Transformer architecture to an aspiring AI engineer", "phi3:3.8b"]
        ],
    flagging_mode="never"
    )

if __name__ == "__main__":
    #gr.Interface(fn=shout, inputs="textbox", outputs="textbox", flagging_mode="never").launch()
    ##gr.Interface(fn=shout, inputs="textbox", outputs="textbox", flagging_mode="never").launch(share=True)
    view.launch(inbrowser=True)
