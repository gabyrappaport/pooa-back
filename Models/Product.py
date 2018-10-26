from Models.ExcelModel import ExcelModel


class Product(ExcelModel):
    counter = 0

    def __init__(self, id_order, reference, color, meter, price, commission, id_shipment=None, id_product=None):
        ExcelModel.__init__(self)
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

    def print_to_cell(self, worksheet, cell):
        worksheet[str(cell[0])] = self.__id_product
        #worksheet[str(cell[1])] = self.__id_order
        worksheet[str(cell[2])] = self.__reference
        worksheet[str(cell[3])] = self.__color
        worksheet[str(cell[4])] = self.__meter
        worksheet[str(cell[5])] = self.__price
        worksheet[str(cell[6])] = self.get_price_per_product()
        #worksheet[str(cell[7])] = self.__id_shipment

    def get_price_per_product(self):
        return self.__price * self.__meter