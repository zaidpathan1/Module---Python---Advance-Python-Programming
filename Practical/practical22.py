import sqlite3

conn = sqlite3.connect("techfix.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    device_type TEXT NOT NULL,
    price REAL
)
""")

conn.commit()
conn.close()
