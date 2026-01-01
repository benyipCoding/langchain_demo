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

# 创建一个PromptTemplate对象，用于生成格式化的提示词模板
# 模板包含两个占位符：{role}表示角色，{question}表示问题
template = PromptTemplate.from_template(
    "你是一个专业的{role}工程师，请回答我的问题给出回答，我的问题是：{question}"
)

# 使用指定的角色和问题参数来格式化模板，生成最终的提示词字符串
# role: 工程师角色描述
# question: 具体的技术问题
prompt = template.format(role="python开发", question="冒泡排序怎么写？")

# 输出生成的提示词
response = model.stream([HumanMessage(content=prompt)])

# 流式打印结果
for chunk in response:
    print(
        chunk.content, end="", flush=True
    )  # 刷新缓冲区 (无换行符，缓冲区未刷新，内容可能不会立即显示)
print("\n")
print(type(response))
