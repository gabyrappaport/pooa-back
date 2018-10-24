import os
import sqlite3

os.remove("itn.db")
conn = sqlite3.connect("itn.db")

cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS 
Orders(id_order INTEGER PRIMARY KEY UNIQUE,
     id_supplier INTEGER,
     id_client INTEGER,
     expected_delivery_date DATE,
     payment_type TEXT,
     l_dips TEXT,
     appro_ship_sample TEXT,
     appro_s_off TEXT,
     ship_sample_2h TEXT,
     total_amount REAL,
     creation_date DATE
      )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS 
Shipments(id_shipment INTEGER PRIMARY KEY UNIQUE,
     expedition_date DATE,
     transportation TEXT,
     departure_location TEXT,
     arrival_location TEXT
      )""")

cursor.execute('''CREATE TABLE IF NOT EXISTS
Partners(id_partner INTEGER PRIMARY KEY UNIQUE,
     partner_type TEXT,
     company TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS
Products(id_product INTEGER PRIMARY KEY UNIQUE,
     id_order INT,
     id_shipment INT,
     reference TEXT,
     color TEXT,
     meter REAL,
     price REAL,
     commission REAL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS
Users(id_user INTEGER PRIMARY KEY UNIQUE,
     name TEXT,
     surname TEXT,
     email TEXT,
     password TEXT,
     user_type TEXT)''')

conn.commit()
cursor.close()
conn.close()
