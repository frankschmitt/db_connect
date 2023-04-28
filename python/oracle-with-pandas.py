# prep
# pip install pandas
# pip install SQLAlchemy
# pip install cx_Oracle 

import pandas as pd
import cx_Oracle
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
try:
   engine = sqlalchemy.create_engine("oracle+cx_oracle://usr:pswd@localhost/?service_name=orclpdb1", arraysize=1000)
   orders_sql = """SELECT * FROM orders"""; 
   df_orders = pd.read_sql(orders_sql, engine)
   details_sql = """SELECT * FROM details""";
   df_details = pd.read_sql(details_sql, engine)
   print(df_orders) 
   print(df_details) 
except SQLAlchemyError as e:
   print(e)
