class Test():
    def public_func(self):
        print("Публичный метод\n")

    def _protected_func(self):
        print("Защищенный метод")

    def __private_func(self):
        print("Приватный метод\n")

    def test_private_func(self):
        self.__private_func()


test = Test()

test.public_func()

test._protected_func()

test.test_private_func()