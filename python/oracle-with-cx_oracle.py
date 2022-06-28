import cx_Oracle
import time

# fetch data for given query (in batches, and measure throughput)
def get_data(db, username, password, query):
  con = cx_Oracle.connect(username + "/" + password + "@" + db)
  BATCHSIZE = 10000

  cur = con.cursor()
  print("Running query " + query + " on db " + db + "\n")
  start_time = time.time()
  cur.execute(query)
  n_overall = 0
  while True:
      rows = cur.fetchmany(BATCHSIZE)
      if not rows:
          break
      n_overall += len(rows)
      execution_time = time.time() - start_time
      rows_per_sec = n_overall / execution_time
      print("Fetched " + str(n_overall) + " rows in " + str(execution_time) + " seconds, rows per second: " + str(rows_per_sec))
 
 
def test_get_data():
  sql = "select * from dual"
  get_data("localhost:1521/xe",
           "scott",
           "tiger",
           sql)

test_get_data()

