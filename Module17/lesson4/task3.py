# Задача 3. Удаление части
#
# Дан список из N чисел, а также числа А и В
# (можно сгенерировать случайно, при этом А < B).
# Напишите программу, которая удаляет элементы списка с индексами от А до В.
# Не используйте дополнительные переменные и методы списков.

N = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
A = 2
B = 5
N[A:B + 1] = ''
print(N)