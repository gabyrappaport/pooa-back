import os
import sqlite3

if os.path.exists("itn.db"):
    os.remove("itn.db")  # à enlever
conn = sqlite3.connect("itn.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS 
Orders(id_order INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     id_supplier INTEGER,
     id_client INTEGER,
     expected_delivery_date DATE,
     payment_type TEXT,
     l_dips TEXT,
     appro_ship_sample TEXT,
     appro_s_off TEXT,
     ship_sample_2h TEXT,
     total_amount REAL,
     creation_date DATE,
     complete_delivery_date DATE,
     complete_payment_date DATE
      )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS 
Shipments(id_shipment INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     expedition_date DATE,
     transportation TEXT,
     departure_location TEXT,
     arrival_location TEXT
      )""")

cursor.execute('''CREATE TABLE IF NOT EXISTS
Partners(id_partner INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     partner_type TEXT,
     company TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS
Products(id_product INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     id_order INT,
     id_shipment INT,
     reference TEXT,
     color TEXT,
     meter REAL,
     price REAL,
     commission REAL)''')

partners = [((1), "client", "Zara"),
            ((2), "client", "HM"),
            ((3), "client", "Mango"),
            ((4), "client", "Kenzo"),
            ((5), "client", "Etam"),
            ((6), "supplier", "Mianoutex"),
            ((7), "supplier", "Hangzhoutex"),
            ((8), "supplier", "Seoultex"),
            ((9), "supplier", "Vietnamtex")]

shipments = [((0), ("2018-11-01"), "bateau", "Shanghai", "Le Havre"),
             ((1), ("2018-10-03"), "truck", "New Delhi", "Le Havre"),
             ((2), ("2018-12-04"), "avion", "Shanghai", "CDG"),
             ((3), ("2018-09-22"), "avion", "Shanghai", "Barcelone"),
             ((4), ("2018-12-30"), "avion", "New Delhi", "CDG"),
             ((5), ("2018-09-04"), "avion", "Shanghai", "CDG"),
             ((6), ("2018-08-03"), "avion", "New Delhi", "CDG"),
             ((7), ("2018-06-04"), "avion", "Shanghai", "CDG"),
             ((8), ("2018-05-10"), "avion", "New Delhi", "CDG"),
             ((9), ("2018-10-10"), "truck", "Shanghai", "CDG"),
             ((10), ("2018-07-17"), "bateau", "Shanghai", "Le Havre")
             ]

orders_list = [
    [(0), (6), (1), "2018-12-10", "TT", "OK", "OK", "OK", "SSAttF", 1, "2018-09-01", None, None],
    [(1), (7), (2), "2018-11-09", "LC", "OK", "OK", "OK", "SSAttF", 2, "2018-09-01", None, None],
    [(2), (7), (1), "2019-01-02", "LC", "OK", "OK", "OK", "SSAttF", 124, "2018-09-02", "2018-09-10", None],
    [(3), (6), (2), "2018-11-05", "TT", "OK", "OK", "OK", "SSAttF", 64, "2018-08-15", "2018-09-10", None],
    [(4), (8), (1), "2018-08-12", "TT", "OK", "OK", "OK", "SSAttF", 1409, "2018-07-15", "2018-09-10", "2018-09-10"],
    [(5), (9), (5), "2018-10-24", "LC", "OK", "OK", "OK", "SSAttF", 169, "2018-06-05", "2018-09-10", "2018-09-10"],
    [(6), (6), (1), "2018-09-04", "TT", "OK", "OK", "OK", "SSAttF", 142, "2018-06-10", "2018-09-10", "2018-09-10"],
    [(7), (8), (3), "2018-09-09", "LC", "OK", "OK", "OK", "SSAttF", 183, "2018-07-01", "2018-09-10", "2018-09-10"],
    [(8), (7), (4), "2018-08-02", "LC", "OK", "OK", "OK", "SSAttF", 124, "2018-05-05", "2018-09-10", "2018-09-10"],
    [(9), (6), (2), "2018-07-05", "TT", "OK", "OK", "OK", "SSAttF", 64, "2018-04-15", "2018-09-10", "2018-09-10"],
    [(10), (8), (1), "2018-06-12", "TT", "OK", "OK", "OK", "SSAttF", 1409, "2018-04-15", "2018-09-10", "2018-09-10"],
    [(11), (9), (5), "2018-05-24", "LC", "OK", "OK", "OK", "SSAttF", 169, "2018-02-5", "2018-09-10", "2018-09-10"],
    [(12), (9), (4), "2018-10-02", "LC", "OK", "OK", "OK", "SSAttF", 124, "2018-08-31", "2018-09-10", "2018-09-10"],
    [(13), (8), (4), "2018-11-04", "LC", "OK", "OK", "OK", "SSAttF", 560, "2018-08-15", "2018-09-10", "2018-09-10"],
    [(14), (7), (3), "2018-09-12", "LC", "OK", "OK", "OK", "SSAttF", 124, "2018-06-15", "2018-09-10", "2018-09-10"],
    [(15), (6), (5), "2018-09-30", "LC", "OK", "OK", "OK", "SSAttF", 124, "2018-07-18", "2018-09-10", "2018-09-10"]]

products = [((0), (0), (2), "ref_1", "blue", 17.5, 12, 11),
            ((1), (0), (2), "ref_2", "grey", 20, 10, 14),
            ((2), (0), (2), "ref_3", "blank", 35, 9, 14),
            ((3), (1), (0), "ref_4", "blue", 150.8, 11, 11),
            ((4), (1), (0), "ref_5", "blue", 18.5, 7, 21),
            ((5), (1), (0), "ref_6", "blue", 19.5, 14, 11),
            ((6), (2), (4), "ref_1", "blue", 17.5, 12, 11),
            ((7), (2), (4), "ref_2", "grey", 26, 10, 15),
            ((8), (2), (4), "ref_3", "blank", 55, 9.4, 14),
            ((9), (3), (0), "ref_4", "blue", 150.8, 8.1, 17),
            ((10), (3), (0), "ref_5", "green", 18.5, 7, 11),
            ((11), (3), (0), "ref_6", "flowers", 19.5, 14, 22),
            ((12), (4), (6), "ref_1", "blue", 17.5, 12, 11),
            ((13), (4), (6), "ref_2", "grey", 20, 10, 22),
            ((14), (4), (10), "ref_3", "blank", 35, 9, 14),
            ((15), (5), (9), "ref_8", "blue", 150.8, 11, 7),
            ((16), (5), (9), "ref_5", "green", 50.5, 9, 7),
            ((17), (5), (9), "ref_6", "flowers", 49.5, 14, 7),
            ((18), (6), (6), "ref_1", "blue", 17.5, 12, 11),
            ((19), (6), (6), "ref_2", "grey", 20, 10, 15),
            ((20), (6), (6), "ref_3", "blank", 35, 9, 44),
            ((21), (7), (6), "ref_4", "blue", 150.8, 11, 7),
            ((22), (7), (6), "ref_5", "green", 18.5, 7, 7),
            ((23), (7), (6), "ref_6", "flowers", 19.5, 14, 7),
            ((24), (8), (10), "ref_1", "blue", 17.5, 12, 11),
            ((25), (8), (10), "ref_2", "grey", 20, 10, 15),
            ((26), (8), (10), "ref_3", "blank", 35, 9, 10),
            ((27), (9), (7), "ref_4", "blue", 150.8, 6, 7),
            ((28), (9), (7), "ref_5", "green", 56.5, 10.5, 7),
            ((29), (9), (8), "ref_9", "flowers", 89.5, 8, 11),
            ((30), (10), (6), "ref_4", "blue", 150.8, 11, 11),
            ((31), (10), (6), "ref_5", "green", 18.5, 7, 11),
            ((32), (10), (6), "ref_6", "flowers", 19.5, 14, 11),
            ((33), (11), (8), "ref_1", "blue", 17.5, 12, 11),
            ((34), (11), (8), "ref_5", "grey", 20, 10, 15),
            ((35), (11), (8), "ref_3", "blank", 35, 9, 10.4),
            ((36), (12), (5), "ref_4", "blue", 150.8, 11, 10),
            ((37), (12), (5), "ref_7", "green", 18.5, 7, 10),
            ((38), (12), (5), "ref_6", "flowers", 19.5, 14, 11.5),
            ((39), (13), (1), "ref_1", "blue", 17.5, 12, 11),
            ((40), (13), (1), "ref_2", "grey", 20, 10, 15),
            ((41), (13), (1), "ref_3", "blank", 35, 9, 14.7),
            ((42), (14), (5), "ref_4", "blue", 150.8, 11, 11),
            ((43), (14), (5), "ref_5", "green", 18.5, 7, 12),
            ((44), (14), (5), "ref_7", "flowers", 19.5, 14, 13),
            ((45), (15), (3), "ref_8", "blue", 150.8, 11, 11),
            ((46), (15), (3), "ref_9", "green", 18.5, 7, 11),
            ((47), (15), (3), "ref_6", "flowers", 19.5, 14, 11)
            ]

for i in range(len(orders_list)):
    orders_list[i][9] = \
        ((float(products[i][5]) * float(products[i][6]) * float(products[i][7])) + \
         (float(products[i + 1][5]) * float(products[i + 1][6]) * float(products[i + 1][7])) + \
         (float(products[i + 2][5]) * float(products[i + 2][6]) * float(products[i + 2][7]))).__round__(2)

for partner in partners:
    cursor.execute("INSERT INTO Partners VALUES(?,?,?)", partner)

for order in orders_list:
    cursor.execute("INSERT INTO Orders VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", order)

for shipment in shipments:
    cursor.execute("INSERT INTO Shipments VALUES (?,?,?,?,?)", shipment)

for product in products:
    cursor.execute("INSERT INTO Products VALUES (?,?,?,?,?,?,?,?)", product)

conn.commit()
cursor.close()
conn.close()
