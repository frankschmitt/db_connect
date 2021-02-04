# Create a connection to the database
library('RPostgreSQL')
## Loading required package: DBI
pg = dbDriver("PostgreSQL")
# Local Postgres.app database; no password by default
# Of course, you fill in your own database information here.
con = dbConnect(pg, user="postgres", password="1234",
                 host="localhost", port=5432) #, dbname="ninazumel")
# write the table into the database.
# use row.names=FALSE to prevent the query 
# from adding the column 'row.names' to the table 
# in the db
dbWriteTable(con,'iris',iris, row.names=FALSE)
