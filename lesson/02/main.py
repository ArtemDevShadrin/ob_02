class Test():
    def __init__(self):
        self.public = "Публичный атрибут\n"
        self._protected = "Защищенный атрибут\n"
        self.__private = "Приватный атрибут\n"

    def get_private(self):
        return self.__private

    def set_private(self, value):
        self.__private = value

test = Test()
print(test.public)

print(test._protected)

print(test.get_private())

test.set_private("Измененный приватный атрибут")

print(test.get_private())