import json

def get_plane_number(date,start_location,end_location):
    """根据日期、出发地、目的地查询航班号"""
    # 模拟航班数据（实际应用中应调用航班API）
    plane_number = {
        "北京": {"深圳": "126", "广州": "356"},
        "郑州": {"北京": "1123", "天津": "3661"}
    }

    return {"date": date, "number": plane_number[start_location][end_location]}

def get_ticket_price(date,number):
    """根据日期和航班号查询票价"""
    # 模拟票价查询（实际应用中应调用票价API）
    print(f"查询日期: {date}, 航班号: {number}")
    return {"ticket_price": "668"}