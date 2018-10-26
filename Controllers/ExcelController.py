import datetime
import os
import werkzeug
from flask import request, send_from_directory
from flask_restful import Resource

from Controllers.Helper.HttpResponse import HttpResponse, HttpStatus
from DataBase.OrderDataBase import *
from DataBase.ProductDataBase import ProductDatabase
from DataBase.PartnerDataBase import PartnerDataBase
from DataBase.ShipmentDataBase import ShipmentDataBase
from Models.Order import *
from Models.Product import Product
from Models.Partner import Partner
from Models.Shipment import Shipment
from Controllers.Helper.Generate_excel import GenerateExcel
#from Models.ExcelModel import ExcelModel inutile car la mere est automatiquement importée


class ExcelController(Resource):
    def __init__(self):
        self.order_db = OrderDataBase()
        self.product_db = ProductDatabase()
        self.partner_db = PartnerDataBase()
        self.shipment_db = ShipmentDataBase()

    def get(self):
        if request.args.get("id_order"):
            id_order = request.args.get("id_order")
            order_db = self.order_db.get_order(id_order)
            if order_db is not None:
                total_amount = 0
                order = Order(int(order_db["supplier"]),
                              int(order_db["client"]),
                              str(order_db["expected_delivery_date"]),
                              str(order_db["payment_type"]),
                              str(order_db["l_dips"]),
                              str(order_db["appro_ship_sample"]),
                              str(order_db["appro_s_off"]),
                              str(order_db["ship_sample_2h"]),
                              total_amount=str(order_db["total_amount"]),
                              creation_date=(order_db["creation_date"]),
                              id_order=int(order_db["id_order"])
                              )

                order_db["products"] = self.product_db.get_products(id_order)
                products = []
                for p in order_db["products"]:
                    product = Product(int(id_order),
                                      str(p["reference"]),
                                      str(p["color"]),
                                      float(p["meter"]),
                                      float(p["price"]),
                                      float(p["commission"]),
                                      #id_shipment=int(p["id_shipment"]),
                                      id_product=p["id_product"])
                    total_amount += float(p["commission"]) * float(p["price"]) * float(p["meter"])
                    products.append(product)
                order.set_products(products)
                order.set_total_amount(total_amount) # NOTRE TOTAL AMOUNT EST DEJA DANS LA BDD
                client_db = self.partner_db.get_partner(int(order_db["client"]))
                client = Partner(str(client_db["partner_type"]),
                                 str(client_db["company"]),
                                 id_partner=int(client_db["id_partner"]))
                supplier_db = self.partner_db.get_partner(int(order_db["supplier"]))
                supplier = Partner(str(supplier_db["partner_type"]),
                                   str(supplier_db["company"]),
                                   id_partner=int(supplier_db["id_partner"]))
                # If we need shipment information
                #shipment_db = self.shipment_db.get_shipments_id_order(id_order)
                #shipment_obj = Shipment(shipment_db["expedition_date"],
                #                        shipment_db["transportation"],
                #                        shipment_db["departure_location"],
                #                        shipment_db["arrival_location"],
                #                        products=shipment_db["products"],
                #                        id_shipment=shipment_db["id_shipment"])
                filename = "Excel_order_" + str(id_order) + ".xlsx"
                uploads = os.path.join("public", "excels")
                excel = GenerateExcel()
                excel.generate_excel(order, client, supplier, uploads + "/" + filename, order.get_number_of_products())
                return send_from_directory(directory=uploads, filename=filename)

            else:
                raise NotImplementedError("error, please type a valid id_order")
