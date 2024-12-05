class Rat():
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def squeak(self):
        print("пик-пик!")

    def describe(self):
        print(f"Меня зовут {self.name}, я {self.color} цвета")



my_rat = Rat("Луи", "серого")
my_rat.squeak()
my_rat.describe()

