import sqlite3

from Controllers.Helper.WritingDataBaseError import WritingDataBaseError


class ShipmentDataBase:

    def __init__(self):
        self.conn = sqlite3.connect('itn.db')
        self.c = self.conn.cursor()

    def get_shipments_expedition_date(self, expedition_date):
        query = self.c.execute("SELECT * FROM Shipments WHERE expedition_date=?", (expedition_date,))
        result = []
        for row in query:
            shipment = self.__list_to_dic_shipment(row)
            result.append(shipment)
        return result

    def get_shipments_id_order(self, id_order):
        query = self.c.execute("SELECT * FROM Shipments WHERE id_shipment IN "
                               "(SELECT DISTINCT id_shipment FROM Products WHERE id_order=?)", (id_order,))
        result = []
        for row in query:
            shipment = self.__list_to_dic_shipment(row)
            result.append(shipment)
        return result

    def get_shipment_id_shipment(self, id_shipment):
        query_shipment = self.c.execute("SELECT * FROM Shipments WHERE id_shipment = ?",
                                        (id_shipment,))  # EUh, attention, la virgule est importante
        shipment = query_shipment.fetchone()
        result = self.__list_to_dic_shipment(shipment)
        return result

    def get_all_shipments(self):
        query = self.c.execute("SELECT * FROM Shipments")
        result = []
        for row in query:
            shipment = self.__list_to_dic_shipment(row)
            result.append(shipment)
        return result

    def add_shipment(self, shipment):
        try:
            values = (shipment.get_id_shipment(),
                      shipment.get_expedition_date(),
                      shipment.get_transportation(),
                      shipment.get_departure_location(),
                      shipment.get_arrival_location())
            self.c.execute("INSERT INTO Shipments VALUES (?,?,?,?,?)", values)
            self.conn.commit()  # Si on fait pas ca, ca enregistre pas les données dans la table.
        except (ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def update_shipment(self, shipment):
        try:
            values = (shipment.get_expedition_date(),
                      shipment.get_transportation(),
                      shipment.get_departure_location(),
                      shipment.get_arrival_location(),
                      shipment.get_id_shipment())
            self.c.execute("UPDATE Shipments "
                           "SET expedition_date = ?,"
                           "transportation = ?,"
                           "departure_location = ?,"
                           "arrival_location = ?"
                           "WHERE id_shipment = ?", values)
            self.conn.commit()  # Si on fait pas ca, ca enregistre pas les données dans la table.
        except (ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def delete_shipment(self, id_shipment):
        self.c.execute("DELETE from Shipments "
                       "WHERE id_shipment = ?", (id_shipment,))
        self.conn.commit()

    def __list_to_dic_shipment(self, shipment):
        return {"id_shipment": shipment[0],
                "expedition_date": shipment[1],
                "transportation": shipment[2],
                "departure_location": shipment[3],
                "arrival_location": shipment[4]}
