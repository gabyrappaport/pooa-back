from enum import Enum
from flask import Response


class HttpResponse:

    def __init__(self, http_status, message=None, data=None):
        self.http_status = http_status
        self.message = message
        self.data = data

    def get_response(self):
        response = {}
        if self.message is not None:
            response["message"] = self.message
        if self.data is not None:
            response["data"] = self.data
        return Response(str(response).replace("\'", "\"").replace("None", "-1"),
                        status=self.http_status.value["code"],
                        mimetype="application/json")

class HttpStatus(Enum):
    OK = {"code": 200, "status": "OK"}
    Bad_Request = {"code": 400, "status": "Bad Request"}
    Unauthorized = {"code": 401, "status": "Unauthorized"}
    Not_Found = {"code": 404, "status": "Not Found"}
