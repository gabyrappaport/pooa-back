from flask_restful import Resource
from flask import request, redirect, url_for, session

from Controllers.Helper import WritingDataBaseError
from Controllers.Helper.HttpResponse import HttpResponse, HttpStatus
from DataBase.UserDataBase import UserDataBase


class LogoutController(Resource):

    def __init__(self):
        self.user_db = UserDataBase()

    def get(self):
        pass

    def post(self):
        # regarder quelle est la session et remplacer le mon_email par none
        session.pop("email", None)
        return HttpResponse(HttpStatus.OK).get_response()