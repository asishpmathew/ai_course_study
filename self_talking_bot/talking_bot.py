import os

from openai import OpenAI
from dotenv import load_dotenv



phi3_model = "phi3:3.8b"
llama_model = "llama3.2"

phi_system = "You are a chatbot who is very informative about geopolitics. Now US and Iran war happens. You have to comment it mindfully about the powers"

llama_system = "You are supporting Iran side"

phi_messages = ["The war is going on"]
llama_messages = ["We will win"]

load_dotenv(override=True)
base_url = os.getenv('BASE_URL')
token=os.getenv('OPENAI_API_KEY')

ollama = OpenAI(base_url=base_url, api_key=token)
print(ollama.models.list())

def call_phi():
    messages=[{"role":"system", "content":phi_system}]
    for phi, llama in zip(phi_messages,llama_messages):
        messages.append({"role":"user", "content":phi})
        messages.append({"role":"assistant", "content":llama})
    response =ollama.chat.completions.create(model=phi3_model, messages=messages)
    return response.choices[0].message.content

def call_llama():
    messages=[{"role":"system", "content":llama_system}]
    for phi, llama in zip(phi_messages,llama_messages):
        messages.append({"role":"user", "content":llama})
        messages.append({"role":"assistant", "content":phi})
    response =ollama.chat.completions.create(model=llama_model, messages=messages)
    return response.choices[0].message.content

if (__name__=="__main__"):
    for i in range(1,5):
        phi_msg =call_phi()
        phi_messages.append(phi_msg)
        print(f"## PHI MESSAGE ###{phi_msg}")

        llama_msg =call_llama()
        llama_messages.append(llama_msg)
        print(f"## LLAMA MESSAGE ###{llama_msg}")