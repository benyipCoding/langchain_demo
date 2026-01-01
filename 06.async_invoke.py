import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate
import asyncio


load_dotenv(override=True)
openai_api_key = os.getenv("OPEN_API_KEY")

model = ChatOpenAI(
    base_url="https://api.openai-proxy.org/v1",
    api_key=openai_api_key,
    model="gpt-4",  # 或者 gpt-3.5-turbo
    # temperature=0.3,  # 可调
)


async def main():
    # 异步调用一条请求
    response = await model.ainvoke("解释一下LangChain是什么")
    print(response)


# 运行异步程序的入口点
asyncio.run(main())
