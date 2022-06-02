class Pet:
    total_sound = 0

    def __init__(self):
        self.legs = 4


class Cat(Pet):

    @classmethod
    def sound(cls):
        cls.total_sound += 1
        print(cls.total_sound)
        print('Мяу!')


class Dog(Pet):
    @classmethod
    def sound(cls):
        cls.total_sound += 1
        print(cls.total_sound)
        print('Гав!')


cat = Cat
cat.sound()
cat.sound()
Cat.sound()
Dog.sound()
Dog.sound()
dog = Dog()
dog.sound()