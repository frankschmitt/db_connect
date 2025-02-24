import pyodbc
from os import getenv
import requests
import requests.auth


# get OAuth token for snowflake
def get_snowflake_token(username: str, password: str, client_id: str, client_secret: str, token_url: str) -> str:
    """Get Snowflake token using OAuth2"""
    bare_username = username.split("@")[0]  # strip domain part
    client_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    post_data = {
        "grant_type": "password",
        "username": bare_username,
        "password": password,
        "scope": "session:role-any",
    }
    response = requests.post(token_url, auth=client_auth, data=post_data)
    token_json = response.json()
    print(f"Got token: {token_json}")
    return token_json["access_token"]


# connect to Snowflake with externalbrowser (simplest to use, for ad-hoc sessions)
def snowflake_conn():
    dsn = getenv("SNOWFLAKE_ODBC_DSN")
    username = getenv("SNOWFLAKE_USER")
    password = getenv("SNOWFLAKE_PASSWORD")
    client_id = getenv("SNOWFLAKE_CLIENT_ID")
    client_secret = getenv("SNOWFLAKE_CLIENT_SECRET")
    token_url = getenv("SNOWFLAKE_TOKEN_URL")

    token = get_snowflake_token(username, password, client_id, client_secret, token_url)
    conn_str =(f"DSN={dsn};token={token}")
    print(f"connecting to: {conn_str}")
    conn = pyodbc.connect(conn_str)
    return conn


if __name__ == '__main__':
  conn = snowflake_conn()
  cursor = conn.cursor()
  cursor.execute('select current_user() where 1 = ?', [1])
  res = cursor.fetchall()
  print(res)
