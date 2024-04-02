class Car:
    def __init__(self, make, model):
        self.public_make = make  # Открытый атрибут
        self._protected_model = model  # Защищенный атрибут
        self.__private_year = 2022  # Приватный атрибут

    def public_method(self):
        return f"Это открытый метод. Машина: {self.public_make} {self._protected_model}."

    def _protected_method(self):
        return "Это защищенный метод."

    def __private_method(self):
        return "Это приватный метод."


class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size

    def get_deails(self):
        # Можно обратиться к открытому и защищенному атрибуту, но не к приватному
        details = f"{self.public_make} {self._protected_model}, Батарея: {self.battery_size} kWh."
        # Нельзя напрямую обратиться к __private_method и __private_year
        return details


# Создаем экземпляр ElectricCar
tesla = ElectricCar("Tesla", "Model S", 100)

# Доступ к открытому атрибуту и методу:
print(tesla.public_make)
print(tesla.public_method())

# Доступ к защищенному атрибуту (не рекомендуется, но можно):
print(tesla._protected_model)
print(tesla._protected_method())

# Доступ к приватному отрибуту и методу напрямую не возможен. Но Python позволяет обойти это ограничение (не рекомендуется):
print(tesla._Car__private_year)  # Доступ к приватному атрибуту через name mangling
