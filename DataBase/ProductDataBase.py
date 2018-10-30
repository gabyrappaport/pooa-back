from Controllers.Helper.WritingDataBaseError import *
from DataBase.Helper.DatabaseConnector import *


class ProductDatabase:

    def __init__(self):
        pass

    def add_product(self, product):
        """Create a new product and return its id which is autoincremented in database"""
        try:
            values = (int(product.get_id_order()),
                      str(product.get_reference()),
                      str(product.get_color()),
                      float(product.get_meter()),
                      float(product.get_price()),
                      float(product.get_commission()))
            Database.query("INSERT INTO Products"
                           "(id_order,"
                           "reference,"
                           "color,"
                           "meter,"
                           "price,"
                           "commission) "
                           "VALUES(?,?,?,?,?,?) ", values)
            id_product = Database.query("SELECT last_insert_rowid() FROM Products").fetchone()
            if product.get_id_shipment():
                values = (int(product.get_id_shipment()),
                          id_product)
                Database.query("UPDATE Products "
                               "SET id_shipment = ?"
                               "WHERE id_product = ?", values)
            return id_product[0]
        except (ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def delete_product(self, id_product):
        """Delete a product with its id"""
        Database.query("DELETE FROM Products WHERE id_product = ?", (id_product,))

    def delete_old_products(self, id_order, id_products_keep):
        """Delete the products that do not exist anymore during the update of an order"""
        if len(id_products_keep) == 1:
            sql = "DELETE FROM Products WHERE id_order = ? AND id_product  != ?"
            values = (id_order, id_products_keep[0])
        elif len(id_products_keep) == 0:
            sql = "DELETE FROM Products WHERE id_order = ?"
            values = (id_order,)
        elif len(id_products_keep) > 1:
            sql = "DELETE FROM Products WHERE id_order = ? AND id_product NOT IN ?"
            values = (id_order, tuple(id_products_keep))
        Database.query(sql, values)

    def get_products(self, id_order):
        """Give the list of products in the order with its id"""
        query_order = Database.query("SELECT * FROM Products WHERE id_order = ?",
                                     (id_order,))
        result = []
        for row in query_order:
            product = self.__list_to_dic_product(row)
            result.append(product)
        return result

    def update_product(self, product):
        try:
            values = (int(product.get_id_order()),
                      int(product.get_reference()),
                      product.get_color(),
                      product.get_meter(),
                      int(product.get_price()),
                      float(product.get_commission()),
                      int(product.get_id_product()))
            Database.query("UPDATE Products "
                           "SET id_order = ?,"
                           "reference = ?,"
                           "color = ?,"
                           "meter = ?,"
                           "price = ?,"
                           "commission = ?"
                           "WHERE id_product = ?", values)
            if product.get_id_shipment():
                values = (int(product.get_id_shipment()),
                          int(product.get_id_product()))
                Database.query("UPDATE Products"
                               " SET id_shipment = ?"
                               "WHERE id_product = ?", values)
        except (ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def set_id_shipment(self, id_product, id_shipment):
        """Set id_shipment in database"""
        try:
            Database.query("UPDATE Products "
                           "SET id_shipment = ? "
                           "WHERE id_product = ?", (id_shipment, id_product))
        except(ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def __list_to_dic_product(self, product):
        if product[2] is None:
            id_shipment = -1
        else:
            id_shipment = product[2]
        return {"id_product": product[0],
                "id_order": product[1],
                "id_shipment": id_shipment,
                "reference": product[3],
                "color": product[4],
                "meter": product[5],
                "price": product[6],
                "commission": product[7]}
