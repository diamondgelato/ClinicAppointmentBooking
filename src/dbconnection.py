import sqlite3 as sql

conn = sql.connect(r'C:\Users\ashuk\Documents\Semester 4\Mini Project\ClinicAppointmentBooking\data.db')
cur = conn.cursor()

query = "SELECT * FROM doctor"
cur.execute (query)
print (cur.fetchall())

conn.commit()
conn.close()