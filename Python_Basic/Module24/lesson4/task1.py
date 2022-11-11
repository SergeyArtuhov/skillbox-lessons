# Задача 1. Машина 3
#
# Вам предстоит снова немного видоизменить класс Toyota из прошлого урока. На всякий случай вот описание класса.
#
# Четыре атрибута:
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Два метода:
# Отображение информации об объекте класса.
# Метод, который позволяет устанавливать текущую скорость машины.
# Теперь все четыре атрибута должны инициализироваться при создании экземпляра класса (то есть передаваться в init).
# Реализуйте такое изменение класса.

class Toyota:

    def __init__(self, color, price, max_speed, current_speed):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.current_speed = current_speed

    def info(self):
        print(
            'Color: {} \nPrice: {} \nMax speed: {} \nCurrent_speed: {}'.format(
                self.color, self.price, self.max_speed, self.current_speed
            )
        )

    def change_speed(self, new_speed):
        self.current_speed = new_speed
        print('Current speed has been changed to {}'.format(self.current_speed))


corolla = Toyota('red', 10000, 180, 20)
corolla.info()
corolla.change_speed(80)
corolla.info()