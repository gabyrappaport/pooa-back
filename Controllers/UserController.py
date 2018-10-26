from flask_restful import Resource
from flask import request, session

import hashlib
import werkzeug
from Controllers.Helper import WritingDataBaseError
from Controllers.Helper.HttpResponse import HttpResponse, HttpStatus
from DataBase.UserDataBase import UserDataBase
from Models.User import User


class UserController(Resource):

    def __init__(self):
        self.user_db = UserDataBase()

    def get(self):
        try:
            if request.args.get("id_user"):
                id_user = request.args.get("id_user")
                user = self.user_db.get_user(id_user)
                return HttpResponse(HttpStatus.OK,
                                    data=user).get_response()
            else:
                users = self.user_db.get_all_users()
                return HttpResponse(HttpStatus.OK,
                                    data=users).get_response()
        except (ValueError, werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def post(self):
        try:
            data = request.get_json(force=True)
            password = hashlib.sha256(str(data["password"]).encode("utf-8")).hexdigest()
            user = User(str(data["name"]),
                        str(data["surname"]),
                        str(data["email"]),
                        password,
                        str(data["user_type"]))
            self.user_db.add_user(user)
            return HttpResponse(HttpStatus.OK).get_response()
        except (ValueError, werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def put(self):
        try:
            data = request.get_json(force=True)
            password = hashlib.sha256(str(data["password"]).encode("utf-8")).hexdigest()
            user = User(str(data["name"]),
                        str(data["surname"]),
                        str(data["email"]),
                        password,
                        str(data["user_type"]),
                        id_user=int(data["id_user"]))
            self.user_db.update_user(user)
            return HttpResponse(HttpStatus.OK).get_response()
        except (ValueError, WritingDataBaseError, KeyError, werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def delete(self):
        try:
            id_user = request.args.get("id_user")
            self.user_db.delete_user(id_user)
            return HttpResponse(HttpStatus.OK).get_response()
        except (werkzeug.exceptions.BadRequest, ValueError) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()
