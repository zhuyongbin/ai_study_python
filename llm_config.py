import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# 全局只加载一次环境变量
load_dotenv()

def get_init_model():
    """
    封装好的获取 LLM 模型函数
    直接调用就能用，无需重复写配置
    """
    # 从环境变量读取配置
    api_key = os.getenv("DASHSCOPE_API_KEY")
    base_url = os.getenv("BAILIAN_BASE_URL")

    # 初始化模型
    model = init_chat_model(
        model_provider="openai",
        model="qwen3.5-flash",
        api_key=api_key,
        base_url=base_url,
    )
    return model


# 如果你想单例模式（全局只创建一个模型，更高效）
_init_model_instance = None
def get_init_model_singleton():
    """单例模式：全局只创建一个模型实例，推荐使用"""
    global _init_model_instance
    if _init_model_instance is None:
        _init_model_instance = get_init_model()
    return _init_model_instance