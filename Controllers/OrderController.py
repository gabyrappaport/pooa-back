import datetime

import werkzeug
from flask import request
from flask_restful import Resource

from Controllers.Helper.HttpResponse import HttpResponse, HttpStatus
from DataBase.OrderDataBase import *
from Models.Order import *
from Models.Product import Product


class OrderController(Resource):

    def __init__(self):
        self.order_db = OrderDataBase()

    def get(self):
        try:
            if request.data:
                data = request.get_json(force=True)
                order = self.order_db.get_order(data["id_order"])
                #products = self.product_db.get_products(data["id_order"])
                # query_products = self.productTable.get_products(id_order)
                return HttpResponse(HttpStatus.OK,
                                    data=order).get_response()
            else:
                #Attention products
                return HttpResponse(HttpStatus.OK,
                                    data=self.order_db.get_all_orders()).get_response()
        except (werkzeug.exceptions.BadRequest, ValueError) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def post(self):
        try:
            data = request.get_json(force=True)
            order = Order(int(data["supplier"]),
                          int(data["client"]),
                          datetime.datetime.strptime(data["expected_delivery_date"], "%d-%m-%Y").date(),
                          str(data["payment_type"]))
            self.order_db.add_order(order)
            products = []
            for p in data["products"]:
                product = Product(int(order.get_id_order()),
                                  str(p["reference"]),
                                  str(p["color"]),
                                  float(p["meter"]),
                                  float(p["price"]))
                products.append(product)
                # ProductDataBase.add_product(product)
            return HttpResponse(HttpStatus.OK).get_response()
        except (ValueError, WritingDataBaseError, KeyError, werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def put(self):
        try:
            data = request.get_json(force=True)
            order = Order(int(data["supplier"]),
                          int(data["client"]),
                          datetime.datetime.strptime(data["expected_delivery_date"], "%d-%m-%Y").date(),
                          str(data["payment_type"]),
                          id_order=int(data["id_order"]))
            self.order_db.update_order(order)
            products = []
            for p in data["products"]:
                if "id_product" in p.keys():
                    product = Product(int(order.get_id_order()),
                                      str(p["reference"]),
                                      str(p["color"]),
                                      float(p["meter"]),
                                      float(p["price"]),
                                      id_product=int(p["id_product"]))
                    # ProductDataBase.update_product(product)
                else:
                    product = Product(int(order.get_id_order()),
                                      str(p["reference"]),
                                      str(p["color"]),
                                      float(p["meter"]),
                                      float(p["price"]))
                    # ProductDataBase.add_product(product)
                products.append(product)
            return HttpResponse(HttpStatus.OK).get_response()
        except (ValueError, WritingDataBaseError, KeyError, werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def delete(self):
        try:
            data = request.get_json(force=True)
            self.order_db.delete_order(data["id_order"])
            return HttpResponse(HttpStatus.OK).get_response()
        except (werkzeug.exceptions.BadRequest, ValueError) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()
