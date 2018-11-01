import werkzeug
from flask import request
from flask_restful import Resource

from Controllers.Helper.HttpResponse import HttpResponse, HttpStatus
from DataBase.OrderDataBase import *


class DashboardController(Resource):

    def __init__(self):
        self.order_db = OrderDataBase()

    def get(self):
        """Using Resource forces us to create REST APIs with only one GET"""
        try:
            # Month must be a number like mm
            month = request.args.get("month")
            if request.args.get("partner_type") == 'client':
                data = self.order_db.client_income(month)
                return HttpResponse(HttpStatus.OK,
                                    data=data).get_response()
            elif request.args.get("partner_type") == 'supplier':
                data = self.order_db.supplier_income(month)
                return HttpResponse(HttpStatus.OK,
                                    data=data).get_response()
        except (werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()
