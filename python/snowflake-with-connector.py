import snowflake.connector
from os import getenv

# connect to Snowflake with externalbrowser (simplest to use, for ad-hoc sessions)
def snowflake_conn():
    conn = snowflake.connector.connect(
             account = getenv('SNOWFLAKE_ACCOUNT'),
             warehouse = getenv('SNOWFLAKE_WAREHOUSE'),
             database =  getenv('SNOWFLAKE_DATABASE'),
             role =  getenv('SNOWFLAKE_ROLE'),
             authenticator = 'externalbrowser',
             paramstyle = 'qmark',
             user =  getenv('SNOWFLAKE_USER')
             )
    return conn

if __name__ == '__main__':
  conn = snowflake_conn()
  cursor = conn.cursor()
  cursor.execute('select current_user() where 1 = ?', [1])
  res = cursor.fetchall()
  print(res)
