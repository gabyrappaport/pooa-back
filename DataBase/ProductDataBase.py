from Controllers.Helper.WritingDataBaseError import *
from DataBase.Helper.DatabaseConnector import *


class ProductDatabase:

    def __init__(self):
        pass

    def add_product(self, product):
        """Create a new product and return its id which is autoincremented in database"""
        try:
            values = (int(product.id_order),
                      str(product.reference),
                      str(product.color),
                      float(product.meter),
                      float(product.price),
                      float(product.commission))
            Database.query("INSERT INTO Products"
                           "(id_order,"
                           "reference,"
                           "color,"
                           "meter,"
                           "price,"
                           "commission) "
                           "VALUES(?,?,?,?,?,?) ", values)
            id_product = Database.query("SELECT last_insert_rowid() FROM Products").fetchone()
            if product.id_shipment:
                values = (int(product.id_shipment),
                          id_product)
                Database.query("UPDATE Products "
                               "SET id_shipment = ?"
                               "WHERE id_product = ?", values)
            return id_product[0]
        except (ValueError, TypeError) as e:
            raise WritingDataBaseError(str(e))

    def delete_product(self, id_product):
        """Delete a product with its id"""
        Database.query("DELETE FROM Products WHERE id_product = ?", (id_product,))

    def delete_old_products(self, id_order, products_in_order):
        """Delete the products that do not exist anymore during the update of an order"""
        if len(products_in_order) == 1:
            Database.query("DELETE FROM Products WHERE id_order = ? AND id_product != ?",
                           (id_order, products_in_order[0]))
        elif len(products_in_order) == 0:
            Database.query("DELETE FROM Products WHERE id_order = ?", (id_order,))
        elif len(products_in_order) > 1:
            str = '(' + ','.join(['?' for i in products_in_order]) + ')'
            Database.query("DELETE FROM Products WHERE id_order = ? AND id_product NOT IN " + str,
                           (id_order, *products_in_order))

    def get_products(self, id_order):
        """Give the list of products in the order with its id"""
        query_order = Database.query("SELECT * FROM Products WHERE id_order = ?",
                                     (id_order,))
        result = []
        for row in query_order:
            product = self.__list_to_dic_product(row)
            result.append(product)
        return result

    def get_products_from_id_shipment(self, id_shipment):
        try:
            query_product_from_ship = Database.query("SELECT * FROM Products WHERE id_shipment=?", (id_shipment,))
            result = []
            for row in query_product_from_ship:
                product = self.__list_to_dic_product(row)
                result.append(product)
            return result
        except(ValueError, TypeError) as e:
            raise WritingDataBaseError(str(e))

    def update_product(self, product):
        try:
            values = (int(product.id_order),
                      str(product.reference),
                      product.color,
                      product.meter,
                      float(product.price),
                      float(product.commission),
                      int(product.id_product))
            Database.query("UPDATE Products "
                           "SET id_order = ?,"
                           "reference = ?,"
                           "color = ?,"
                           "meter = ?,"
                           "price = ?,"
                           "commission = ?"
                           "WHERE id_product = ?", values)
            if product.id_shipment:
                values = (int(product.id_shipment()),
                          int(product.id_product()))
                Database.query("UPDATE Products"
                               " SET id_shipment = ?"
                               "WHERE id_product = ?", values)
        except (ValueError, TypeError) as e:
            raise WritingDataBaseError(str(e))

    def set_id_shipment(self, id_product, id_shipment):
        """Set id_shipment in database"""
        try:
            Database.query("UPDATE Products "
                           "SET id_shipment = ? "
                           "WHERE id_product = ?", (id_shipment, id_product))
        except(ValueError, TypeError) as e:
            raise WritingDataBaseError(str(e))

    def delete_id_shipment(self, id_product):
        try:
            Database.query("UPDATE Products SET id_shipment = null WHERE id_product = ?", (id_product,))
        except(ValueError, TypeError) as e:
            raise WritingDataBaseError(str(e))

    def get_id_product_from_shipment(self, id_shipment):
        try:
            query_product_from_ship = Database.query("SELECT id_product FROM Products WHERE id_shipment=?",
                                                     (id_shipment,))
            result = []
            for row in query_product_from_ship:
                result.append(row[0])
            return result
        except(ValueError, TypeError) as e:
            raise WritingDataBaseError(str(e))

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
