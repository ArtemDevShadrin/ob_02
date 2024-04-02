class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f"{self.name} - летает")

    def eat(self):
        print(f"{self.name} - кушает")

    def sing(self):
        print(f"{self.name} - поет - Чирик")

    def info(self):
        print(f"{self.name} - имя\n"
              f"{self.voice} - голос\n"
              f"{self.color} - цвет птицы\n")

class Pigeon(Bird):
    def __init__(self, name, voice, color, favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food

    def walk(self):
        print(f"{self.name} - гуляет")

    def sing(self):
        print(f"{self.name} - поет - Курлык курлык")

bird1 = Pigeon("Гоша", "Курлык", "Серый", "Хлебные крошки")
bird2 = Bird("Маша", "Чирик", "Коричневый")

bird1.sing()
bird2.sing()

bird1.info()
bird2.info()

bird1.walk()

