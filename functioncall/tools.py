tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "获取给定位置的当前天气",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "城市或区，例如北京、海淀"
                    }
                },
                "required": ["location"]
            }

        }
    }
]
