import sqlite3

with sqlite3.connect("11-bdsqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute("SELECT * FROM usuarios")
    print(cursor.fetchall())
