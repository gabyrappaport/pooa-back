from flask_restful import Resource
from flask import Flask, request, render_template, flash,  redirect, url_for, session

import hashlib, uuid, os
import werkzeug
from werkzeug.utils import secure_filename
from Controllers.Helper import WritingDataBaseError
from Controllers.Helper.HttpResponse import HttpResponse, HttpStatus
from DataBase.UserDataBase import UserDataBase
from Models.User import User


class UserController(Resource):

    def __init__(self):
        self.user_db = UserDataBase()

    # def get(self):
    #     try:
    #
    #     except (ValueError, werkzeug.exceptions.BadRequest) as e:
    #         return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def post(self):
        try:
            data = request.get_json(force=True)
            password = hashlib.sha256(str(data["password"]).encode("utf-8")).hexdigest()
            user = (str(data["name"]),
                    str(data["surname"]),
                    str(data["email"]),
                    password,
                    str(data["user_type"]))
            self.user_db.add_user(user)
            session["email"] = data["email"]
            return HttpResponse(HttpStatus.OK).get_response()
        except (ValueError, werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def put(self):
        try:
            #TO DO with password hashing
            return HttpResponse(HttpStatus.OK).get_response()
        except (ValueError, WritingDataBaseError, KeyError, werkzeug.exceptions.BadRequest) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()

    def delete(self):
        try:
            id_user = request.args.get("id_user")
            self.shipment_db.delete_user(id_user)
            return HttpResponse(HttpStatus.OK).get_response()
        except (werkzeug.exceptions.BadRequest, ValueError) as e:
            return HttpResponse(HttpStatus.Bad_Request, message=str(e)).get_response()