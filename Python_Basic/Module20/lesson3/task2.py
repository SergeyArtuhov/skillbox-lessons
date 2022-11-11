# Задача 2. Словари из списков
#
# Создайте два списка, в каждом из которых лежит 10 случайных букв алфавита (могут повторяться).
# Затем для каждого списка создайте словарь из пар «индекс — значение» и выведите оба словаря на экран.
#
# Подсказка: random
#
# Пример:
#
# Первый список: ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']
# Второй список: ['д', 'а', 'а', 'в', 'т', 'ж', 'р', 'б', 'й', 'р']
#
# Первый словарь: {0: 'й', 1: 'р', 2: 'с', 3: 'г', 4: 'а', 5: 'а', 6: 'т', 7: 'ж', 8: 'е', 9: 'к'}
# Второй словарь: {0: 'д', 1: 'а', 2: 'а', 3: 'в', 4: 'т', 5: 'ж', 6: 'р', 7: 'б', 8: 'й', 9: 'р'}

import random
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
first_list = [alphabet[random.randint(1, len(alphabet))] for symbol_1 in range(10)]
second_list = [alphabet[random.randint(1, len(alphabet))] for symbol_2 in range(10)]
my_dict_1 = {index_1: symbol_1 for index_1, symbol_1 in enumerate(first_list)}
my_dict_2 = {index_2: symbol_2 for index_2, symbol_2 in enumerate(second_list)}

print(f'Первый список: {first_list}')
print(f'Второй список: {second_list}')

print(f'\nПервый словарь: {my_dict_1}')
print(f'Второй словарь: {my_dict_2}')

