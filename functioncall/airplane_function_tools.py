tools = [
    {
        "type": "function",
        "function": {
            "name": "get_plane_number",
            "description": "根据出发地、目的地和日期，查询对应日期的航班号",
            "parameters": {
                "type": "object",
                "properties": {
                    "start_location": {"type": "string", "description": "出发地"},
                    "end_location": {"type": "string", "description": "目的地"},
                    "date": {"type": "string", "description": "日期"}
                },
                "required": ["start_location", "end_location", "date"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_ticket_price",
            "description": "查询某航班在某日的价格",
            "parameters": {
                "type": "object",
                "properties": {
                    "number": {"type": "string", "description": "航班号"},
                    "date": {"type": "string", "description": "日期"}
                },
                "required": ["number", "date"]
            }
        }
    }
]