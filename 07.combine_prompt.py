from langchain_core.prompts import PromptTemplate

# # 创建一个PromptTemplate模板，用于生成介绍某个主题的提示词
# # 该模板包含两个占位符：topic（主题）和length（字数限制）
# template1 = (
#     PromptTemplate.from_template("请用一句话介绍{topic}，要求通俗易懂\n")
#     + "内容不超过{length}个字"
# )
# # 使用format方法填充模板中的占位符，生成具体的提示词
# prompt1 = template1.format(topic="LangChain", length=20)
# print(prompt1)

# # 分别创建两个独立的PromptTemplate模板
# prompt_a = PromptTemplate.from_template("请用一句话介绍{topic}，要求通俗易懂\n")
# prompt_b = PromptTemplate.from_template("内容不超过{length}个字")
# # 将两个模板进行拼接组合
# prompt_all = prompt_a + prompt_b
# # 填充组合后模板的占位符，生成最终的提示词
# prompt2 = prompt_all.format(topic="LangChain", length=20)
# print(prompt2)


# # 创建一个PromptTemplate对象，用于生成格式化的提示词模板
# # 模板包含两个占位符：{role}表示角色，{question}表示问题
# template = PromptTemplate.from_template(
#     "你是一个专业的{role}工程师，请回答我的问题给出回答，我的问题是：{question}"
# )

# # 使用指定的角色和问题参数来格式化模板，生成最终的提示词字符串
# # role: 工程师角色描述
# # question: 具体的技术问题
# prompt = template.format(role="python开发", question="冒泡排序怎么写？")

# # 输出生成的提示词
# print(prompt)
# print(type(prompt))


# 创建一个PromptTemplate对象，用于生成格式化的提示词模板
# 模板中包含两个占位符：{role}表示角色，{question}表示问题
template = PromptTemplate.from_template(
    "你是一个专业的{role}工程师，请回答我的问题给出回答，我的问题是：{question}"
)

# 使用invoke方法填充模板中的占位符，生成具体的提示词
# 参数：字典类型，包含role和question两个键值对
# 返回值：PromptValue对象，包含了格式化后的提示词
prompt = template.invoke({"role": "python开发", "question": "冒泡排序怎么写？"})

# 打印PromptValue对象及其类型
print(prompt)
print(type(prompt))

# 将PromptValue对象转换为字符串并打印
# to_string()方法将PromptValue转换为可读的字符串格式
print(prompt.to_string())
print(type(prompt.to_string()))
