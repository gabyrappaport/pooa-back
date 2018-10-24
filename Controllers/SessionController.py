import hashlib
from flask_restful import Resource
from flask import request, redirect, url_for, session

from Controllers.Helper import WritingDataBaseError
from Controllers.Helper.HttpResponse import HttpResponse, HttpStatus
from DataBase.UserDataBase import UserDataBase
from Models.User import User


class SessionContoller(Resource):

    def __init__(self):
        self.user_db = UserDataBase()

    def get(self):
        pass

    def post(self):
        email = request.form["email"]
        password = request.form["password"]
        password_hash = hashlib.sha256(str(password).encode("utf-8")).hexdigest()
        if not self.user_db.check_user(email, password_hash):
            session['e_mail'] = None
            return HttpResponse(HttpStatus.Unauthorized).get_response()
        else:
            session["email"] = request.form["email"]
            return HttpResponse(HttpStatus.OK).get_response()

    def delete(self):
        pass
