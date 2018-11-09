from Models.ExcelModel import ExcelModel


class Partner(ExcelModel):

    def __init__(self, partner_type, company, id_partner=None):
        ExcelModel.__init__(self)

        if not isinstance(partner_type, str):
            raise TypeError("Partner type must be a string")
        if not isinstance(company, str):
            raise TypeError("Company must be a string")
        if company == "":
            raise ValueError("Enter a valid company name")

        self.__id_partner = id_partner
        self.__partner_type = partner_type
        self.__company = company

    def print_to_cell(self, worksheet, cell):
        # worksheet[str(cell[0])] = self.__id_partner
        # worksheet[str(cell[1])] = self.__partner_type
        worksheet[str(cell[2])] = self.__company

    def _get_id_partner(self):
        return self.__id_partner

    def _get_partner_type(self):
        return self.__partner_type

    def _get_company(self):
        return self.__company

    id_partner = property(_get_id_partner)
    partner_type = property(_get_partner_type)
    company = property(_get_company)
