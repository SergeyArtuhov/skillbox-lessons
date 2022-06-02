# Задача 2. Поиск файла 2
#
# Как мы помним, скрипты — это просто куча строк текста, хоть они и понятны только программисту.
# Таким образом, с ними можно работать точно так же, как и с обычными текстовыми файлами.
#
# Используя функцию поиска файла из предыдущего урока, реализуйте программу,
# которая находит внутри указанного пути все файлы с искомым названием
# и выводит на экран текст одного из них (выбор можно сгенерировать случайно).
#
# Подсказка: можно использовать, например, список для сохранения найденного пути.

import os
import random


def file_finder(cur_path, file, my_list):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if file == i_elem:
            my_list.append(path)
        if os.path.isdir(path):
            file_finder(path, file, my_list)


files = list()
folder_name = input('Ищем в: ')
file_name = input('Имя файла: ')

file_finder(folder_name, file_name, files)
number_of_file = random.randint(0, len(files) - 1)
file = open(files[number_of_file], 'r', encoding='utf-8')
data = file.read()
print(data)
file.close()
