import datetime
from DataBase.Helper.DatabaseConnector import Database
from Controllers.Helper.WritingDataBaseError import WritingDataBaseError


class OrderDataBase:

    def __init__(self):
        pass

    def get_all_orders(self):
        """Get all orders info"""
        query = Database.query("SELECT * FROM Orders ORDER BY creation_date DESC")
        result = []
        for row in query:
            order = self.__list_to_dic_order(row)
            result.append(order)
        return result

    def get_order(self, id_order):
        """Get order info with its id"""
        query_order = Database.query("SELECT * FROM Orders WHERE id_order = ?",
                                     (id_order,))
        order = query_order.fetchone()
        if order is not None:
            return self.__list_to_dic_order(order)
        else:
            return order

    def add_order(self, order):
        """Create a new order and return its id which is autoincremented in database"""
        try:
            values = (int(order.get_id_supplier()),
                      int(order.get_id_client()),
                      order.get_expected_delivery_date(),
                      order.get_payment_type(),
                      order.get_l_dips(),
                      order.get_appro_ship_sample(),
                      order.get_appro_s_off(),
                      order.get_ship_sample_2h(),
                      order.get_total_amount(),
                      order.get_creation_date())
            Database.query("INSERT INTO Orders "
                           "(id_supplier, id_client, expected_delivery_date,"
                           "payment_type, l_dips, appro_ship_sample, appro_s_off,"
                           "ship_sample_2h, total_amount, creation_date)"
                           "VALUES (?,?,?,?,?,?,?,?,?,?)", values)
            id_order = Database.query("SELECT last_insert_rowid() FROM Orders").fetchone()
            return id_order[0]
        except (ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def update_order(self, order):
        try:
            values = (int(order.get_id_supplier()),
                      int(order.get_id_client()),
                      order.get_expected_delivery_date(),
                      order.get_payment_type(),
                      order.get_l_dips(),
                      order.get_appro_ship_sample(),
                      order.get_appro_s_off(),
                      order.get_ship_sample_2h(),
                      order.get_total_amount(),
                      int(order.get_id_order()))
            Database.query("UPDATE Orders "
                           "SET id_supplier = ?,"
                           "id_client = ?,"
                           "expected_delivery_date = ?,"
                           "payment_type = ?,"
                           "l_dips = ?,"
                           "appro_ship_sample = ?,"
                           "appro_s_off = ?,"
                           "ship_sample_2h = ?,"
                           "total_amount = ?"
                           "WHERE id_order = ?", values)
        except (ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def set_total_amount(self, total_amount, id_order):
        """Set total_amount in database"""
        try:
            Database.query("UPDATE Orders "
                           "SET total_amount = ?"
                           "WHERE id_order = ?", (total_amount, id_order))
        except (ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def supplier_income(self, month):
        """Give the income from every supplier in the month"""
        try:
            query_income = Database.query("SELECT id_supplier, partner_type, SUM(total_amount) "
                                          "FROM Orders, Partners "
                                          "WHERE Orders.id_supplier = Partners.id_partner "
                                          "AND strftime('%m', creation_date) = ?"
                                          "GROUP BY id_partner, partner_type",
                                          (str(month),))
            result = []
            for row in query_income:
                income = self.__list_to_dic_income(row)
                result.append(income)
            return result
        except (ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def client_income(self, month):
        """Give the income from every client in the month"""
        try:
            query_income = Database.query("SELECT id_client, partner_type, SUM(total_amount) "
                                          "FROM Orders, Partners "
                                          "WHERE Orders.id_client = Partners.id_partner "
                                          "AND strftime('%m', creation_date) = ?"
                                          "GROUP BY id_partner, partner_type",
                                          (str(month),))
            result = []
            for row in query_income:
                income = self.__list_to_dic_income(row)
                result.append(income)
            return result
        except (ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def delete_order(self, id_order):
        """Delete order with its id"""
        Database.query("DELETE from Orders "
                       "WHERE id_order = ?", (id_order,))

    def __list_to_dic_order(self, order):
        return {"id_order": order[0],
                "supplier": order[1],
                "client": order[2],
                "expected_delivery_date": order[3],
                "payment_type": order[4],
                "l_dips": order[5],
                "appro_ship_sample": order[6],
                "appro_s_off": order[7],
                "ship_sample_2h": order[8],
                "total_amount": order[9],
                "creation_date": order[10]}

    def __list_to_dic_income(self, income):
        return {"id_partner": income[0],
                "partner_type": income[1],
                "income": income[2]}