from DataBase.Helper.DatabaseConnector import *
from Controllers.Helper.WritingDataBaseError import WritingDataBaseError


class ShipmentDataBase:

    def __init__(self):
        pass

    def get_shipments_expedition_date(self, expedition_date):
        query = Database.query("SELECT * FROM Shipments WHERE expedition_date=?", (expedition_date,))
        result = []
        for row in query:
            shipment = self.__list_to_dic_shipment(row)
            result.append(shipment)
        return result

    def get_shipments_id_order(self, id_order):
        query = Database.query("SELECT * FROM Shipments WHERE id_shipment IN "
                               "(SELECT DISTINCT id_shipment FROM Products WHERE id_order=?)", (id_order,))
        result = []
        for row in query:
            shipment = self.__list_to_dic_shipment(row)
            result.append(shipment)
        return result

    def get_shipment_id_shipment(self, id_shipment):
        query_shipment = Database.query("SELECT * FROM Shipments WHERE id_shipment = ?",
                                        (id_shipment,))
        shipment = query_shipment.fetchone()
        result = self.__list_to_dic_shipment(shipment)
        return result

    def get_all_shipments(self):
        query = Database.query("SELECT * FROM Shipments")
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
            Database.query("INSERT INTO Shipments VALUES (?,?,?,?,?)", values)
        except (ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def update_shipment(self, shipment):
        try:
            values = (shipment.get_expedition_date(),
                      shipment.get_transportation(),
                      shipment.get_departure_location(),
                      shipment.get_arrival_location(),
                      shipment.get_id_shipment())
            Database.query("UPDATE Shipments "
                           "SET expedition_date = ?,"
                           "transportation = ?,"
                           "departure_location = ?,"
                           "arrival_location = ?"
                           "WHERE id_shipment = ?", values)
        except (ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def delete_shipment(self, id_shipment):
        Database.query("DELETE from Shipments "
                       "WHERE id_shipment = ?", (id_shipment,))

    def __list_to_dic_shipment(self, shipment):
        return {"id_shipment": shipment[0],
                "expedition_date": shipment[1],
                "transportation": shipment[2],
                "departure_location": shipment[3],
                "arrival_location": shipment[4]}
