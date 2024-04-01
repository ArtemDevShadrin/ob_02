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
        print(f"{self.name} - поет - ")

    def info(self):
        print(f"{self.name} - имя\n"
              f"{self.voice} - голос\n"
              f"{self.color} - цвет птицы\n")

class Pigeon(Bird):
    pass

bird1 = Pigeon("Гоша", "Курлык", "Серый")

bird1.sing()
