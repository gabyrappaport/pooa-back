import werkzeug
from flask import request
from flask_restful import Resource
from datetime import datetime
from dateutil.relativedelta import relativedelta

from Controllers.Helper.HttpResponse import HttpResponse, HttpStatus
from DataBase.OrderDataBase import *
from DataBase.PartnerDataBase import *

""" 
REST API for Dashboard.

It is used to retrieve datas on the dollar amount brought by customers and suppliers per month.
"""


class DashboardController(Resource):

    def __init__(self):
        self.order_db = OrderDataBase()
        self.partner_db = PartnerDataBase()

    def get(self):
        try:
            number_of_months = 8
            x_month_ago = datetime.today() - relativedelta(months=number_of_months - 1)
            months = [(x_month_ago + relativedelta(months=i)).strftime('%m/%Y') for i in range(number_of_months)]
            partners = self.partner_db.get_partner_ids(request.args.get("partner_type"), number_of_months)
            partner_stats = self.order_db.partner_income(request.args.get("partner_type"), months, partners)
            data = {"months": months, "partner_stats": partner_stats}
            return HttpResponse(HttpStatus.OK,
                                data=data).get_response()
        except (werkzeug.exceptions.BadRequest, ValueError, TypeError) as e:
            return HttpResponse(HttpStatus.Bad_Request, data=str(e)).get_response()
