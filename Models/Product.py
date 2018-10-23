class Product:
    counter = 0

    def __init__(self, id_order, reference, color, meter, price, commission, id_shipment=None, id_product=None):
        if id_product is None:
            self.__id_product = Product.counter
            Product.counter += 1
            print(Product.counter)
        else:
            self.__id_product = id_product
        self.__id_order = id_order
        self.__id_shipment = id_shipment
        self.__reference = reference
        self.__color = color
        self.__meter = meter
        self.__price = price
        self.__commission = commission

    def get_id_product(self):
        return self.__id_product

    def get_id_order(self):
        return self.__id_order

    def set_id_order(self, id_order):
        self.__id_order = id_order

    def get_id_shipment(self):
        return self.__id_shipment

    def set_id_shipment(self, id_shipment):
        self.__id_shipment = id_shipment

    def get_reference(self):
        return self.__reference

    def set_reference(self, reference):
        self.__reference = reference

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_meter(self):
        return self.__meter

    def set_meter(self, meter):
        self.__meter = meter

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_commission(self):
        return self.__commission

    def set_commission(self, commission):
        self.__commission = commission