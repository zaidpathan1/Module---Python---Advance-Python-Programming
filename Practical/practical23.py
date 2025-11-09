import sqlite3

conn = sqlite3.connect("techfix.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO devices (name, device_type, price) VALUES (?, ?, ?)", 
               ("iPhone 14", "Smartphone", 1200))
cursor.execute("INSERT INTO devices (name, device_type, price) VALUES (?, ?, ?)", 
               ("Dell XPS 13", "Laptop", 1500))
cursor.execute("INSERT INTO devices (name, device_type, price) VALUES (?, ?, ?)", 
               ("Samsung Galaxy S23", "Smartphone", 1000))

conn.commit()

cursor.execute("SELECT * FROM devices")
rows = cursor.fetchall()

print("=== Devices in TechFix Database ===")
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Type: {row[2]}, Price: ${row[3]}")

conn.close()