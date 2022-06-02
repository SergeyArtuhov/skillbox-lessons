# Задача 1. Машина
#
# Напишите класс Toyota, состоящий из четырёх статических атрибутов:
#
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Создайте три экземпляра класса и каждому из них поменяйте значение текущей скорости на случайное число от нуля до 200.

import random


class Toyota:
    color = 'blue'
    max_speed = 200
    current_speed = 0


corolla = Toyota()
camry = Toyota()
prius = Toyota()

corolla.current_speed = random.randint(0, 200)
camry.current_speed = random.randint(0, 200)
prius.current_speed = random.randint(0, 200)

print(f'Текущая скорость Toyota Corolla: {corolla.current_speed}')
print(f'Текущая скорость Toyota Camry: {camry.current_speed}')
print(f'Текущая скорость Toyota Prius: {prius.current_speed}')
