class Partner:
    counter = 0

    def __init__(self, partner_type, company, id_partner=None):
        if id_partner is None:
            self.__id_partner = Partner.counter
            Partner.counter += 1
        else:
            self.__id_partner = id_partner
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
