class Order:
    counter = 0

    def __init__(self, id_supplier, id_client, expected_delivery_date, payment_type, id_order=None, products=None):
        if id_order is None:
            self.__id_order = Order.counter
            Order.counter += 1
        else:
            self.__id_order = id_order
        self.__supplier = id_supplier
        self.__client = id_client
        self.__expected_delivery_date = expected_delivery_date
        self.__products = products
        self.__payment_type = payment_type

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

