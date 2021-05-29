import sqlite3 as sql

import ProgramVar as pv

conn = sql.connect(pv.databasePath)
cur = conn.cursor()

query = "SELECT * FROM patient"
cur.execute (query)
print (cur.fetchall())

conn.commit()
conn.close()