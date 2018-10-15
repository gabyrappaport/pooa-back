from DataBase.Helper.DatabaseConnector import *
from Controllers.Helper.WritingDataBaseError import *


class ProductDatabase:

    def __init__(self):
        pass

    def add_product(self, product):
        """Create a new product with its id, reference, color and its price/meter"""
        try:
            values = (
                int(product.get_id_product()),
                int(product.get_id_order()),
                int(product.get_id_shipment()),
                int(product.get_reference()),
                product.get_color(),
                product.get_meter(),
                int(product.get_price()),)

            Database.query((''' INSERT INTO Products(id_product, id_order, id_shipment,reference,color,meter,price)
                  VALUES(?,?,?,?,?,?,?) ''', (values,)))

        except(ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def delete_product(self, id_product):
        """Delete a product with its reference"""
        Database.query(('''DELETE FROM Products WHERE id_product = ?''', (id_product,)))

    def get_product(self, id_order):
        """Give the list of products in the order defined by its id"""
        query_order = Database.query(('''SELECT * FROM Products WHERE id_order = ?''',
                                      (id_order,)))
        products = query_order.fetchone()
        if products is not None:
            return self.__list_to_dic_product(products)
        else:
            return products

    def update_product(self, product):
        """Update product"""
        try:
            values = (int(product.get_id_product()),
                      int(product.get_id_order()),
                      int(product.get_id_shipment()),
                      int(product.get_reference()),
                      product.get_color(),
                      product.get_meter(),
                      int(product.get_price()),
                      int(product.get_id_product()))
            Database.query(('''UPDATE Products 
                SET id_product = ?,
                    id_order = ?,
                    id_shipment = ?,
                    reference = ?, 
                    color = ?, 
                    meter = ?, 
                    price = ?
                    WHERE id_product = ?''', values))
        except (ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def set_id_shipment(self, id_product, id_shipment):
        try:
            Database.query(('''UPDATE Products SET id_shipment = ? WHERE id_product = ?''', (id_shipment, id_product)))
        except(ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def __list_to_dic_product(self, product):
        return {"id_order": product[0],
                "supplier": product[1],
                "client": product[2],
                "expected_delivery_date": product[3],
                "payment_type": product[4]}
