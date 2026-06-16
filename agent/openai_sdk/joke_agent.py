
import asyncio

from dotenv import load_dotenv
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, set_tracing_disabled, trace

load_dotenv(override=True)
set_tracing_disabled(True)


ollama_client = AsyncOpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)
model = OpenAIChatCompletionsModel(
    model="gemma4:e4b",  # or llama3.2, qwen2.5:7b, etc.
    openai_client=ollama_client,
)

agent = Agent(name="Jokester", instructions="You are a joke teller", model=model)


async def main():
    result = await Runner.run(agent, "Tell a joke about Autonomous AI Agents")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())