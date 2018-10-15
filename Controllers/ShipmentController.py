import datetime

import werkzeug
from flask import request
from flask_restful import Resource

from Controllers.Helper import WritingDataBaseError
from Controllers.Helper.HttpResponse import HttpResponse, HttpStatus
from DataBase.ShipmentDataBase import ShipmentDataBase
from Models.Shipment import Shipment


class ShipmentController(Resource):

    def __init__(self):
        self.shipment_db = ShipmentDataBase()

    def get(self):
        # ATTENTION, il faudra pas oublier d'ajouter les products
        try:
            if request.args.get("expedition_date"):
                shipments = self.shipment_db.get_shipments_expedition_date(request.args.get("expedition_date")])
                return HttpResponse(HttpStatus.OK,
                                    data=shipments).get_response()
            elif request.args.get("id_order"):
                shipments = self.shipment_db.get_shipments_id_order(request.args.get("id_order"))
                return HttpResponse(HttpStatus.OK,
                                    data=shipments).get_response()
            elif request.args.get("id_shipment"):
                shipments = self.shipment_db.get_shipment_id_shipment(request.args.get("id_shipment"))
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
            # for id_product in data["products"]:
            # ProductDataBase.indicate_shipment_date(id_product, shipment.get__id_shipment)
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
            # for id_product in data["added_products"]:
            # ProductDataBase.indicate_id_shipment(id_product, shipment.get__id_shipment)
            # for id_product in data["removed_products"]:
            # ProductDataBase.delete_id_shipment(id_product)
            return HttpResponse(HttpStatus.OK).get_response()
        except (ValueError, WritingDataBaseError, KeyError, werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def delete(self):
        try:
            data = request.get_json(force=True)
            self.shipment_db.delete_shipment(data["id_shipment"])
            return HttpResponse(HttpStatus.OK).get_response()
        except (werkzeug.exceptions.BadRequest, ValueError) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()
