from langchain_core.prompts import ChatPromptTemplate

# # 创建聊天提示模板，包含系统角色设定、用户询问和AI回答的对话历史
# # 以及用户当前输入的占位符
# prompt_template = ChatPromptTemplate(
#     [
#         ("system", "你是一个AI助手，你的名字是{name}"),
#         ("human", "你能做什么事"),
#         ("ai", "我可以陪你聊天，讲笑话，写代码"),
#         ("human", "{user_input}"),
#     ]
# )

# # 使用指定的参数格式化提示模板，生成最终的提示字符串
# # name: AI助手的名称
# # user_input: 用户的当前输入
# prompt = prompt_template.format(name="小张", user_input="你可以做什么")
# print(prompt)


# # 创建聊天提示模板，包含系统角色设定和用户问题格式
# # 系统消息定义了AI的角色，人类消息定义了问题的输入格式
# chat_prompt = ChatPromptTemplate.from_messages(
#     [("system", "你是一个{role}，请回答我提出的问题"), ("human", "请回答:{question}")]
# )

# # 使用指定的角色和问题参数填充模板，生成具体的提示内容
# # role: 指定AI扮演的角色
# # question: 用户提出的具体问题
# prompt_value = chat_prompt.invoke(
#     {"role": "python开发工程师", "question": "冒泡排序怎么写"}
# )

# # 输出生成的提示内容
# print(prompt_value.to_string())


# 创建聊天提示模板，包含系统角色设定和用户问题格式
# 系统消息定义了AI助手的角色，人类消息定义了用户问题的格式
chat_prompt = ChatPromptTemplate.from_messages(
    [("system", "你是一个{role}，请回答我提出的问题"), ("human", "请回答:{question}")]
)

# 格式化聊天提示模板，填充角色和问题参数
# 参数role: 指定AI助手的角色身份
# 参数question: 用户提出的具体问题
# 返回值: 格式化后的消息列表
prompt_value = chat_prompt.format_messages(
    role="python开发工程师", question="冒泡排序怎么写"
)

# 打印格式化后的提示消息
print(prompt_value)
