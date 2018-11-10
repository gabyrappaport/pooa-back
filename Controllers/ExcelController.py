import os

from flask import request, send_from_directory
from flask_restful import Resource

# from Models.Shipment import Shipment
from Controllers.Helper.GenerateExcel import GenerateExcel
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
        """ First part of the function : recovery of order data """
        if not request.args.get("id_order"):
            raise NameError("error, please type 'id_order=' with a valid id_order")

        if request.args.get("id_order"):
            id_order = request.args.get("id_order")
            order_db = self.order_db.get_order(id_order)

            # We create an Order object with the information in the database
            if order_db is not None:
                total_amount = 0
                order = ExcelController.__get_order_info(order_db)
                if self.product_db.get_products(id_order) is not None:
                    order_db["products"] = self.product_db.get_products(id_order)
                    products = []
                    # We create a Product object thanks to information in order_db
                    for p in order_db["products"]:
                        product, amount_product = ExcelController.__get_info_product(id_order, p)
                        total_amount += amount_product
                        products.append(product)
                else:
                    raise ValueError("there isn't any product in your order")
            else:
                raise ValueError("please enter a valid id_order")
            # We update this information on the order project
            order.products = products
            order.total_amount = total_amount
            # We have now all the information we need about the specific order

            """Second part of the function : recovery of client data"""
            client_db = self.partner_db.get_partner(int(order_db["id_client"]))
            client = ExcelController.__get_partner_info(client_db)

            """Third part of the function : recovery of supplier data"""
            supplier_db = self.partner_db.get_partner(int(order_db["id_supplier"]))
            supplier = ExcelController.__get_partner_info(supplier_db)

            """Fourth part of the function :information about the excel file"""

            filename = "Excel_order_" + str(id_order) + ".xlsx"
            uploads = os.path.join("public", "excels")

            """" Generation of the excel file"""
            excel = GenerateExcel()
            excel.generate_excel(order, client, supplier, uploads + "/" + filename, order.get_number_of_products())
            return send_from_directory(directory=uploads, filename=filename)
        else:
            raise NameError("error, please type 'id_order=' with a valid id_order")

    @staticmethod
    def __get_order_info(order_db):
        """We create an Order object thanks information in the database"""
        if order_db is None:
            raise ValueError("please enter a valid id_order")
        if order_db is not None:
            print (type(datetime.datetime.strptime(order_db["expected_delivery_date"], "%Y-%m-%d").date()))
            print("good")
            order = Order(int(order_db["id_supplier"]),
                          int(order_db["id_client"]),
                          datetime.datetime.strptime(order_db["expected_delivery_date"], "%Y-%m-%d").date(),
                          str(order_db["payment_type"]),
                          str(order_db["l_dips"]),
                          str(order_db["appro_ship_sample"]),
                          str(order_db["appro_s_off"]),
                          str(order_db["ship_sample_2h"]),
                          total_amount=str(order_db["total_amount"]),
                          creation_date=(order_db["creation_date"]),
                          id_order=int(order_db["id_order"])
                          )
            return order

    @staticmethod
    def __get_info_product(id_order, p):
        total_amount = 0
        product = Product(int(id_order),
                          str(p["reference"]),
                          str(p["color"]),
                          float(p["meter"]),
                          float(p["price"]),
                          float(p["commission"]),
                          id_product=p["id_product"])
        # We compute the total amount of each product that we want to display on the excel file
        total_amount += float(p["price"]) * float(p["meter"])

        return product, total_amount

    @staticmethod
    def __get_partner_info(partner_db):
        partner = Partner(str(partner_db["partner_type"]),
                          str(partner_db["company"]), id_partner=int(partner_db["id_partner"]))
        return partner
