# Задача 2. Фигуры
#
# При моделировании компьютерных объектов используются два типа фигур: прямоугольники и квадраты.
# Каждая из них имеет координаты XY, длину и ширину. Также каждая фигура может менять координаты (двигаться)
# и менять размер.
#
# Реализуйте такие классы. Учтите, что с точки зрения интерфейса прямоугольник и квадрат — это разные фигуры
# и работают они по-разному. В частности, по-разному работает метод изменения размера фигуры,
# так как у квадрата все стороны равны.


from abc import ABC, abstractmethod


class Figure(ABC):
    """
    Абстрактный базовый класс Фигура
    Args:
        pos_x: координата икс
        pos_y: координата игрек
        length: длина
        width: ширина
    """
    def __init__(self, pos_x: int, pos_y: int, length: int, width: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length
        self.width = width

    @abstractmethod
    def move(self, pos_x: int, pos_y: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y


class ResizableMixin:
    def resize(self, length: int, width: int) -> None:
        self.length = length
        self.width = width
        print(self.length, self.width)


class Rectangle(Figure, ResizableMixin):
    """Прямоугольник. Родительский класс: Figure"""
    def move(self, pos_x: int, pos_y: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y


class Square(Figure, ResizableMixin):
    """Квадрат. Родительский класс: Figure"""
    def move(self, pos_x: int, pos_y: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y

    def __init__(self, pos_x: int, pos_y: int, size: int) -> None:
        super().__init__(pos_x, pos_y, size, size)


rect_1 = Rectangle(pos_x=1, pos_y=1, length=10, width=5)
rect_2 = Rectangle(pos_x=2, pos_y=2, length=5, width=6)
square = Square(pos_x=3, pos_y=3, size=5)

for figure in [rect_1, rect_2, square]:
    new_x = figure.length * 2
    new_y = figure.width * 2
    figure.resize(new_x, new_y)