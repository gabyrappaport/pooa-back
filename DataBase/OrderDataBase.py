import sqlite3
from DataBase.Helper.DatabaseConnector import Database
from Controllers.Helper.WritingDataBaseError import WritingDataBaseError


class OrderDataBase:

    def __init__(self):
        pass

    def get_all_orders(self):
        query = Database.query("SELECT * FROM Orders")
        result = []
        for row in query:
            order = self.__list_to_dic_order(row)
            result.append(order)
        return result

    def get_order(self, id_order):
        query_order = Database.query("SELECT * FROM Orders WHERE id_order = ?",
                                     (id_order,))
        order = query_order.fetchone()
        if order is not None:
            return self.__list_to_dic_order(order)
        else:
            return order

    def add_order(self, order):
        try:
            values = (int(order.get_id_order()),
                      int(order.get_id_supplier()),
                      int(order.get_id_client()),
                      order.get_expected_delivery_date(),
                      order.get_payment_type())
            Database.query("INSERT INTO Orders VALUES (?,?,?,?,?)", values)
        except (ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def update_order(self, order):
        try:
            values = (int(order.get_id_supplier()),
                      int(order.get_id_client()),
                      order.get_expected_delivery_date(),
                      order.get_payment_type(),
                      int(order.get_id_order()))

            Database.query("UPDATE Orders "
                           "SET id_supplier = ?,"
                           "id_client = ?,"
                           "expected_delivery_date = ?,"
                           "payment_type = ?"
                           "WHERE id_order = ?", values)
        except (ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def delete_order(self, id_order):
        Database.query("DELETE from Orders "
                       "WHERE id_order = ?", (id_order,))

    def __list_to_dic_order(self, order):
        return {"id_order": order[0],
                "supplier": order[1],
                "client": order[2],
                "expected_delivery_date": order[3],
                "payment_type": order[4]}