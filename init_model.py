import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(override=True)
openai_api_key = os.getenv("OPEN_API_KEY")
LLM_NAME = "gpt-4.1-mini"

model = ChatOpenAI(
    base_url="https://api.openai-proxy.org/v1",
    api_key=openai_api_key,
    model=LLM_NAME,  # 或者 gpt-3.5-turbo
    # temperature=0.3,  # 可调
)
