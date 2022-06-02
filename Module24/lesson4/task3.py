# Задача 3. Весёлая ферма
#
# Для игры «Весёлая ферма» необходимо прописать два класса: класс «Картошка» и класс «Грядка картошки».
#
# У картошки есть её номер в грядке, а также стадия зрелости.
# Она может предоставлять информацию о своей зрелости и расти. Всего у картошки может быть четыре стадии зрелости.
#
# Грядка с картошкой содержит список картошки, которая на ней растёт, и может, собственно, взращивать всю эту картошку,
# а также предоставлять информацию о зрелости всей картошки на своей территории.
#
# Реализуйте оба класса и проверьте их работу: создайте экземпляр грядки из пяти картошек и три раза взрастите грядку.

class Potato:
    scale = {0: 'Ничего нет', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print(
            'Картощка {} сейчас {}'.format(self.index, Potato.scale[self.state])
        )


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка проростает')
        for i_potato in self.potatoes:
            i_potato.grow()

    def ripe_all(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка еще не созрела')
        else:
            print('Картошка созрела')


my_garden = PotatoGarden(5)
my_garden.ripe_all()
for _ in range(3):
    my_garden.grow_all()
    my_garden.ripe_all()