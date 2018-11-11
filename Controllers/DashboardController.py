import werkzeug
from flask import request
from flask_restful import Resource

from Controllers.Helper.HttpResponse import HttpResponse, HttpStatus
from DataBase.OrderDataBase import *

""" 
REST API for Dashboard.

It is used to retrieves datas on the dollar amount brought by customers and suppliers per month.
"""


class DashboardController(Resource):

    def __init__(self):
        self.order_db = OrderDataBase()

    def get(self):
        try:
            data = self.order_db.partner_income(request.args.get("partner_type"))
            return HttpResponse(HttpStatus.OK,
                                data=data).get_response()
        except (werkzeug.exceptions.BadRequest, ValueError, TypeError) as e:
            return HttpResponse(HttpStatus.Bad_Request, data=str(e)).get_response()
