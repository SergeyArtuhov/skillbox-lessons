# Задача 1. Корабли
#
# Даны два класса кораблей — грузовой и военный. У каждого из этих кораблей есть своя модель,
# и каждый может сделать два действия: сообщить свою модель и идти по воде.
#
# Грузовой корабль имеет такой атрибут, как заполненность, изначально он равен нулю.
# У него есть ещё два действия: погрузить и выгрузить груз с корабля.
#
# У военного же корабля нет никаких грузов, есть только оружие, которое передаётся вместе с моделью.
# Также, вместо погрузки и выгрузки, у него есть другое действие — атаковать.
#
# Реализуйте классы грузового и военного кораблей. Для этого выделите общие атрибуты и методы в отдельный класс
# «Корабль» и используйте наследование. Не забудьте про функцию super в дочерних классах.

class Ship:
    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return 'Модель корабля - {model}'.format(
            model=self.__model
        )

    def sail(self):
        print('Корабль плывет')


class WarShip(Ship):
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def attack(self):
        print('Корабль атакует оружием - {}'.format(
            self.gun
        ))


class CargoShip(Ship):
    def __init__(self, model):
        super().__init__(model)
        self.tonnage_load = 0

    def load(self):
        print('Погрузили на корабль')
        self.tonnage_load += 1
        print('Загруженность корабля: {}'.format(self.tonnage_load))

    def unload(self):
        print('Разгрузили с корабля')
        self.tonnage_load -= 1
        print('Загруженность корабля: {}'.format(self.tonnage_load))


ship_1 = WarShip('911', 'Ракеты')
ship_2 = CargoShip('007')
print(ship_1)
ship_1.sail()
ship_1.attack()
print(ship_2)
ship_2.sail()
ship_2.load()
ship_2.unload()