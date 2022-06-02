# Задача 1. Словарь квадратов чисел
#
# На вход программе поступает целое число num.
# Напишите программу создания словаря, который включает в себя ключи от 1 до num,
# а значениями соответствующего ключа будет значение ключа в квадрате.
#
# Пример:
# Введите целое число: 5
# Результат: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

num = int(input('Введите целое число: '))
result = dict()
for i_num in range(1, num + 1):
    result[i_num] = i_num ** 2
print('Результат: {}'.format(result))