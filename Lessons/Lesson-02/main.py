from agents import Agent, Runner, OpenAIChatCompletionsModel,RunConfig, set_tracing_disabled
from openai import AsyncOpenAI
gemini_api_key="<your_api_key>"

client_provider = AsyncOpenAI(
   api_key=gemini_api_key,
   base_url="https://generativelanguage.googleapis.com/v1beta/openai/"

)
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client_provider)
# set_tracing_disabled(True)

config = RunConfig(model=model, model_provider=client_provider,tracing_disabled=True)


agent = Agent(name="Assistant",
               instructions="You are a helpful assistant",
            #    model=model
                 )

result = Runner.run_sync(
    starting_agent=agent,
    input="Write program that sum two numbers and numbers are 10 and 5.",
    run_config=config)

print(result.final_output)