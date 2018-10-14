import werkzeug
from flask import request
from flask_restful import Resource

from Controllers.Helper.HttpResponse import HttpResponse, HttpStatus
from Controllers.Helper import WritingDataBaseError
from DataBase.PartnerDataBase import PartnerDataBase

from Models.Partner import Partner


class PartnerController(Resource):

    def __init__(self):
        self.partner_db = PartnerDataBase()

    def get(self):
        try:
            if request.data:
                data = request.get_json(force=True)
                if "id_partner" in data.keys():
                    partner = self.partner_db.get_partner(data["id_partner"])
                    return HttpResponse(HttpStatus.OK,
                                        data=partner).get_response()
                elif "partner_type" in data.keys():
                    if data["partner_type"] == "supplier":
                        suppliers = self.partner_db.get_suppliers()
                        return HttpResponse(HttpStatus.OK,
                                            data=suppliers).get_response()
                    elif data["partner_type"] == "client":
                        clients = self.partner_db.get_clients()
                        return HttpResponse(HttpStatus.OK,
                                            data=clients).get_response()
            else:
                return HttpResponse(HttpStatus.OK,
                                    data=self.partner_db.get_all_partners()).get_response()
        except (werkzeug.exceptions.BadRequest, ValueError) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def post(self):
        try:
            data = request.get_json(force=True)
            partner = Partner(str(data["partner_type"]),
                              str(data["company"]))
            self.partner_db.add_partner(partner)
            return HttpResponse(HttpStatus.OK).get_response()
        except (ValueError, WritingDataBaseError, KeyError, werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def put(self):
        try:
            data = request.get_json(force=True)
            partner = Partner(str(data["partner_type"]),
                              str(data["company"]),
                              id_partner=int(data["id_partner"]))
            self.partner_db.update_partner(partner)
            return HttpResponse(HttpStatus.OK).get_response()
        except (ValueError, WritingDataBaseError, KeyError, werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def delete(self): #delete by id mais est_ce qu'on connaît l'id ?
        try:
            data = request.get_json(force=True)
            self.partner_db.delete_partner(data["id_partner"])
            return HttpResponse(HttpStatus.OK).get_response()
        except (werkzeug.exceptions.BadRequest, ValueError) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()