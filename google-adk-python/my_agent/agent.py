from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
import os

API_BASE_URL = "http://localhost:4000"
MODEL_NAME = "openai/gemini-2.5-flash"
TOKEN = "sk-supersecretpassword"
os.environ["GEMINI_API_KEY"] = ""

auth_headers = {"Authorization": f"Bearer {TOKEN}"}

root_agent = LlmAgent(
    model=LiteLlm(
        model=MODEL_NAME,
        api_base=API_BASE_URL,
        api_key=TOKEN,
    ),
    name='root_agent',
    description='あなたは優秀なアシスタントです。',
    instruction='すべての質問に関西弁で答えてください。',
)
