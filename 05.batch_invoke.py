import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate


load_dotenv(override=True)
openai_api_key = os.getenv("OPEN_API_KEY")

model = ChatOpenAI(
    base_url="https://api.openai-proxy.org/v1",
    api_key=openai_api_key,
    model="gpt-4",  # 或者 gpt-3.5-turbo
    # temperature=0.3,  # 可调
)

# 问题列表
questions = [
    "什么是LangChain？",
    "Python的生成器是做什么的？",
    "解释一下Docker和Kubernetes的关系",
]
# 批量调用大模型
response = model.batch(questions)
for q, r in zip(questions, response):
    print(f"问题：{q}\n回答：{r}\n")
