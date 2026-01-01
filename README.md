# LangChain Demo

快速演示如何使用 LangChain 调用 OpenAI

步骤：

1. 安装依赖：

```bash
pip install -r requirements.txt
```

2. 在项目根目录创建 `.env` 并设置 `OPENAI_API_KEY`：

```
OPENAI_API_KEY=sk-...
```

或在系统环境变量中设置同名变量。

3. 运行 demo：

```bash
python main.py
```

说明：`main.py` 使用 `langchain` 的 `OpenAI` 封装和 `LLMChain` + `PromptTemplate`，将一段中文翻译为英文并给出摘要。
