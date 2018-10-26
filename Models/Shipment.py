class Shipment:
    counter = 0

    def __init__(self, expedition_date, transportation,
                 departure_location, arrival_location, products=None, id_shipment=None):
        self.__id_shipment = id_shipment
        self.__expedition_date = expedition_date
        self.__transportation = transportation
        self.__departure_location = departure_location
        self.__arrival_location = arrival_location
        self.__products = products

    def get_id_shipment(self):
        return self.__id_shipment

    def get_expedition_date(self):
        return self.__expedition_date

    def set_expedition_date(self, expedition_date):
        self.__expedition_date = expedition_date

    def get_transportation(self):
        return self.__transportation

    def set_transportation(self, transportation):
        self.__transportation = transportation

    def get_departure_location(self):
        return self.__departure_location

    def set_departure_location(self, departure_location):
        self.__departure_location = departure_location

    def get_arrival_location(self):
        return self.__arrival_location

    def set_arrival_location(self, arrival_location):
        self.__arrival_location = arrival_location

    def get_products(self):
        return self.__products

    def set_products(self, products):
        self.__products = products
