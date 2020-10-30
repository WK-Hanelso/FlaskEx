import sqlite3

conn = sqlite3.connect("./chadwick.db")
print("Opened database successfully")

cursor = conn.execute("select yearID from Salaries limit 10")

for row in cursor:
    print(row )
    print("yearID=", row[0] )
