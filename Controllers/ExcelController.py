import datetime

import werkzeug
from flask import request
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
from Controllers.Helper.Generate_excel import Generate_excel
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
            order_db = self.order_db.get_order(id_order) # interoge la BDD pour récuperer les infos sur l'ordre - dict
            if order_db is not None:
                products = []
                # total_amount = 0
                for p in order_db["products"]:
                    product = Product(int(id_order),
                                      str(p["reference"]),
                                      str(p["color"]),
                                      float(p["meter"]),
                                      float(p["price"]),
                                      float(p["commission"]),
                                      id_shipment=int(p["id_shipment"]),
                                      id_product=p["id_product"])
                    products.append(product)
                    # self.product_db.add_product(product) ON NE VEUT PAS AJOUTER UN PRODUIT A LA BDD
                    # total_amount += float(p["commission"]) * float(p["price"]) * float(p["meter"])
                # order.set_total_amount(total_amount) NOTRE TOTAL AMOUNT EST DEJA DANS LA BDD
                # self.order_db.add_order(order)

                order = Order(int(order_db["id_supplier"]),
                              int(order_db["id_client"]),
                              datetime.datetime.strptime(order_db["expected_delivery_date"], "%d-%m-%Y").date(),
                              str(order_db["payment_type"]),
                              str(order_db["l_dips"]),
                              str(order_db["appro_ship_sample"]),
                              str(order_db["appro_s_off"]),
                              str(order_db["ship_sample_2h"]),
                              total_amount=str(order_db["total_amount"]),
                              creation_date=datetime.datetime.strptime(order_db["creation_date"], "%d-%m-%Y").date(),
                              id_order=int(order_db["id_order"]),
                              products=products)
                client_db = self.partner_db.get_partner(int(order_db["id_client"]))
                client = Partner(str(client_db["partner_type"]),
                                 str(client_db["company"]),
                                 id_partner=int(client_db["id_partner"]))

                supplier_db = self.partner_db.get_partner(int(order_db["id_supplier"]))
                supplier = Partner(str(supplier_db["partner_type"]),
                                   str(supplier_db["company"]),
                                   id_partner=int(supplier_db["id_partner"]))

                shipment_db = self.shipment_db.get_shipments_id_order(id_order)
                shipment_obj = Shipment(shipment_db["expedition_date"],
                                        shipment_db["transportation"],
                                        shipment_db["departure_location"],
                                        shipment_db["arrival_location"],
                                        products=shipment_db["products"],
                                        id_shipment=shipment_db["id_shipment"])
                excel = Generate_excel()
                excel.generate_excel(order, client, supplier, shipment_obj)
                return excel
            else:
                raise NotImplementedError("error, please type a valid id_order")
            # return HttpResponse(HttpStatus.OK,data=order).get_response() Pourquoi ?

