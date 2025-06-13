import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_tracing_disabled(disabled=True)

async def main():
    agent = Agent(
        name='Assistant',
        instructions='You only respond in haikus.',
        model=OpenAIChatCompletionsModel(
            model="gemini-2.0-flash",
            openai_client=client
        )
    )

    result = await Runner.run(
        agent,
        "What is agentic AI?",        
    )

    print(f"Result: {result.final_output}")

if __name__ == '__main__':
    asyncio.run(main())
