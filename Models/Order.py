import datetime


class Order:
    counter = 0

    def __init__(self, id_supplier, id_client, expected_delivery_date, payment_type,
                 l_dips, appro_ship_sample, appro_s_off, ship_sample_2h, total_amount=0,
                 creation_date=None, products=None, id_order=None):
        self.__id_order = id_order
        self.__supplier = id_supplier
        self.__client = id_client
        self.__expected_delivery_date = expected_delivery_date
        self.__products = products
        self.__payment_type = payment_type
        self.__l_dips = l_dips
        self.__appro_ship_sample = appro_ship_sample
        self.__appro_s_off = appro_s_off
        self.__ship_sample_2h = ship_sample_2h
        self.__total_amount = total_amount
        if creation_date is None:
            self.__creation_date = datetime.datetime.today().strftime("%d-%m-%Y")
        else:
            self.__creation_date = creation_date

    def get_id_order(self):
        return self.__id_order

    def get_id_supplier(self):
        return self.__supplier

    def set_id_supplier(self, supplier):
        self.__supplier = supplier

    def get_id_client(self):
        return self.__client

    def set_id_client(self, client):
        self.__client = client

    def get_expected_delivery_date(self):
        return self.__expected_delivery_date

    def set_expected_delivery_date(self, expected_delivery_date):
        self.__expected_delivery_date = expected_delivery_date

    def get_products(self):
        return self.__products

    def set_products(self, products):
        self.__products = products

    def get_payment_type(self):
        return self.__payment_type

    def set_payment_type(self, payment_type):
        self.__payment_type = payment_type

    def get_creation_date(self):
        return self.__creation_date

    def set_creation_date(self, creation_date):
        self.__creation_date = creation_date

    def get_l_dips(self):
        return self.__l_dips

    def set_l_dips(self, l_dips):
        self.__l_dips = l_dips

    def get_appro_ship_sample(self):
        return self.__appro_ship_sample

    def set_appro_ship_sample(self, appro_ship_sample):
        self.__appro_ship_sample = appro_ship_sample

    def get_appro_s_off(self):
        return self.__appro_s_off

    def set_appro_s_off(self, appro_s_off):
        self.__appro_s_off = appro_s_off

    def get_ship_sample_2h(self):
        return self.__ship_sample_2h

    def set_ship_sample_2h(self, ship_sample_2h):
        self.__ship_sample_2h = ship_sample_2h

    def get_total_amount(self):
        return self.__total_amount

    def set_total_amount(self, total_amount):
        self.__total_amount = total_amount