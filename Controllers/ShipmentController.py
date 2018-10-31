import datetime

import werkzeug
from flask import request
from flask_restful import Resource

from Controllers.Helper import WritingDataBaseError
from Controllers.Helper.HttpResponse import HttpResponse, HttpStatus
from DataBase.ShipmentDataBase import ShipmentDataBase
from Models.Shipment import Shipment
from DataBase.ProductDataBase import ProductDatabase


class ShipmentController(Resource):

    def __init__(self):
        self.shipment_db = ShipmentDataBase()
        self.product_db = ProductDatabase()

    def get(self):
        """Using Resource forces us to create REST APIs with only one GET"""
        try:
            if request.args.get("expedition_date"):
                shipments = self.shipment_db.get_shipments_expedition_date(request.args.get("expedition_date"))

            elif request.args.get("id_order"):
                shipments = self.shipment_db.get_shipments_id_order(request.args.get("id_order"))

            elif request.args.get("id_shipment"):
                shipments = self.shipment_db.get_shipment_id_shipment(request.args.get("id_shipment"))

            if len(shipments) > 1:
                shipments_list = []
                for shipment in shipments:
                    list_product = self.product_db.get_products_from_id_shipment(shipment['id_shipment'])
                    shipment["products"] = list_product
                    shipments_list.append(shipment)
                return HttpResponse(HttpStatus.OK,
                                    data=shipments_list).get_response()
            elif len(shipments) == 1:
                list_product = self.product_db.get_products_from_id_shipment(shipments[0]['id_shipment'])
                shipments[0]['products'] = list_product
                return HttpResponse(HttpStatus.OK,
                                    data=shipments).get_response()
            else:
                return HttpResponse(HttpStatus.OK,
                                    data=self.shipment_db.get_all_shipments()).get_response()
        except (ValueError, werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def post(self):
        try:
            data = request.get_json(force=True)
            shipment = Shipment(datetime.datetime.strptime(data["expedition_date"], "%d-%m-%Y").date(),
                                str(data["transportation"]),
                                str(data["departure_location"]),
                                str(data["arrival_location"]))
            self.shipment_db.add_shipment(shipment)
            for id_product in data["products"]:
                self.product_db.set_id_shipment(id_product, shipment.get_id_shipment)
            return HttpResponse(HttpStatus.OK).get_response()
        except (ValueError, WritingDataBaseError, KeyError, werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def put(self):
        try:
            data = request.get_json(force=True)
            shipment = Shipment(datetime.datetime.strptime(data["expedition_date"], "%d-%m-%Y").date(),
                                str(data["transportation"]),
                                str(data["departure_location"]),
                                str(data["arrival_location"]),
                                id_shipment=int(data["id_shipment"]))
            self.shipment_db.update_shipment(shipment)
            for id_product in data["added_products"]:
                self.product_db.set_id_shipment(id_product, shipment.get_id_shipment)
            for id_product in data["removed_products"]:
                self.product_db.delete_id_shipment(id_product)
            return HttpResponse(HttpStatus.OK).get_response()
        except (ValueError, WritingDataBaseError, KeyError, werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def delete(self):
        try:
            id_shipment = request.args.get("id_shipment")
            self.shipment_db.delete_shipment(id_shipment)
            id_product_to_del = self.product_db.get_id_product_from_shipment(id_shipment)
            if id_product_to_del:
                for id_product in id_product_to_del:
                    self.product_db.delete_id_shipment(id_product)
            return HttpResponse(HttpStatus.OK).get_response()
        except (werkzeug.exceptions.BadRequest, ValueError) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()
