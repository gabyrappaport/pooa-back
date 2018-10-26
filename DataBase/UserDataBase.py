from DataBase.Helper.DatabaseConnector import Database
from Controllers.Helper.WritingDataBaseError import *
import hashlib

class UserDataBase:

    def __init__(self):
        pass

    def get_user(self, id_user):
        """Get the user with its id"""
        query_user = Database.query("SELECT * FROM Users WHERE id_user = ?", (id_user,))
        user = query_user.fetchone()
        if user is not None:
            return self.__list_to_dic_user(user)
        else:
            return user

    def get_all_users(self):
        query_users = Database.query("SELECT * FROM Users ")
        result = []
        for row in query_users:
            user = self.__list_to_dic_user(row)
            result.append(user)
        return result

    def add_user(self, user):
        """Create a new user with its info"""
        try:
            values = (int(user.get_id_user()),
                      user.get_name(),
                      user.get_surname(),
                      user.get_email(),
                      user.get_password(),
                      user.get_user_type())
            Database.query("INSERT INTO Users VALUES(?,?,?,?,?,?)", values)
        except(ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def check_user(self, email, password):
        """Returns True if the email and password are right, False if not"""
        try:
            values = (email,
                      password)
            query_user = Database.query("SELECT * FROM Users WHERE email = ? AND password = ?", values)
            result_connection_user = query_user.fetchall()
            if len(result_connection_user) > 0:
                return True
            else:
                return False
        except(ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def delete_user(self, id_user):
        """Delete a user with the id"""
        Database.query("DELETE FROM Users WHERE id_user = ?", (id_user,))

    def update_user(self, user):
        """Change the value for the object user"""
        try:
            values = (user.get_name(),
                      user.get_surname(),
                      user.get_email(),
                      user.get_password(),
                      user.get_user_type(),
                      user.get_id_user())
            Database.query("UPDATE Users SET name = ?, surname = ?, email = ?, password = ?, user_type = ? "
                           "WHERE id_user = ? ", values)
        except(ValueError, TypeError):
            raise WritingDataBaseError("Wrong type Value.")

    def __list_to_dic_user(self, user):
        return {"id_user": user[0],
                "name": user[1],
                "surname": user[2],
                "email": user[3],
                "password": user[4],
                "user_type": user[5]}
