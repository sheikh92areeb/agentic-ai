import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

if not openrouter_api_key:
    raise ValueError("OPENROUTER_API_KEY environment variable is not set.")

external_client = AsyncOpenAI(
    api_key=openrouter_api_key,
    base_url="https://openrouter.ai/api/v1",
)

model = OpenAIChatCompletionsModel(
    model='google/gemini-2.0-flash-exp:free',
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)

agent = Agent(
    name='writer',
    instructions='You are a writer. Write a short stories, poems, or essays based on the given prompts.',
)

response = Runner.run_sync(
    starting_agent=agent,
    input='Write an essay of my favorite hobby.',
    run_config=config,
)

print(response)