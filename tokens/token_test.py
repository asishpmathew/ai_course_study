import tiktoken

encoding= tiktoken.encoding_for_model("gpt-4.1-mini")
tokens= encoding.encode("my name is asish")

for token in tokens:
    print(f"{token}={encoding.decode([token])}")