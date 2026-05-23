from fastmcp import FastMCP
from pymysql import Connection
mcp = FastMCP("DataBaseServer")

@mcp.tool()
def query_database(query: str) ->str:
    """执行数据库查询并返回结果"""
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

if __name__ == "__main__":
    mcp.run()
