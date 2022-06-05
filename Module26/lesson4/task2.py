# Задача 2. Случайная сумма
#
# Алексею по работе необходимо обрабатывать огромные массивы данных из миллионов элементов.
# Каждый новый элемент — это сумма случайного вещественного числа от 0 до 1 и предыдущего элемента
# (первый элемент — просто случайное вещественное число от 0 до 1). Алексею нельзя хранить в памяти весь этот список,
# а со значениями работать как-то надо.
#
# Помогите Алексею, реализуйте такой класс-итератор и проверьте его работу.
# Также сделайте, чтобы при каждом новом вызове итератора в цикле значения считались заново.
#
# Пример работы программы:
#
# Кол-во элементов: 5
#
# Элементы итератора:
# 0.74
# 1.13
# 1.95
# 2.2
# 2.55
#
# Новое кол-во элементов: 6
#
# Элементы итератора:
# 0.79
# 1.58
# 2.55
# 2.81
# 3.06
# 3.34


import random


class MyIterator:
    def __init__(self, number):
        self.number = number
        self.counter = 0
        self.curr_number = 0

    def __iter__(self):
        self.counter = 0
        self.curr_number = 0
        return self

    def __next__(self):
        if self.counter < self.number:
            self.counter += 1
            self.curr_number += round(random.random(), 2)
            return round(self.curr_number, 2)
        else:
            raise StopIteration


my_iter = MyIterator(6)

for i in my_iter:
    print(i)

