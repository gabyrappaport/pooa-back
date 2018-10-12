import sqlite3
from Controllers.Helper.WritingDataBaseError import WritingDataBaseError


class OrderDataBase:

    def __init__(self):
        self.conn = sqlite3.connect('itn.db')
        self.c = self.conn.cursor()

    def get_all_orders(self):
        query = self.c.execute("SELECT * FROM Orders")
        result = []
        for row in query:
            order = self.__list_to_dic_order(row)
            result.append(order)
        return result

    def get_order(self, id_order):
        query_order = self.c.execute("SELECT * FROM Orders WHERE id_order = ?",
                                     (id_order,))  # EUh, attention, la virgule est importante
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
            self.c.execute("INSERT INTO Orders VALUES (?,?,?,?,?)", values)
            self.conn.commit()  # Si on fait pas ca, ca enregistre pas les données dans la table.
        except (ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def update_order(self, order):
        try:
            values = (int(order.get_id_supplier()),
                      int(order.get_id_client()),
                      order.get_expected_delivery_date(),
                      order.get_payment_type(),
                      int(order.get_id_order()))

            self.c.execute("UPDATE Orders "
                           "SET supplier = ?,"
                           "client = ?,"
                           "expected_delivery_date = ?,"
                           "payment_type = ?"
                           "WHERE id_order = ?", values)
            self.conn.commit()
        except (ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def delete_order(self, id_order):
        self.c.execute("DELETE from Orders "
                       "WHERE id_order = ?", (id_order,))
        self.conn.commit()

    def __list_to_dic_order(self, order):
        return {"id_order": order[0],
                "supplier": order[1],
                "client": order[2],
                "expected_delivery_date": order[3],
                "payment_type": order[4]}