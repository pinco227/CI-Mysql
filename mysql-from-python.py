# import os
# import pwd
# pwd.getpwuid(os.getuid())[0]
import datetime
import pymysql

# Get username
username = "root"
password = "root"

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password=password,
                             db="Chinook")

# try:
#     # Run a query
#     with connection.cursor(pymysql.cursors.DictCursor) as cursor:
#         sql = "SELECT * FROM Genre;"
#         cursor.execute(sql)
#         for row in cursor:
#             print(row)
# finally:
#     # Close the connection, regardless of whether the above was successful
#     connection.close()

# try:
#     # Run a query
#     with connection.cursor() as cursor:
#         cursor.execute("""CREATE TABLE IF NOT EXISTS
#                        Friends(name char(20), age int, DOB datetime);""")
#         # Note that the above will still display a warning (not error) if the table already exists
# finally:
#     # Close the connection, regardless of whether the above was successful
#     connection.close()

try:
    # Run a query
    with connection.cursor() as cursor:
        row = ("Bob", 21, "1990-02-06 23:04:56")
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
