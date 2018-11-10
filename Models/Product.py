from Models.ExcelModel import ExcelModel


class Product(ExcelModel):

    def __init__(self, id_order, reference, color, meter, price, commission, id_shipment=None, id_product=None):
        ExcelModel.__init__(self)

        if not isinstance(reference, str):
            raise TypeError("Reference must be a string")
        if not isinstance(color, str):
            raise TypeError("Color must be a string")
        if not isinstance(meter, float):
            raise TypeError("Meter must be a number")
        if not isinstance(price, float):
            raise TypeError("Price must be a number")
        if not isinstance(commission, float):
            raise TypeError("Commission must be a number")

        self.__id_product = id_product
        self.__id_order = id_order
        self.__id_shipment = id_shipment
        self.__reference = reference
        self.__color = color
        self.__meter = meter
        self.__price = price
        self.__commission = commission

    def print_to_cell(self, worksheet, cell):
        worksheet[str(cell[0])] = self.__id_product
        worksheet[str(cell[2])] = self.__reference
        worksheet[str(cell[3])] = self.__color
        worksheet[str(cell[4])] = self.__meter
        worksheet[str(cell[5])] = self.__price
        worksheet[str(cell[6])] = self.get_price_per_product()

    def get_price_per_product(self):
        return self.__price * self.__meter

    def get_price_with_commission(self):
        return (self.__commission / 100 * self.__price * self.__meter).__round__(2)

    def _get_id_product(self):
        return self.__id_product
    
    def _set_id_product(self, id_product):
        self.__id_product = id_product

    def _get_id_order(self):
        return self.__id_order

    def _get_id_shipment(self):
        return self.__id_shipment

    def _get_reference(self):
        return self.__reference

    def _get_color(self):
        return self.__color

    def _get_meter(self):
        return self.__meter

    def _get_price(self):
        return self.__price

    def _get_commission(self):
        return self.__commission

    id_product = property(_get_id_product, _set_id_product)
    id_order = property(_get_id_order)
    id_shipment = property(_get_id_shipment)
    reference = property(_get_reference)
    color = property(_get_color)
    meter = property(_get_meter)
    price = property(_get_price)
    commission = property(_get_commission)
