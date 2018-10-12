import sqlite3

conn = sqlite3.connect("itn.db")

cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS 
Orders(id_order INTEGER PRIMARY KEY UNIQUE,
     id_supplier INTEGER,
     id_client INTEGER,
     expected_delivery_date DATE,
     payment_type TEXT
      )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS 
Shipments(id_shipment INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     expedition_date DATE,
     transportation TEXT,
     departure_location TEXT,
     arrival_location TEXT
      )""")

conn.commit()
