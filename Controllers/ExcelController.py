import os
import werkzeug

from flask import request, send_from_directory
from flask_restful import Resource

from Controllers.Helper.GenerateExcel import GenerateExcel
from Controllers.Helper.HttpResponse import HttpResponse, HttpStatus
from DataBase.OrderDataBase import *
from DataBase.PartnerDataBase import PartnerDataBase
from DataBase.ProductDataBase import ProductDatabase
from DataBase.ShipmentDataBase import ShipmentDataBase
from Models.Order import *
from Models.Partner import Partner
from Models.Product import Product


class ExcelController(Resource):
    def __init__(self):
        self.order_db = OrderDataBase()
        self.product_db = ProductDatabase()
        self.partner_db = PartnerDataBase()
        self.shipment_db = ShipmentDataBase()

    def get(self):
        try:
            if request.args.get("id_order") is None:
                raise NameError("error, please type 'id_order=' with a valid id_order")
            else:
                """ Recovery of order data."""
                id_order = request.args.get("id_order")
                order_data = self.order_db.get_order(id_order)
                order = ExcelController.__order_from_data(order_data)

                """ Recovery of products order and total amount."""
                products, total_amount = self.__get_products_info_and_total_amount(id_order)
                order.set_products(products)
                order.set_total_amount(total_amount)

                """Recovery of order's client data."""
                client_data = self.partner_db.get_partner(int(order_data["id_client"]))
                client = ExcelController.__get_partner_info(client_data)
                
                """Recovery of order's supplier data."""
                supplier_data = self.partner_db.get_partner(int(order_data["id_supplier"]))
                supplier = ExcelController.__get_partner_info(supplier_data)

                """Information about the excel file."""
                filename = "Excel_order_" + str(id_order) + ".xlsx"
                uploads = os.path.join("public", "excels")

                """" Generation of the excel file."""
                excel = GenerateExcel()
                excel.generate_excel(order, client, supplier, uploads + "/" + filename, order.get_number_of_products())
                return send_from_directory(directory=uploads, filename=filename)

        except (ValueError, NameError, werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, data=str(e)).get_response()

    def __get_products_info_and_total_amount(self, id_order):
        # We create an Order object with the information in the database
        total_amount = 0
        order_products = self.product_db.get_products(id_order)
        products = []
        # We create a Product object thanks to information in order_data
        for p in order_products:
            product = ExcelController.__product_from_data(id_order, p)
            total_amount += product.get_price_per_product()
            products.append(product)
        return products, total_amount

    @staticmethod
    def __order_from_data(order_data):
        """We create an Order object thanks information in the database"""
        if order_data is None:
            raise ValueError("please enter a valid id_order")
        if order_data is not None:
            return Order(int(order_data["id_supplier"]),
                         int(order_data["id_client"]),
                         str(order_data["expected_delivery_date"]),
                         str(order_data["payment_type"]),
                         str(order_data["l_dips"]),
                         str(order_data["appro_ship_sample"]),
                         str(order_data["appro_s_off"]),
                         str(order_data["ship_sample_2h"]),
                         total_amount=str(order_data["total_amount"]),
                         creation_date=(order_data["creation_date"]),
                         id_order=int(order_data["id_order"]))

    @staticmethod
    def __product_from_data(id_order, p):
        return Product(int(id_order),
                       str(p["reference"]),
                       str(p["color"]),
                       float(p["meter"]),
                       float(p["price"]),
                       float(p["commission"]),
                       id_product=p["id_product"])

    @staticmethod
    def __get_partner_info(order_data):
        return Partner(str(order_data["partner_type"]),
                       str(order_data["company"]),
                       id_partner=int(order_data["id_partner"]))
