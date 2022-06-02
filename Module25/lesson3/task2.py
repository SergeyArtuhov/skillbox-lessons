# Задача 2. Роботы
#
# На военную базу завезли несколько интересных моделей роботов, которые похожи между собой,
# но имеют немного разные функции. У каждого робота есть номер модели и действие operate,
# которое означает, что делает робот. Особенности роботов следующие:
#
# У робота-пылесоса есть мешок для мусора, изначально он пустой (0). При команде operate робот сообщает,
# что он пылесосит пол, и выводит текущую заполняемость мешка.
# У военного робота есть оружие, и при команде operate он выводит сообщение о защите военного объекта
# с помощью этого оружия.
# Ещё есть робот — подводная лодка, который также является военным. У этого робота есть значение глубины,
# и при команде operate он делает то же, что и военный робот, плюс сообщает, что охрана ведётся под водой.
#
# Напишите программу, которая реализует все необходимые классы роботов.


class Robot:
    def __init__(self, model):
        self.__model = model

    def operate(self):
        pass


class VacuumCleaner(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.garbage_bag = 0

    def operate(self):
        print('Робот пылесосит. Текущая заполняемость мешка - {}'.format(self.garbage_bag))
        self.garbage_bag += 1


class Defender(Robot):
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def operate(self):
        print('Военный объект защищен с помощью оружия - {}'.format(self.gun))


class Submarine(Defender):
    def __init__(self, model, gun, depth):
        super().__init__(model, gun)
        self.depth = depth

    def operate(self):
        print('Охрана ведется под водой на глубине {}'.format(self.depth))
        print('Военный объект защищен с помощью оружия - {}'.format(self.gun))


robot_1 = VacuumCleaner('911')
robot_2 = Defender('111', 'Пушки')
robot_3 = Submarine('431', 'Торпеды', -1)


robot_1.operate()
robot_1.operate()

robot_2.operate()

robot_3.operate()



