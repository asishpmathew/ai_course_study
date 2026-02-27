import os
import json
from dotenv import load_dotenv
from IPython.display import Markdown, display, update_display
from web_scrapper.scraper import fetch_website_links, fetch_website_contents
from openai import OpenAI


load_dotenv(override=True)
ollama = OpenAI(base_url="http://9.46.101.215:8085/v1", api_key="ollama")

link_system_prompt = """
You are provided with a list of links found on a webpage.
You are able to decide which of the links would be most relevant to include in a brochure about the company,
such as links to an About page, or a Company page, or Careers/Jobs pages.
You should respond in JSON as in this example:

{
    "links": [
        {"type": "about page", "url": "https://full.url/goes/here/about"},
        {"type": "careers page", "url": "https://another.full.url/careers"}
    ]
}
"""

def get_links_user_prompt(url):
    user_prompt = f"""
Here is the list of links on the website {url} -
Please decide which of these are relevant web links for a brochure about the company, include blog posts, linkindin, twitter profile links
respond with the full https URL in JSON format.
Do not include Terms of Service, Privacy, email links.

Links (some might be relative links):

"""
    links = fetch_website_links(url)
    user_prompt += "\n".join(links)
    return user_prompt

def select_relevant_links(url):
    response = ollama.chat.completions.create(
        model="llama3.2",
        messages=[
            {"role": "system", "content": link_system_prompt},
            {"role": "user", "content": get_links_user_prompt(url)}
        ],
        response_format={"type": "json_object"}
    )
    result = response.choices[0].message.content
    links = json.loads(result)
    return links

if __name__ == "__main__":
    print(select_relevant_links("https://edwarddonner.com"))