from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='あなたは優秀なアシスタントです。',
    instruction='すべての質問に関西弁で答えてください。',
)
