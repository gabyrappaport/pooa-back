import werkzeug
from flask import request
from flask_restful import Resource

from Controllers.Helper import WritingDataBaseError
from Controllers.Helper.HttpResponse import HttpResponse, HttpStatus
from DataBase.PartnerDataBase import PartnerDataBase
from Models.Partner import Partner

""" 
REST API for Partners. 

Note 1 :
We are using flask_restful, which forces us to create only one of each HTTP Methods,
Thus, we have only one public GET which calls several private ones.
 
Note 2 : 
The project aims to be more consistent and longer, especially for the front.
This is why some HTTP Methods are not yet called by the front, like DELETE or PUT,
but are still necessary and fully working.
"""


class PartnerController(Resource):

    def __init__(self):
        self.partner_db = PartnerDataBase()

    def get(self):
        try:
            if request.args.get("id_partner"):
                return self.__get_partner_by_id(request.args.get("id_partner"))

            elif request.args.get("partner_type"):
                return self.__get_partners_by_type(request.args.get("partner_type"))

            elif request.args.get("unpaid"):
                return self.__get_nbr_unpaid_order_by_partner()

            elif request.args.get("undelivered"):
                return self.__get_nbr_undelivered_order_by_partner()
            else:
                return self.__get_all_partners()
        except (werkzeug.exceptions.BadRequest, ValueError) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def __get_all_partners(self):
        return HttpResponse(HttpStatus.OK,
                            data=self.partner_db.get_all_partners()).get_response()

    def __get_partner_by_id(self, id_partner):
        partner = self.partner_db.get_partner(id_partner)
        return HttpResponse(HttpStatus.OK,
                            data=partner).get_response()

    def __get_partners_by_type(self, partner_type):
        if partner_type == "supplier":
            suppliers = self.partner_db.get_suppliers()
            return HttpResponse(HttpStatus.OK,
                                data=suppliers).get_response()
        elif partner_type == "client":
            clients = self.partner_db.get_clients()
            return HttpResponse(HttpStatus.OK,
                                data=clients).get_response()

    def __get_nbr_unpaid_order_by_partner(self):
        nbr_unpaid_order = self.partner_db.get_nbr_unpaid_order_by_partner()
        return HttpResponse(HttpStatus.OK,
                            data=nbr_unpaid_order).get_response()

    def __get_nbr_undelivered_order_by_partner(self):
        return HttpResponse(HttpStatus.OK,
                            data=self.partner_db.get_nbr_undelivered_order_by_partner()).get_response()

    def post(self):
        try:
            data = request.get_json(force=True)
            partner = Partner(str(data["partner_type"]),
                              str(data["company"]))
            self.partner_db.add_partner(partner)
            return HttpResponse(HttpStatus.OK).get_response()
        except (ValueError, TypeError, WritingDataBaseError, KeyError, werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def put(self):
        try:
            data = request.get_json(force=True)
            partner = Partner(str(data["partner_type"]),
                              str(data["company"]),
                              id_partner=int(data["id_partner"]))
            self.partner_db.update_partner(partner)
            return HttpResponse(HttpStatus.OK).get_response()
        except (ValueError, TypeError, WritingDataBaseError, KeyError, werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def delete(self):
        try:
            id_partner = request.args.get("id_partner")
            self.partner_db.delete_partner(id_partner)
            return HttpResponse(HttpStatus.OK).get_response()
        except (werkzeug.exceptions.BadRequest, ValueError) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()
