import os
import torch
from dotenv import load_dotenv
from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

load_dotenv(override=True)

hf_token = os.getenv("HF_TOKEN")
login(token=hf_token)

device = "mps" if torch.backends.mps.is_available() else "cpu"

print("Using device:", device)

model_name = "facebook/nllb-200-distilled-600M"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

model.to(device)

text = "I am learning AI"

inputs = tokenizer(
    text,
    return_tensors="pt"
).to(device)

translated_tokens = model.generate(
    **inputs,
    forced_bos_token_id=tokenizer.convert_tokens_to_ids("mal_Mlym"),
    max_length=200
)

result = tokenizer.batch_decode(
    translated_tokens,
    skip_special_tokens=True
)

print(result[0])