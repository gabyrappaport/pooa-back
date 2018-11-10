import datetime

from Models.ExcelModel import ExcelModel


class Order(ExcelModel):

    def __init__(self, id_supplier, id_client, expected_delivery_date, payment_type,
                 l_dips, appro_ship_sample, appro_s_off, ship_sample_2h, total_amount=0, creation_date=None,
                 id_order=None, products=None, complete_delivery_date=None, complete_payment_date=None):
        ExcelModel.__init__(self)

        if not isinstance(payment_type, str):
            raise TypeError("Payment type must be a string")
        if not isinstance(expected_delivery_date, datetime.datetime):
            raise TypeError("Delivery date must be a valid datetime object")
        if not isinstance(l_dips, str):
            raise TypeError("Lype must be a string")
        if not isinstance(payment_type, str):
            raise TypeError("Payment type must be a string")
        if not isinstance(payment_type, str):
            raise TypeError("Payment type must be a string")
        if not isinstance(payment_type, str):
            raise TypeError("Payment type must be a string")
        if not isinstance(payment_type, str):
            raise TypeError("Payment type must be a string")


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
        self.__complete_delivery_date = complete_delivery_date
        self.__complete_payment_date = complete_payment_date
        if creation_date is None:
            self.__creation_date = datetime.datetime.today().strftime("%Y-%m-%d")
        else:
            self.__creation_date = creation_date

    def get_number_of_products(self):
        return len(self.__products)

    def get_total_amout_per_order(self):
        if self.__products:
            sum = 0
            for p in self.__products:
                price = p.get_price_per_product()
                sum += price
            return sum
        else:
            return "There is no product in this order"

    def print_to_cell(self, worksheet, cell):
        worksheet[str(cell[1])] = self.get_total_amout_per_order()
        worksheet[str(cell[2])] = self.get_total_amout_per_order()
        worksheet[str(cell[3])] = self.__expected_delivery_date
        worksheet[str(cell[4])] = self.__payment_type
        worksheet[str(cell[5])] = self.__l_dips
        worksheet[str(cell[6])] = self.__appro_ship_sample
        worksheet[str(cell[7])] = self.__appro_s_off
        worksheet[str(cell[8])] = self.__ship_sample_2h
        worksheet[str(cell[10])] = self.__creation_date
        if self.__products:
            i = 0
            for p in self.__products:
                iter_products = int(11 + i)
                p.print_to_cell(worksheet, cell[iter_products])
                i += 1

    def _get_id_order(self):
        return self.__id_order

    def _set_id_order(self, id_order):
        self.__id_order = id_order

    def _get_id_supplier(self):
        return self.__supplier

    def _get_id_client(self):
        return self.__client

    def _get_expected_delivery_date(self):
        return self.__expected_delivery_date

    def _get_products(self):
        return self.__products

    def _set_products(self, products):
        self.__products = products

    def _get_payment_type(self):
        return self.__payment_type

    def _get_creation_date(self):
        return self.__creation_date

    def _get_l_dips(self):
        return self.__l_dips

    def _get_appro_ship_sample(self):
        return self.__appro_ship_sample

    def _get_appro_s_off(self):
        return self.__appro_s_off

    def _get_ship_sample_2h(self):
        return self.__ship_sample_2h

    def _get_total_amount(self):
        return self.__total_amount

    def _set_total_amount(self, total_amount):
        self.__total_amount = total_amount

    def _get_complete_delivery_date(self):
        return self.__complete_delivery_date

    def _set_complete_delivery_date(self, complete_delivery_date):
        self.__complete_delivery_date = complete_delivery_date

    def _get_complete_payment_date(self):
        return self.__complete_payment_date

    def _set_complete_payment_date(self, complete_payment_date):
        self.__complete_payment_date = complete_payment_date

    id_order = property(_get_id_order, _set_id_order)
    id_supplier = property(_get_id_supplier)
    id_client = property(_get_id_client)
    expected_delivery_date = property(_get_expected_delivery_date)
    products = property(_get_products, _set_products)
    payment_type = property(_get_payment_type)
    creation_date = property(_get_creation_date)
    l_dips = property(_get_l_dips)
    appro_ship_sample = property(_get_appro_ship_sample)
    appro_s_off = property(_get_appro_s_off)
    ship_sample_2h = property(_get_ship_sample_2h)
    total_amount = property(_get_total_amount, _set_total_amount)
    complete_delivery_date = property(_get_complete_delivery_date, _set_complete_delivery_date)
    complete_payment_date = property(_get_complete_payment_date, _set_complete_payment_date)