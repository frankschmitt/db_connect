library(RJDBC)

# load JDBC driver
jdbcdriver = "lib/ojdbc8.jar"
write(paste("loading JDBC driver from: ", jdbcdriver), stderr())
drv = JDBC("oracle.jdbc.OracleDriver", classPath = jdbcdriver, "")

host = "localhost"
port = "1521"
service_name = "xe"
jdbcConnectString = sprintf("jdbc:oracle:thin:@%s:%s/%s", host, port, service_name)
print(jdbcConnectString)

username "scott"
password = "tiger"

con = dbConnect(drv, jdbcConnectString, username, password)

q = "select * from dual"
result = dbGetQuery(con, q)
print(result)
