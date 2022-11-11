# Задача 1. Машина 2
#
# Модернизируйте класс Toyota из прошлого урока. Атрибуты остаются такими же:
#
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
#
# Добавьте два метода класса:
# Отображение информации об объекте класса.
# Метод, который позволяет устанавливать текущую скорость машины.
# Проверьте работу этих методов.

class Toyota:
    color = 'red'
    price = 10 ** 6
    max_speed = 200
    current_speed = 0

    def info(self):
        print(
            'Color: {}\nPrice: {}\nMax speed: {}\nCurrent speed: {}'.format(
                self.color, self.price, self.max_speed, self.current_speed
            )
        )

    def change_speed(self, new_speed):
        self.current_speed = new_speed
        print('Current speed has been changed to {}'.format(self.current_speed))


car_1 = Toyota()
car_1.info()
car_1.change_speed(50)
car_1.info()