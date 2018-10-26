import os
import sqlite3

os.remove("itn.db")
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
     creation_date DATE
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

cursor.execute('''CREATE TABLE IF NOT EXISTS
Users(id_user INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     surname TEXT,
     email TEXT,
     password TEXT,
     user_type TEXT)''')

partners = [((1), "client", "Zara"),
            ((2), "client", "HM"),
            ((3), "client", "Mango"),
            ((4), "client", "Kenzo"),
            ((5), "client", "Etam"),
            ((6), "supplier", "Mianoutex"),
            ((7), "supplier", "Hangzhoutex"),
            ((8), "supplier", "Seoultex"),
            ((9), "supplier", "Vietnamtex")]

Shipments = [((0),("2018-11-1"),"bateau","Shanghai", "Le Havre"),
             ((1), ("2018-10-3"), "truck", "New Delhi", "Le Havre"),
            ((2),("2018-12-4"),"avion","Shanghai", "CDG"),
            ((3),("2018-09-22"),"avion","Shanghai", "Barcelone"),
            ((4), ("2018-12-30"), "avion", "New Delhi", "CDG"),
            ((5),("2018-09-4"),"avion","Shanghai", "CDG"),
            ((6), ("2018-08-3"), "avion", "New Delhi", "CDG"),
            ((7),("2018-06-4"),"avion","Shanghai", "CDG"),
            ((8), ("2018-05-10"), "avion", "New Delhi", "CDG"),
            ((9),("2018-10-10"),"truck","Shanghai", "CDG"),
            ((10),("2018-07-17"),"bateau","Shanghai", "Le Havre")
             ]


orders_list = [[(0), (6), (1), "2018-12-10","TT","NO","NO","NO","NO",1,"2018-09-10"],
        [(1), (7), (2), "2018-11-9","LC at Sight","NO","NO","NO","NO",2,"2018-09-1"],
        [(2), (7), (1), "2019-01-2","LC at Sight","NO","NO","NO","NO",124,"2018-09-5"],
        [(3), (6), (2), "2018-11-5","TT","NO","NO","NO","NO",64,"2018-08-15"],
        [(4), (8), (1), "2018-08-12","TT","NO","NO","NO","NO",1409,"2018-07-15"],
        [(5), (9), (5), "2018-10-24","LC at Sight","NO","NO","NO","NO",169,"2018-09-5"],
        [(6), (6), (1), "2018-09-4","TT","NO","NO","NO","NO",142,"2018-06-10"],
        [(7), (8), (3), "2018-09-9","LC at Sight","NO","NO","NO","NO",183,"2018-07-1"],
        [(8), (7), (4), "2018-08-2","LC at Sight","NO","NO","NO","NO",124,"2018-05-5"],
        [(9), (6), (2), "2018-07-5","TT","NO","NO","NO","NO",64,"2018-04-15"],
        [(10), (8), (1), "2018-06-12","TT","NO","NO","NO","NO",1409,"2018-04-15"],
        [(11), (9), (5), "2018-05-24","LC at Sight","NO","NO","NO","NO",169,"2018-02-5"],
        [(12), (9), (4), "2018-10-2","LC at Sight","NO","NO","NO","NO",124,"2018-08-31"],
        [(13), (8), (4), "2018-11-4","LC at Sight","NO","NO","NO","NO",560,"2018-08-15"],
        [(14), (7), (3), "2018-09-12","LC at Sight","NO","NO","NO","NO",124,"2018-06-15"],
        [(15), (6), (5), "2018-09-30","LC at Sight","NO","NO","NO","NO",124,"2018-07-18"]]

products = [((0),(0),(2),"ref_1","blue",17.5,12,1.1),
            ((1),(0),(2),"ref_2","grey",20,10,1.05),
            ((2),(0),(2),"ref_3","blank",35,9,1.04),
            ((3),(1),(0),"ref_4","blue",150.8,11,1.108),
            ((4),(1),(0),"ref_5","blue",18.5,7,1.01),
            ((5),(1),(0),"ref_6","blue",19.5,14,1.11),
            ((6), (2), (4), "ref_1", "blue", 17.5, 12, 1.1),
            ((7), (2), (4), "ref_2", "grey", 26, 10, 1.5),
            ((8), (2), (4), "ref_3", "blank", 55, 9.4, 4.4),
            ((9), (3), (0), "ref_4", "blue", 150.8, 8.1, 1.7),
            ((10), (3), (0), "ref_5", "green", 18.5, 7, 1.1),
            ((11), (3), (0), "ref_6", "flowers", 19.5, 14, 1.05),
            ((12), (4), (6), "ref_1", "blue", 17.5, 12, 1.1),
            ((13), (4), (6), "ref_2", "grey", 20, 10, 1.05),
            ((14), (4), (10), "ref_3", "blank", 35, 9, 1.4),
            ((15), (5), (9), "ref_8", "blue", 150.8, 11, 0.1),
            ((16), (5), (9), "ref_5", "green", 50.5, 9, 0.1),
            ((17), (5), (9), "ref_6", "flowers", 49.5, 14, 0.1),
            ((18), (6), (6), "ref_1", "blue", 17.5, 12, 1.1),
            ((19), (6), (6), "ref_2", "grey", 20, 10, 1.5),
            ((20), (6), (6), "ref_3", "blank", 35, 9, 4.4),
            ((21), (7), (6), "ref_4", "blue", 150.8, 11, 0.1),
            ((22), (7), (6), "ref_5", "green", 18.5, 7, 0.1),
            ((23), (7), (6), "ref_6", "flowers", 19.5, 14, 0.1),
            ((24), (8), (10), "ref_1", "blue", 17.5, 12, 1.1),
            ((25), (8), (10), "ref_2", "grey", 20, 10, 1.5),
            ((26), (8), (10), "ref_3", "blank", 35, 9, 1.09),
            ((27), (9), (7), "ref_4", "blue", 150.8, 6, 0.1),
            ((28), (9), (7), "ref_5", "green", 56.5, 10.5, 0.1),
            ((29), (9), (8), "ref_9", "flowers", 89.5, 8, 1.1),
            ((30), (10), (6), "ref_4", "blue", 150.8, 11, 1.14),
            ((31), (10), (6), "ref_5", "green", 18.5, 7, 1.17),
            ((32), (10), (6), "ref_6", "flowers", 19.5, 14, 1.13),
            ((33), (11), (8), "ref_1", "blue", 17.5, 12, 1.1),
            ((34), (11), (8), "ref_5", "grey", 20, 10, 1.5),
            ((35), (11), (8), "ref_3", "blank", 35, 9, 1.04),
            ((36), (12), (5), "ref_4", "blue", 150.8, 11, 1.019),
            ((37), (12), (5), "ref_7", "green", 18.5, 7, 1.10),
            ((38), (12), (5), "ref_6", "flowers", 19.5, 14, 1.15),
            ((39), (13), (1), "ref_1", "blue", 17.5, 12, 1.1),
            ((40), (13), (1), "ref_2", "grey", 20, 10, 1.5),
            ((41), (13), (1), "ref_3", "blank", 35, 9, 1.47),
            ((42), (14), (5), "ref_4", "blue", 150.8, 11, 1.1),
            ((43), (14), (5), "ref_5", "green", 18.5, 7, 1.2),
            ((44), (14), (5), "ref_7", "flowers", 19.5, 14, 1.3),
            ((45), (15), (3), "ref_8", "blue", 150.8, 11, 1.1),
            ((46), (15), (3), "ref_9", "green", 18.5, 7, 1.1),
            ((47), (15), (3), "ref_6", "flowers", 19.5, 14, 1.1)
            ]

for i in range(len(orders_list)):
    orders_list[i][9] = (float(products[i][5])*float(products[i][6])*float(products[i][7])) + \
                 (float(products[i+1][5])*float(products[i+1][6])*float(products[i+1][7])) + \
                  (float(products[i+2][5])*float(products[i+2][6])*float(products[i+2][7]))

for partner in partners:
    cursor.execute("INSERT INTO Partners VALUES(?,?,?)", partner)

for order in orders_list:
    cursor.execute("INSERT INTO Orders VALUES (?,?,?,?,?,?,?,?,?,?,?)", order)

for shipment in Shipments:
    cursor.execute("INSERT INTO Shipments VALUES (?,?,?,?,?)", shipment)

for product in products:
    cursor.execute("INSERT INTO Products VALUES (?,?,?,?,?,?,?,?)", product)

conn.commit()
cursor.close()
conn.close()