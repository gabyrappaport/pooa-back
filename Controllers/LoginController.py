import hashlib
from flask_restful import Resource
from flask import request, session

from Controllers.Helper.HttpResponse import HttpResponse, HttpStatus
from DataBase.UserDataBase import UserDataBase


class LoginController(Resource):

    def __init__(self):
        self.user_db = UserDataBase()

    def post(self):
        data = request.get_json(force=True)
        email = str(data["email"])
        password = str(data["password"])
        password_hash = hashlib.sha256(str(password).encode("utf-8")).hexdigest()
        print(self.user_db.check_user(email, password_hash))
        if not self.user_db.check_user(email, password_hash):
            #session['email'] = None
            return HttpResponse(HttpStatus.Unauthorized).get_response()
        else:
            #session['email'] = email
            return HttpResponse(HttpStatus.OK).get_response()
