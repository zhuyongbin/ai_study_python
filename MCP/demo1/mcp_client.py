# Deleted:from mcp.client import MCPClient
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import asyncio
import llm_config


# Deleted:mcp_client = MCPClient("ws://localhost:8000")
# Deleted:mcp_client.connect()

def get_answer(prompt: str) -> str:
    """使用MCP查询数据库并生成答案"""

    async def run_query():
        server_params = StdioServerParameters(
            command="python",
            args=["D:\\pythonSpace\\ai_study_python\\MCP\\demo1\\mcp_server.py"]
        )

        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()

                query = "SELECT * FROM sys_user WHERE name LIKE '%{}%'".format(prompt)
                result = await session.call_tool("query_database", {"query": query})

                messages = [
                    {"role": "system", "content": "你是一个全能的AI助手"},
                    {"role": "user", "content": "根据以下信息回答问题：\n\n{} \n\n问题：{}".format(result, prompt)}
                ]
                response = llm_config.get_init_model().invoke(messages)
                print(response)
                return response.content

    return asyncio.run(run_query())


if __name__ == "__main__":
    user_prompt = input("请输入您的问题：")
    answer = get_answer(user_prompt)
    print(answer)


