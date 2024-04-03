Система управления пользователями и администраторами
Данный Python-скрипт реализует простую систему управления пользователями и администраторами. Он определяет два класса: 
User (Пользователь) и Admin (Администратор).

Класс User
Класс User представляет собой базового пользователя в системе. У него есть следующие атрибуты:

id: Идентификационный номер пользователя.
name: Имя пользователя.
access_level: Уровень доступа пользователя, по умолчанию равен 1.
Кроме того, он предоставляет метод user_info(), который позволяет получить информацию о пользователе.

Класс Admin
Класс Admin является подклассом класса User и представляет собой администратора в системе. Помимо атрибутов, 
унаследованных от класса User, у него есть дополнительный атрибут:

access_level_admin: Уровень доступа для администраторов, по умолчанию равен "admin".
Класс Admin предоставляет следующие методы:

add_user(new_add_user): Добавляет нового пользователя в систему.
list_user(): Выводит список всех пользователей в системе.
remove_user(remove_user): Удаляет пользователя из системы.


Пример использования

# Создаем экземпляр администратора
admin1 = Admin(1, "Ник", 5)

# Добавляем пользователей
admin1.add_user("Пэм")
admin1.add_user("Роб")
admin1.add_user("Боб")

# Выводим список пользователей
admin1.list_user()

# Удаляем пользователя
admin1.remove_user("Боб")

# Пытаемся удалить несуществующего пользователя
admin1.remove_user("Поб")

# Выводим список пользователей после удаления
admin1.list_user()

# Создаем обычного пользователя
user1 = User(2, "Поп")

# Выводим информацию о пользователе
print(user1.user_info())
Этот код создает экземпляр администратора, добавляет пользователей, выводит список пользователей, удаляет пользователя 
и выводит информацию о пользователе.

Зависимости
Для работы этой программы требуется Python 3.x. Дополнительные зависимости не требуются.

Лицензия
Этот проект лицензируется на основе лицензии MIT - см. файл LICENSE для получения дополнительной информации.




