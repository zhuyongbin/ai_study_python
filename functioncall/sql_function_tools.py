import pymysql
import json

from pymysql import Connection

database_schema_string = """
CREATE TABLE `sys_user`  (
  `id` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,-- id 主键
  `name` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL, -- 用户姓名
  `age` int(10) NULL DEFAULT NULL, -- 用户年龄
  PRIMARY KEY (`id`) USING BTREE
)"""


def ask_database(query: str):
    """执行SQL查询并返回结果"""
    try:
        connection = Connection(
            host="localhost",
            user="root",
            password="root1234",
            port=3306,
            database="python_mysql",
            autocommit=True)
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return str(result)
    except Exception as e:
        return f"查询数据失败 {query},{str(e)}"


tools = [
    {
        "type": "function",
        "function": {
            "name": "ask_database",
            "description": "使用此函数回答业务问题，要求输出是一个SQL查询语句",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": f"SQL查询语句，基于以下数据库结构:{database_schema_string}"
                    }
                },
                "required": ["query"]
            }
        }
    }
]

