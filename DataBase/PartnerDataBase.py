from Controllers.Helper.WritingDataBaseError import *
from DataBase.Helper.DatabaseConnector import Database


class PartnerDataBase:

    def __init__(self):
        pass

    def get_partner(self, id_partner):
        """Get the partner with its id"""
        query_partner = Database.query("SELECT * FROM Partners WHERE id_partner = ?", (id_partner,))
        partner = query_partner.fetchone()
        if partner is not None:
            return self.__list_to_dic_partner(partner)
        else:
            return partner

    def get_clients(self):
        """Get all clients"""
        query_clients = Database.query("SELECT * FROM Partners WHERE partner_type = 'client' ")
        result = []
        for row in query_clients:
            partner = self.__list_to_dic_partner(row)
            result.append(partner)
        return result

    def get_suppliers(self):
        """Get all suppliers"""
        query_suppliers = Database.query("SELECT * FROM Partners WHERE partner_type = 'supplier' ")
        result = []
        for row in query_suppliers:
            partner = self.__list_to_dic_partner(row)
            result.append(partner)
        return result

    def get_nbr_undelivered_order_by_partner(self):
        """Get all partners with number of undelivered orders."""

        query_undelivered = Database.query(
            "SELECT Partners.id_partner, company, COUNT(Orders.complete_delivery_date) as 'undelivered' "
            "FROM Partners , Orders "
            "WHERE Partners.id_partner = Orders.id_supplier "
            "AND Orders.complete_delivery_date = 'NULL' "
            "GROUP BY Partners.id_partner, company "
            "UNION "
            "SELECT Partners.id_partner, company, COUNT(Orders.complete_delivery_date) as 'undelivered' "
            "FROM Partners , Orders "
            "WHERE Partners.id_partner = Orders.id_client "
            "AND Orders.complete_delivery_date = 'NULL' "
            "GROUP BY Partners.id_partner, company ")

        result = []
        for row in query_undelivered:
            partner = self.__list_to_dic_partner_undelivered(row)
            result.append(partner)
        return result

    def get_nbr_unpaid_order_by_partner(self):
        """Get all partners with number of unpaid orders."""

        query_undelivered = Database.query(
            "SELECT id_partner, company, COUNT(complete_delivery_date) as 'unpaid' "
            "FROM Partners , Orders "
            "WHERE Partners.id_partner = Orders.id_supplier "
            "AND Orders.complete_payment_date = 'NULL' "
            "GROUP BY Partners.id_partner, company "
            "UNION "
            "SELECT id_partner, company, COUNT(complete_delivery_date) as 'unpaid' "
            "FROM Partners , Orders "
            "WHERE Partners.id_partner = Orders.id_client "
            "AND Orders.complete_payment_date = 'NULL' "
            "GROUP BY Partners.id_partner, company ")

        result = []
        for row in query_undelivered:
            partner = self.__list_to_dic_partner_unpaid(row)
            result.append(partner)
        return result

    def get_clients_stats(self):
        """Get all clients with statistics on their orders."""
        query_clients = Database.query("SELECT * FROM Partners WHERE partner_type = 'client' ")
        result = []
        for row in query_clients:
            partner = self.__list_to_dic_partner(row)
            result.append(partner)
        return result

    def get_all_partners(self):
        query_partners = Database.query("SELECT * FROM Partners ")
        result = []
        for row in query_partners:
            partner = self.__list_to_dic_partner(row)
            result.append(partner)
        return result

    def add_partner(self, partner):
        """Create a new partner with its company name and partner type : client or supplier"""
        try:
            values = (partner.get_partner_type(),
                      partner.get_company())
            Database.query("INSERT INTO Partners (partner_type, company) VALUES(?,?)", values)
        except(ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def delete_partner(self, id_partner):
        """Delete a partner with the name of the company"""
        Database.query("DELETE FROM Partners WHERE id_partner = ?", (id_partner,))

    def update_partner(self, partner):
        """Change the value for the object partner"""
        try:
            values = (partner.get_partner_type(),
                      partner.get_company(),
                      partner.get_id_partner())
            Database.query("UPDATE Partners SET partner_type = ?, company = ? WHERE id_partner = ? ", values)
        except(ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def __list_to_dic_partner(self, partner):
        return {"id_partner": partner[0],
                "partner_type": partner[1],
                "company": partner[2]}

    def __list_to_dic_partner_unpaid(self, partner):
        return {"id_partner": partner[0],
                "company": partner[1],
                "unpaid": partner[2]}

    def __list_to_dic_partner_undelivered(self, partner):
        return {"id_partner": partner[0],
                "company": partner[1],
                "undelivered": partner[2]}
