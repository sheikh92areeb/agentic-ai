import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

set_tracing_disabled(True)
set_default_openai_api('chat_completions')

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_default_openai_client(external_client)

agent: Agent = Agent(
    name='Assistant',
    instructions="you are a helpful assistant. You will answer questions and provide information based on the user's requests. If you don't know the answer, say 'I don't know'.",
    model='gemini-2.0-flash'
)

result = Runner.run_sync(
    starting_agent=agent,
    input="What is the simple and best way to designed and plan a project?"
)

print(result.final_output)