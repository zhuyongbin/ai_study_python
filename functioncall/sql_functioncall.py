from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, ToolMessage, SystemMessage
import dotenv
import os
from langchain_openai import ChatOpenAI

from functioncall.sql_function_tools import ask_database,tools

dotenv.load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("DASHSCOPE_API_KEY")
os.environ['OPENAI_BASE_URL'] = os.getenv("BAILIAN_BASE_URL")
init_model = init_chat_model(model_provider="openai", model="qwen3.5-flash", api_key=os.getenv("OPENAI_API_KEY"),
                        base_url=os.getenv("OPENAI_BASE_URL"), )
model = init_model.bind_tools(tools)



if __name__ == '__main__':
    messages = [
        HumanMessage(content="查询一下最高年龄的人的名字,他的年龄是多少"),
        SystemMessage(content="你是一个sql高手,根据所说的自然语言转成sql查询并返回结果")
    ]

    while True:
        model_response = model.invoke(messages)
        if not model_response.tool_calls:
            print("\n✅ 最终回答：")
            print(messages)
            print(model_response.content)
            break
        for tool in model_response.tool_calls:
            print("\n🤖 模型正在执行工具：")
            function_name = tool['name']
            print(tool['name'])
            id_ = tool['id']
            query_sql = tool['args']['query']
            print(tool['args']['query'])
            tool_response = ""
            if function_name == "ask_database":
                tool_response = ask_database(query_sql)
            else:
                tool_response = "不支持此工具"
            messages.append(model_response)
            messages.append(ToolMessage(tool_call_id=id_, content=tool_response))
            model.invoke(messages)
