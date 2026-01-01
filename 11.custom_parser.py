## 自定义输出解析器

import re
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from loguru import logger
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


# 定义数据模型
class Answer(BaseModel):
    content: str = Field(description="回答内容")
    tags: str = Field(description="标签，格式为《标签1》《标签2》")


# 自定义解析器
class CustomPydanticOutputParser(PydanticOutputParser):
    def parse(self, text: str) -> Answer:
        # 将数组格式转换为《》格式
        tags_match = re.search(r'"tags"\s*:\s*\[(.*?)\]', text, re.DOTALL)
        if tags_match:
            tags_list = re.findall(r'"([^"]+)"', tags_match.group(1))
            tags_string = "".join([f"《{tag}》" for tag in tags_list])
            text = re.sub(
                r'"tags"\s*:\s*\[.*?\]',
                f'"tags": "{tags_string}"',
                text,
                flags=re.DOTALL,
            )
        return super().parse(text)


# 创建解析器
parser = CustomPydanticOutputParser(pydantic_object=Answer)

# 创建提示模板
chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是AI助手，请按JSON格式简短回答\n{format_instructions}"),
        ("human", "{question}"),
    ]
)

# 生成提示
prompt = chat_prompt.invoke(
    {
        "question": "什么是LangChain",
        "format_instructions": parser.get_format_instructions(),
    }
)

# 调用模型
load_dotenv(override=True)
openai_api_key = os.getenv("OPEN_API_KEY")

model = ChatOpenAI(
    base_url="https://api.openai-proxy.org/v1",
    api_key=openai_api_key,
    model="gpt-4.1-mini",  # 或者 gpt-3.5-turbo
    # temperature=0.3,  # 可调
)
result = model.invoke(prompt)

# 解析结果
response = parser.invoke(result)
logger.info(f"回答: {response.content}")
logger.info(f"标签: {response.tags}")
