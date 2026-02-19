import os
from dotenv import load_dotenv
from scraper import fetch_website_contents
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")

#openai = OpenAI()
ollama = OpenAI(base_url="http://9.46.101.215:8085/v1", api_key="ollama")

system_prompt = """
You are a snarky assistant that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""

user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.

"""


def message_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website},
    ]

def summarize_url(url):
    website = fetch_website_contents(url)
    #response = openai.chat.completions.create(model="gpt-5-nano", messages=website)
    response = ollama.chat.completions.create(model="llama3.2", messages=message_for(website))
    #print(response.json())
    #print("_______")
    return response.choices[0].message.content

def main():
    res= summarize_url("https://edwarddonner.com")
    print(res)


if __name__ == "__main__":
    main()