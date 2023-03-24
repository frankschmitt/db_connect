from ldap3 import Server, Connection, SAFE_SYNC
from sys import argv

def connect(server, username, password): 
  # server = Server('my_server')
  #conn = Connection(server, 'my_user', 'my_password', client_strategy=SAFE_SYNC, auto_bind=True)
  server = Server(server)
  conn = Connection(server, username, password, client_strategy=SAFE_SYNC, auto_bind=True)
  return conn

def search(conn, term):
  #status, result, response, _ = conn.search('o=test', '(objectclass=*)')  # usually you don't need the original request (4th element of the returned tuple)
  status, result, response, _ = conn.search('o=' + term, '(objectclass=*)')  # usually you don't need the original request (4th element of the returned tuple)
  return (status, result, response)

if __name__ == '__main__':
    if len(argv) < 4:
        print("Usage: <progname> <server> <username> <password> <search term>")
        exit(1)
    server, username, password = argv[1], argv[2], argv[3]
    conn = connect(server, username, password)
    term = argv[4]
    status, result, response = search(conn, term)
    print(result)
