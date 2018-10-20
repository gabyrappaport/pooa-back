import datetime

import werkzeug
from flask import request
from flask_restful import Resource

from Controllers.Helper.HttpResponse import HttpResponse, HttpStatus
from DataBase.OrderDataBase import *
from DataBase.ProductDataBase import ProductDatabase
from DataBase.PartnerDataBase import PartnerDataBase
from Models.Order import *
from Models.Product import Product
from Models.ExcelModel import ExcelModel

class ExcelController(Resource):
    def __init__(self):
        self.order_db = OrderDataBase()
        self.product_db = ProductDatabase()
        self.partner_db = PartnerDataBase()

    def get(self):
        pass