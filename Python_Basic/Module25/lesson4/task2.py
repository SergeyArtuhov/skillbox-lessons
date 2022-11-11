# Задача 2. Полёт
#
# Иногда для реализации дочерних классов используется так называемый класс-роль, где также описываются общие атрибуты
# и методы, но в программе инициализируются объекты только дочерних классов, а базовый класс-роль не трогается.
# К примеру, что общего у бабочки и ракеты? Они обе могут летать и приземляться.
#
# Реализуйте класс «Может летать».
# Атрибуты:
#
# Высота = 0.
# Скорость = 0.
# Методы:
#
# Взлететь (в теле прописать pass).
# Лететь (в теле прописать pass).
# Приземлиться (установить высоту и скорость в значение 0).
# Вывести высоту и скорость на экран.
#
# Затем реализуйте два дочерних класса:
#
# «Бабочка», который может:
# Взлететь (высота = 1).
# Лететь (скорость = 0.5).

# «Ракета», которая может:
# Взлететь (высота = 500, скорость = 1000).
# Приземлиться (высота = 0, взрыв).
# Взорваться (тут уже что угодно).


class CanFly:
    def __init__(self):
        self.height = 0
        self.speed = 0

    def take_off(self):
        pass

    def fly(self):
        pass

    def to_land(self):
        self.height = 0
        self.speed = 0

    def __str__(self):
        return 'Высота: {}\tСкорость: {}'.format(self.height, self.speed)


class Butterfly(CanFly):
    def take_off(self):
        self.height = 1

    def fly(self):
        self.speed = 0.5


class Rocket(CanFly):
    def take_off(self):
        self.height = 500
        self.speed = 1000

    def to_land(self):
        self.height = 0
        self.speed = 0
        self.explosion()

    def explosion(self):
        print('Бах!')


rocket = Rocket()
rocket.take_off()
print(rocket)
rocket.to_land()
print(rocket)