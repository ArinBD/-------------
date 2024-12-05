class Rat():
    def __init__(self, name, color, age=0):
        self.name = name
        self.color = color
        self.age = age

    def squeak(self):
        print("пик-пик!")

    def describe(self):
        print(f"Меня зовут {self.name}, я {self.color} цвета, мне {self.color} лет.")


class Humster(Rat):
    def __init__(self, name, color, age, job):
        super().__init__(name,color,age)
        self.job = job
    def do_job(self):
        print(f"{self.name} выполняет свою работу: {self.job}.")

my_rat = Rat("Луи", "серого")
my_rat.describe()


work_humster = Humster("Джеральд", "коричнегого", 3 , "Криптоинвестор")
work_humster.describe()
work_humster.do_job()
work_humster.squeak()