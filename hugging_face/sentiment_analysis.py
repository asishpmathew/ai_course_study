import os

from dotenv import load_dotenv
from huggingface_hub import login
from sympy.printing.pytorch import torch
from transformers import pipeline

load_dotenv(override=True)
hf_token = os.getenv("HF_TOKEN")

login(token=hf_token)

# Select device
device = "mps" if torch.backends.mps.is_available() else "cpu"
print(device)

# classifier = pipeline(
#     "sentiment-analysis",
#     device=device
# )

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    device=device,
    token=hf_token
)

result = classifier("I saw a superb movie today")

print(result)