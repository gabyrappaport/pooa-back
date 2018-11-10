import datetime

import werkzeug
from flask import request
from flask_restful import Resource

from Controllers.Helper import WritingDataBaseError
from Controllers.Helper.HttpResponse import HttpResponse, HttpStatus
from DataBase.ProductDataBase import ProductDatabase
from DataBase.ShipmentDataBase import ShipmentDataBase
from Models.Shipment import Shipment

""" 
REST API for Shipments. 

Note 1 :
We are using flask_restful, which forces us to create only one of each HTTP Methods,
Thus, we have only one public GET which calls several private ones.

Note 2 : 
The project aims to be more consistent and longer, especially for the front.
This is why some HTTP Methods are not yet called by the front, like DELETE or PUT,
but are still necessary and fully working.
"""


class ShipmentController(Resource):

    def __init__(self):
        self.shipment_db = ShipmentDataBase()
        self.product_db = ProductDatabase()

    def get(self):
        try:
            if request.args.get("expedition_date"):
                return self.__get_shipments_by_expedition_date(request.args.get("expedition_date"))
            elif request.args.get("id_order"):
                return self.__get_shipments_by_id_order(request.args.get("id_order"))
            elif request.args.get("id_shipment"):
                return self.__get_shipment_by_id_shipment(request.args.get("id_shipment"))
            else:
                return self.__get_shipment_all_shipments()
        except (ValueError, werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def __get_shipments_by_id_order(self, id_order):
        shipments = self.shipment_db.get_shipments_id_order(id_order)
        self.__set_products(shipments)
        return HttpResponse(HttpStatus.OK,
                            data=shipments).get_response()

    def __get_shipments_by_expedition_date(self, expedition_date):
        shipments = self.shipment_db.get_shipments_expedition_date(expedition_date)
        self.__set_products(shipments)
        return HttpResponse(HttpStatus.OK,
                            data=shipments).get_response()

    def __get_shipment_by_id_shipment(self, id_shipment):
        shipment = self.shipment_db.get_shipment_id_shipment(id_shipment)
        if shipment is not None:
            self.__set_products(shipment)
        return HttpResponse(HttpStatus.OK,
                            data=shipment).get_response()

    def __get_shipment_all_shipments(self):
        shipments = self.shipment_db.get_all_shipments()
        self.__set_products(shipments)
        return HttpResponse(HttpStatus.OK,
                            data=shipments).get_response()

    def __set_products(self, shipments):
        if shipments is None:
            return
        if type(shipments) == list:
            for s in shipments:
                s['products'] = self.product_db.get_products_from_id_shipment(s['id_shipment'])
        else:
            shipments["products"] = self.product_db.get_products_from_id_shipment(shipments['id_shipment'])

    def post(self):
        try:
            data = request.get_json(force=True)
            shipment = self.__shipment_from_data(data)
            id_shipment = self.shipment_db.add_shipment(shipment)
            if "products" in data.keys():
                for id_product in data["products"]:
                    self.product_db.set_id_shipment(id_product, id_shipment)
            return HttpResponse(HttpStatus.OK).get_response()
        except (ValueError, WritingDataBaseError, KeyError, werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def put(self):
        try:
            data = request.get_json(force=True)
            shipment = self.__shipment_from_data(data)
            self.shipment_db.update_shipment(shipment)
            for id_product in data["added_products"]:
                self.product_db.set_id_shipment(id_product, shipment.id_shipment)
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

    def __get_shipments_by_id_order(self, id_order):
        shipments = self.shipment_db.get_shipments_id_order(id_order)
        self.__set_products(shipments)
        return HttpResponse(HttpStatus.OK,
                            data=shipments).get_response()

    def __get_shipments_by_expedition_date(self, expedition_date):
        shipments = self.shipment_db.get_shipments_expedition_date(expedition_date)
        self.__set_products(shipments)
        return HttpResponse(HttpStatus.OK,
                            data=shipments).get_response()

    def __get_shipment_by_id_shipment(self, id_shipment):
        shipment = self.shipment_db.get_shipment_id_shipment(id_shipment)
        self.__set_products(shipment)
        return HttpResponse(HttpStatus.OK,
                            data=shipment).get_response()

    def __get_shipment_all_shipments(self):
        shipments = self.shipment_db.get_all_shipments()
        self.__set_products(shipments)
        return HttpResponse(HttpStatus.OK,
                            data=shipments).get_response()

    def __set_products(self, shipments):
        if shipments is None:
            return
        if type(shipments) == list:
            for s in shipments:
                s['products'] = self.product_db.get_products_from_id_shipment(s['id_shipment'])
        else:
            shipments["products"] = self.product_db.get_products_from_id_shipment(shipments['id_shipment'])

    def __shipment_from_data(self, data):
        shipment = Shipment(datetime.datetime.strptime(data["expedition_date"], "%Y-%m-%d").date(),
                            str(data["transportation"]),
                            str(data["departure_location"]),
                            str(data["arrival_location"]))
        if "id_shipment" in data.keys():
            shipment.set_id_shipment(int(data["id_shipment"]))
        return shipment
