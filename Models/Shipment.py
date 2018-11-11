from datetime import datetime


class Shipment:

    def __init__(self, expedition_date, transportation,
                 departure_location, arrival_location, products=None, id_shipment=None):

        if not isinstance(expedition_date, datetime):
            raise TypeError("Expedition date must be a valid datetime object")
        if not isinstance(transportation, str):
            raise TypeError("Transportation must be a string")
        if not isinstance(departure_location, str):
            raise TypeError("Departure location must be a string")
        if not isinstance(arrival_location, str):
            raise TypeError("Arrival location must be a string")
        if expedition_date == "":
            raise ValueError("Enter a valid expedition_date")
        if transportation == "":
            raise ValueError("Enter a valid transportation mode")
        if departure_location == "":
            raise ValueError("Enter a valid departure_location")
        if arrival_location == "":
            raise ValueError("Enter a valid arrival_location")

        self.__id_shipment = id_shipment
        self.__expedition_date = expedition_date
        self.__transportation = transportation
        self.__departure_location = departure_location
        self.__arrival_location = arrival_location
        self.__products = products

    def _get_id_shipment(self):
        return self.__id_shipment

    def _set_id_shipment(self, id_shipment):
        self.__id_shipment = id_shipment

    def _get_expedition_date(self):
        return self.__expedition_date

    def _get_transportation(self):
        return self.__transportation

    def _get_departure_location(self):
        return self.__departure_location

    def _get_arrival_location(self):
        return self.__arrival_location

    id_shipment = property(_get_id_shipment, _set_id_shipment)
    expedition_date = property(_get_expedition_date)
    transportation = property(_get_transportation)
    departure_location = property(_get_departure_location)
    arrival_location = property(_get_arrival_location)
