# Задача 1. Юниты
#
# Есть базовый класс «Юнит», который определяется количеством здоровья (хитпоинты).
# У Юнита есть действие «получить урон» (базовый класс получает 0 урона).
#
# Также есть два дочерних класса:
#
# Солдат: получает урон, равный переданному значению.
# Обычный гражданин: получает урон, равный двукратному переданному значению.
# Реализуйте родительский и дочерние классы и их методы, используя принцип полиморфизма (а также инкапсуляции и
# наследования, конечно же).

class Unit:
    def __init__(self, health=100):
        self.health = health

    def take_damage(self, damage=0):
        self.health -= damage
        print('Юнит получил урон {}. Осталось здоровья: {}'.format(damage, self.health))


class Soldier(Unit):
    def take_damage(self, damage=0):
        self.health -= damage
        print('Юнит получил урон {}. Осталось здоровья: {}'.format(damage, self.health))


class Civilian(Unit):
    def take_damage(self, damage=0):
        self.health -= damage * 2
        print('Юнит получил урон {}. Осталось здоровья: {}'.format(damage * 2, self.health))


unit = Unit()
soldier = Soldier()
civilian = Civilian()
soldier.take_damage(5)
civilian.take_damage(5)