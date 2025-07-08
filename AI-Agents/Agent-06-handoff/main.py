import os
from dotenv import load_dotenv
from agents import Agent, Runner, handoff, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

set_tracing_disabled(True)
set_default_openai_api('chat_completions')

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_default_openai_client(external_client)

writer_agent = Agent(
    name='Writer',
    instructions='write short essay and story for user',
    model='gemini-2.0-flash'
)

doctor_agent = Agent(
    name='Doctor',
    instructions='suggest user to health tips and medicines',
    model='gemini-2.0-flash'
)


triage_agent = Agent(
    name="Triage Agent",
    instructions="You are main agent answers user's input and if its belong to another specialist handoff to that one don't use your power to answer.",    
    model='gemini-2.0-flash',
    handoffs=[writer_agent, doctor_agent]
)

result = Runner.run_sync(
    starting_agent=triage_agent,
    input='How are you?'
)

print(result)

