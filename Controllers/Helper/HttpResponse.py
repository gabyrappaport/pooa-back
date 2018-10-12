from enum import Enum


class HttpResponse:

    def __init__(self, http_status, message=None, data=None):
        self.http_status = http_status
        self.message = message
        self.data = data

    def get_response(self):
        response = {"status": self.http_status.value["status"],
                    "code": self.http_status.value["code"]}
        if self.message is not None:
            response["message"] = self.message
        if self.data is not None:
            response["data"] = self.data
        return response


class HttpStatus(Enum):
    OK = {"code": 200, "status": "OK"}
    Bad_Request = {"code": 400, "status": "Bad Request"}
    Unauthorized = {"code": 401, "status": "Unauthorized"}
    Not_Found = {"code": 404, "status": "Not Found"}
