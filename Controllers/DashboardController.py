import werkzeug
from flask import request
from flask_restful import Resource

from Controllers.Helper.HttpResponse import HttpResponse, HttpStatus
from DataBase.OrderDataBase import *
from DataBase.ProductDataBase import ProductDatabase


class DashboardController(Resource):

    def __init__(self):
        self.order_db = OrderDataBase()
        self.product_db = ProductDatabase()

    def get(self):
        """Using Resource forces us to create REST APIs with only one GET"""
        try:
            # Month must be a number like mm
            # todo client vs supplier
            month = request.args.get("month")
            data = self.order_db.partner_income(month)
            return HttpResponse(HttpStatus.OK,
                                data=data).get_response()
        except (werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()
