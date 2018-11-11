import werkzeug
from flask import request
from flask_restful import Resource

from Controllers.Helper.HttpResponse import HttpResponse, HttpStatus
from DataBase.OrderDataBase import *
from DataBase.ProductDataBase import ProductDatabase
from Models.Order import *
from Models.Product import Product

""" 
REST API for Orders. 

Note 1 :
We are using flask_restful, which forces us to create only one of each HTTP Methods,
Thus, we have only one public GET which calls several private ones.
 
Note 2 : 
The project aims to be more consistent and longer, especially for the front.
This is why some HTTP Methods are not yet called by the front, like DELETE or PUT,
but are still necessary and fully working.
"""


class OrderController(Resource):

    def __init__(self):
        self.order_db = OrderDataBase()
        self.product_db = ProductDatabase()

    def get(self):
        try:
            if request.args.get("id_order"):
                return self.__get_order_by_id(request.args.get("id_order"))
            else:
                return self.__get_all_orders()
        except (werkzeug.exceptions.BadRequest, ValueError, TypeError) as e:
            return HttpResponse(HttpStatus.Bad_Request, data=str(e)).get_response()

    def post(self):
        try:
            # Create new order
            data = request.get_json(force=True)
            order = self.__order_from_data(data)
            id_order = self.order_db.add_order(order)
            # Add products in new order and calculate total amount
            total_amount = 0
            for p in data["products"]:
                product = self.__product_from_data(id_order, p)
                self.product_db.add_product(product)
                total_amount += product.get_price_with_commission()
            self.order_db.set_total_amount(total_amount, id_order)
            return HttpResponse(HttpStatus.OK).get_response()
        except (ValueError, TypeError, WritingDataBaseError, KeyError, werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, data=str(e)).get_response()

    def put(self):
        try:
            data = request.get_json(force=True)
            order = self.__order_from_data(data)
            updated_total_amount = self.__update_products(order.id_order, data["products"])
            order.total_amount = updated_total_amount
            self.order_db.update_order(order)
            return HttpResponse(HttpStatus.OK).get_response()
        except (ValueError, TypeError, WritingDataBaseError, KeyError, werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, data=str(e)).get_response()

    def delete(self):
        try:
            id_order = request.args.get("id_order")
            self.order_db.delete_order(id_order)
            products = self.product_db.get_products(id_order)
            # Delete products of the deleted order.
            for i in products:
                self.product_db.delete_product(i["id_product"])
            return HttpResponse(HttpStatus.OK).get_response()
        except (werkzeug.exceptions.BadRequest, ValueError, TypeError) as e:
            return HttpResponse(HttpStatus.Bad_Request, data=str(e)).get_response()

    def __get_order_by_id(self, id_order):
        order = self.order_db.get_order(id_order)
        if order is not None:
            order["products"] = self.product_db.get_products(id_order)
        return HttpResponse(HttpStatus.OK,
                            data=order).get_response()

    def __get_all_orders(self):
        orders = self.order_db.get_all_orders()
        for order in orders:
            order["products"] = self.product_db.get_products(order["id_order"])
        return HttpResponse(HttpStatus.OK,
                            data=orders).get_response()

    def __update_products(self, id_order, products):
        products_in_order = []
        total_amount = 0
        for p in products: # dans p il y a mon nouveau produit
            product = self.__product_from_data(id_order, p)
            total_amount += product.get_price_with_commission()
            # If the product already has an id_product, it means it is already stored in the database,
            # so we only have to update it.
            if "id_product" in p.keys():
                self.product_db.update_product(product)
            # If the product doesn't have an id_product, it means it is a new product in the database,
            # so we need to add it.
            else:
                product.id_product = self.product_db.add_product(product)
            products_in_order.append(product.id_product)
        self.product_db.delete_old_products(id_order, products_in_order)
        return total_amount

    def __order_from_data(self, data):
        order = Order(int(data["id_supplier"]),
                      int(data["id_client"]),
                      datetime.datetime.strptime(data["expected_delivery_date"], "%Y-%m-%d").date(),
                      str(data["payment_type"]),
                      str(data["l_dips"]),
                      str(data["appro_ship_sample"]),
                      str(data["appro_s_off"]),
                      str(data["ship_sample_2h"]))
        if "id_order" in data.keys():
            order.id_order = data["id_order"]
        if "complete_payment_date" in data.keys() and data["complete_payment_date"] != -1:
            order.complete_payment_date = datetime.datetime.strptime(data["complete_payment_date"], "%Y-%m-%d").date()
        if "complete_delivery_date" in data.keys() and data["complete_delivery_date"] != -1:
            order.complete_delivery_date = datetime.datetime.strptime(data["complete_delivery_date"], "%Y-%m-%d").date()
        return order

    def __product_from_data(self, id_order, data_product):
        print(float(data_product["commission"]))
        product = Product(int(id_order),
                          str(data_product["reference"]),
                          str(data_product["color"]),
                          float(data_product["meter"]),
                          float(data_product["price"]),
                          float(data_product["commission"]))
        if "id_product" in data_product.keys():
            product.id_product = data_product["id_product"]
        return product
