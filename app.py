from flask import Blueprint
from flask_restful import Api

from Controllers.ShipmentController import ShipmentController
from Controllers.OrderController import OrderController
from Controllers.PartnerController import PartnerController
from Controllers.ExcelController import ExcelController

itn_bp = Blueprint('itn', __name__)
itn = Api(itn_bp)

# Route
itn.add_resource(ShipmentController, '/shipment')
itn.add_resource(OrderController, '/order')
itn.add_resource(PartnerController, '/partner')
itn.add_resource(ExcelController, '/excel')

