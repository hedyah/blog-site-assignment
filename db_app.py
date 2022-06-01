
import dbcreds
import mariadb

conn = mariadb.connect(
                        user = dbcreds.user,
                        password = dbcreds.password,
                        host = dbcreds.host,
                        port = dbcreds.port,
                        database = dbcreds.database
)

cursor = conn.cursor()

cursor.execute("INSERT INTO blog_assignment(username, content)")

conn.commit()