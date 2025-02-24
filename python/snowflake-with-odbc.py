import pyodbc
from os import getenv

# connect to Snowflake with externalbrowser (simplest to use, for ad-hoc sessions)
def snowflake_conn():
    driver = "{SnowflakeDSIIDriver}"
    database = getenv("SNOWFLAKE_DATABASE")
    user = getenv("SNOWFLAKE_USER")
    warehouse = getenv("SNOWFLAKE_WAREHOUSE")
    server = f"{getenv('SNOWFLAKE_ACCOUNT')}.snowflakecomputing.com"
    conn_str = f"DRIVER={driver};server={server};uid={user};warehouse={warehouse};authenticator=externalbrowser"
    print(f"connecting to: {conn_str}")
    conn = pyodbc.connect(conn_str)
    return conn


if __name__ == '__main__':
  conn = snowflake_conn()
  cursor = conn.cursor()
  cursor.execute('select current_user() where 1 = ?', [1])
  res = cursor.fetchall()
  print(res)
