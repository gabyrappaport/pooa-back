from Models.ExcelModel import ExcelModel


class Partner(ExcelModel):
    counter = 0

    def __init__(self, partner_type, company, id_partner=None):
        ExcelModel.__init__(self)
        self.__id_partner = id_partner
        self.__partner_type = partner_type
        self.__company = company

    def get_id_partner(self):
        return self.__id_partner
        
    def get_partner_type(self):
        return self.__partner_type

    def set_partner_type(self, partner_type):
        self.__partner_type = partner_type

    def get_company(self):
        return self.__company

    def set_company(self, company):
        self.__company = company

    def print_to_cell(self, worksheet, cell):
        # worksheet[str(cell[0])] = self.__id_partner
        # worksheet[str(cell[1])] = self.__partner_type
        worksheet[str(cell[2])] = self.__company
