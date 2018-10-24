class User:
    counter = 0

    def __init__(self, name, surname, email, password, user_type, id_user=None):
        if id_user is None:
            self.__id_user = User.counter
            User.counter += 1
        else:
            self.__id_user= id_user
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__password = password
        self.__user_type = user_type

    def get_id_user(self):
        return self.__id_user

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_surname(self):
        return self.__surname

    def set_surname(self, surname):
        self.__surname = surname

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_user_type(self):
        return self.__user_type

    def set_user_type(self, user_type):
        self.__user_type = user_type