import os
import json
from dotenv import load_dotenv
from IPython.display import Markdown, display, update_display
from web_scrapper.scraper import fetch_website_links, fetch_website_contents
from openai import OpenAI
import httpx
import traceback


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
Please decide which of these are relevant web links for a brochure about the company, include blog posts, linkdin, twitter profile links
respond with the full https URL in JSON format.
Do not include Terms of Service, Privacy, email links.

Links (some might be relative links):

"""
    links = fetch_website_links(url)
    links = filter_valid_links(links)
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

def fetch_page_and_relevant_links(url):
    content = fetch_website_contents(url)
    print(f"website content fetched. url:{url}")
    links = select_relevant_links(url)
    valid_links = [link for link in links['links'] if link.get('url')]
    print(f"total links retrieved. size: {len(valid_links)} ")
    print(f'valid links {valid_links}')
    result = f"### landing page: \n\n{content} ## Relevant links:\n"
    for link in links['links']:
        result += f"\n {link['type']} \n"
        result += fetch_website_contents(link['url'])
    return result

brochure_system_prompt = """
You are an assistant that analyzes the contents of several relevant pages from a company website
and creates a short brochure about the company for prospective customers, investors and recruits.
Respond in markdown without code blocks.
Include details of company culture, customers and careers/jobs if you have the information.
"""

def get_brochure_user_prompt(company_name, url):
    user_prompt = f"""
You are looking at a company called: {company_name}
Here are the contents of its landing page and other relevant pages;
use this information to build a short brochure of the company in markdown without code blocks.\n\n
"""
    user_prompt += fetch_page_and_relevant_links(url)
    user_prompt = user_prompt[:10_000] # Truncate if more than 5,000 characters
    return user_prompt

def create_brochure(company_name, url):
    user_prompt = get_brochure_user_prompt(company_name, url)
    response = ollama.chat.completions.create(
        model="llama3.2",
        messages=[
            {"role": "system", "content": brochure_system_prompt},
            {"role": "user", "content": user_prompt}
        ],
    )
    result = response.choices[0].message.content
    return result

def stream_brochure(company_name, url, model):
    yield f"Generating brochure for **{company_name}**...\n\n"
    user_prompt = get_brochure_user_prompt(company_name, url)
    stream = ollama.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": brochure_system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        stream= True
    )
    result = ""

    for chunk in stream:
        if chunk.choices[0].delta.content:
            content = chunk.choices[0].delta.content
            print(content, end="", flush=True)   # live output
            result += content
            yield result

def filter_valid_links(links):
    valid_links=[]
    with httpx.Client(timeout= 5, follow_redirects=True) as client:
        for link in links:
            try:
                response = client.head(link)
                if response.status_code < 400:
                    valid_links.append(link)
            except Exception as e:
                pass
    return valid_links


           
               
        


if __name__ == "__main__":
    #print(create_brochure("Asish P Mathew", "https://asishpmathew.github.io/"))
    stream_brochure("Asish P Mathew", "https://asishpmathew.github.io/", "llama3.2")

