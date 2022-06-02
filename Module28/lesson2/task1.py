# Задача 1. Снова роботы
#
# На военную базу привезли очередную партию роботов. И в этот раз не абы каких,
# а летающих: разведывательного дрона и военного робота.
#
# Разведывательный дрон просто летает в поиске противника.
# При команде operate он выводит сообщение «Веду разведку с воздуха» и передвигается немного вперёд.
#
# У летающего военного робота есть оружие, и при команде operate он выводит сообщение
# о защите военного объекта с воздуха с помощью этого оружия.
#
# Напишите программу, которая реализует все необходимые классы роботов. Сущности «Робот» и «Может летать»
# должны быть вынесены в отдельные классы. Обычный робот имеет модель и может вывести сообщение «Я — Робот».
# Объект, который умеет летать, дополнительно имеет атрибуты «Высота» и «Скорость»,
# а также может взлетать, летать и приземляться.


class Robot:
    def __init__(self, model):
        self.model = model

    def message(self):
        print('Я - работ')


class CanFly:
    def __init__(self, height, speed):
        self.height = height
        self.speed = speed

    def takeoff(self):
        print('Взлет')

    def fly(self):
        print('Летит')

    def to_land(self):
        print('Приземлился')


class Scout(CanFly, Robot):
    def __init__(self, height, speed, model):
        super().__init__(height, speed)
        self.model = model


    def operate(self):
        print('Веду разведку с воздуха')


t_800 = Scout(10, 1, 2)
t_800.message()
