class User():
    def __init__(self, id, name, access_level = 1):
        self.id = id
        self.name = name
        self.access_level = access_level

    def user_info(self):
        return (f"Информация пользователя: \n"
                f"Идентификационный номер - {self.id} \n"
                f"Имя пользователя - {self.name} \n"
                f"Уровень доступа - {self.access_level}")

class Admin(User):
    user = []
    def __init__(self,  id, name, access_level, access_level_admin = "admin"):
        super().__init__( id, name, access_level)
        self.access_level_admin = access_level_admin
        self.__private_user = self.user

    def add_user(self, new_add_user):
        """
        :param new_add_user: имя нового пользователя
        :return: добавление нового пользователя в список
        """
        return self.__private_user.append(new_add_user)

    def list_user(self):
        """
        :return: вывод списка пользователя
        """
        return print(f"Список пользователей: {self.__private_user}")

    def remove_user(self, remove_user):
        """
        :param remove_user: имя пользователя которого хотим удалить
        :return: удаляет пользователя из списка
        """
        if remove_user in self.__private_user:
            return self.__private_user.remove(remove_user)
        else:
            return print(f"Такого пользователя - {remove_user} нет в списке")