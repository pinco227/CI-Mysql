# import os
# import pwd
# pwd.getpwuid(os.getuid())[0]
# import datetime
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
#     with connection.cursor() as cursor:
#         sql = "SELECT * FROM Genre;"
#         cursor.execute(sql)
#         print(cursor.fetchall()) #returns a tuple
# finally:
#     # Close the connection, regardless of whether the above was successful
#     connection.close()

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

# try:
#     # Run a query
#     with connection.cursor() as cursor:
#         row = ("Bob", 21, "1990-02-06 23:04:56")
#         cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
#         connection.commit() # Save changes to table
# finally:
#     # Close the connection, regardless of whether the above was successful
#     connection.close()

# try:
#     # Run a query
#     with connection.cursor() as cursor:
#         rows = [("Bob", 21, "1990-02-06 23:04:56"),
#                 ("Jim", 56, "1995-05-09 13:12:45"),
#                 ("Fred", 100, "1911-09-12 01:01:01")]
#         cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
#         connection.commit()
# finally:
#     # Close the connection, regardless of whether the above was successful
#     connection.close()

# try:
#     # Run a query
#     with connection.cursor() as cursor:
#         cursor.execute("UPDATE Friends SET age = %s WHERE Name = %s;",
#                        (23, 'Bob'))
#         connection.commit()
# finally:
#     # Close the connection, regardless of whether the above was successful
#     connection.close()

# try:
#     # Run a query
#     with connection.cursor() as cursor:
#         rows = cursor.execute("DELETE FROM Friends WHERE Name = %s;", "jim")
#         connection.commit()
# finally:
#     # Close the connection, regardless of whether the above was successful
#     connection.close()

# try:
#     # Run a query
#     with connection.cursor() as cursor:
#         rows = cursor.executemany(
#             "DELETE FROM Friends WHERE Name = %s;", ["bob", "jim"])
#         connection.commit()
# finally:
#     # Close the connection, regardless of whether the above was successful
#     connection.close()

# try:
#     # Run a query
#     with connection.cursor() as cursor:
#         cursor.execute("DELETE FROM Friends WHERE Name in ('fred', 'bob');")
#         connection.commit()
# finally:
#     # Close the connection, regardless of whether the above was successful
#     connection.close()

# try:
#     # Run a query
#     with connection.cursor() as cursor:
#         names = ['fred', 'bob']
#         format_strings = ",".join(['%s']*len(names))
#         cursor.execute("DELETE FROM Friends WHERE Name in ({})".format(format_strings),
#                        names)
#         connection.commit()
# finally:
#     # Close the connection, regardless of whether the above was successful
#     connection.close()
