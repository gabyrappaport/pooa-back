import datetime

import werkzeug
from flask import request
from flask_restful import Resource

from Controllers.Helper.HttpResponse import HttpResponse, HttpStatus
from DataBase.OrderDataBase import *
from DataBase.ProductDataBase import ProductDatabase
from Models.Order import *
from Models.Product import Product


class OrderController(Resource):

    def __init__(self):
        self.order_db = OrderDataBase()
        self.product_db = ProductDatabase()

    def get(self):
        try:
            if request.args.get("id_order"):
                id_order = request.args.get("id_order")
                order = self.order_db.get_order(id_order)
                if order is not None:
                    order["products"] = self.product_db.get_products(id_order)
                return HttpResponse(HttpStatus.OK,
                                    data=order).get_response()
            else:
                orders = self.order_db.get_all_orders()
                for order in orders:
                    order["products"] = self.product_db.get_products(order["id_order"])
                return HttpResponse(HttpStatus.OK,
                                    data=orders).get_response()
        except (werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def post(self):
        try:
            data = request.get_json(force=True)
            order = Order(int(data["id_supplier"]),
                          int(data["id_client"]),
                          datetime.datetime.strptime(data["expected_delivery_date"], "%d-%m-%Y").date(),
                          str(data["payment_type"]),
                          str(data["l_dips"]),
                          str(data["appro_ship_sample"]),
                          str(data["appro_s_off"]),
                          str(data["ship_sample_2h"]))
            products = []
            total_amount = 0
            for p in data["products"]:
                product = Product(int(order.get_id_order()),
                                  str(p["reference"]),
                                  str(p["color"]),
                                  float(p["meter"]),
                                  float(p["price"]),
                                  float(p["commission"]))
                products.append(product)
                self.product_db.add_product(product)
                total_amount += float(p["commission"]) * float(p["price"]) * float(p["meter"])
            order.set_total_amount(total_amount)
            self.order_db.add_order(order)
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
                          str(data["l_dips"]),
                          str(data["appro_ship_sample"]),
                          str(data["appro_s_off"]),
                          str(data["ship_sample_2h"]),
                          id_order=int(data["id_order"]))
            id_products_keep = []
            total_amount = 0
            for p in data["products"]:
                if "id_product" in p.keys():
                    product = Product(int(order.get_id_order()),
                                      str(p["reference"]),
                                      str(p["color"]),
                                      float(p["meter"]),
                                      float(p["price"]),
                                      float(p["commission"]),
                                      id_product=int(p["id_product"]))
                    total_amount += float(p["commission"]) * float(p["price"]) * float(p["meter"])
                    self.product_db.update_product(product)
                else:
                    product = Product(int(order.get_id_order()),
                                      str(p["reference"]),
                                      str(p["color"]),
                                      float(p["meter"]),
                                      float(p["price"]),
                                      float(p["commission"]))
                    total_amount += float(p["commission"]) * float(p["price"]) * float(p["meter"])
                    self.product_db.add_product(product)
                id_products_keep.append(product.get_id_product())
            order.set_total_amount(total_amount)
            self.order_db.update_order(order)
            self.product_db.delete_old_products(order.get_id_order(), id_products_keep)
            return HttpResponse(HttpStatus.OK).get_response()
        except (ValueError, WritingDataBaseError, KeyError, werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def delete(self):
        try:
            id_order = request.args.get("id_order")
            self.order_db.delete_order(id_order)
            products = self.product_db.get_products(id_order)
            for i in products:
                self.product_db.delete_product(i["id_product"])
            return HttpResponse(HttpStatus.OK).get_response()
        except (werkzeug.exceptions.BadRequest, ValueError) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()