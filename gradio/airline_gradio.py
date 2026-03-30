import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr
from soupsieve.util import lower

load_dotenv(override=True)
baseUrl = os.getenv("BASE_URL")
model = os.getenv("MODEL_LLAMA_3_2")

ticket_prices = {"london": "$799", "paris": "$899", "tokyo": "$1400", "berlin": "$499"}

def get_ticket_price(destination_city):
    destination = (destination_city or "").lower()
    print(f"Tool called for city {destination}")
    price = ticket_prices.get(destination, "Unknown ticket price")
    return f"The price of a ticket to {destination} is {price}"


ollama = OpenAI(base_url=baseUrl, api_key="ollama")
system_message = """
You are a helpful assistant for an Airline called FlightAI.
Give short, courteous answers, no more than 1 sentence.
Always be accurate. If you don't know the answer, say so.

if you don't know the ticket price after tool calling. Please say, we don't have flight to that country/state
"""



# There's a particular dictionary structure that's required to describe our function:
price_function = {
    "name": "get_ticket_price",
    "description": "Get the price of a return ticket to the destination city.",
    "parameters": {
        "type": "object",
        "properties": {
            "destination_city": {
                "type": "string",
                "description": "The city that the customer wants to travel to",
            },
        },
        "required": ["destination_city"],
        "additionalProperties": False
    }
}

tools = [{"type":"function", "function":price_function}]


def chat(message, history):
    history = [{"role": h["role"], "content": h["content"]} for h in history]
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    response = ollama.chat.completions.create(model=model, messages=messages, tools=tools)

    while response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        responses = handle_tool_calls(message)
        messages.append(message)
        messages.extend(responses)
        response = ollama.chat.completions.create(model=model, messages=messages, tools=tools)

    return response.choices[0].message.content

# We have to write that function handle_tool_call:

def handle_tool_calls(message):
    responses = []
    for tool_call in message.tool_calls:
        if tool_call.function.name == "get_ticket_price":
            arguments = json.loads(tool_call.function.arguments)
            city = arguments.get('destination_city')
            price_details = globals()[tool_call.function.name](city)
            responses.append({
                "role": "tool",
                "content": price_details,
                "tool_call_id": tool_call.id
            })
    return responses

if __name__ =='__main__':
    gr.ChatInterface(fn=chat).launch()