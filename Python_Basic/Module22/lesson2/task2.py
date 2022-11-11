# Задача 2. Поиск файла
#
# В уроке мы написали функцию, которая ищет нужный нам файл во всех подкаталогах указанной директории.
# Однако, как мы понимаем, файлов с таким названием может быть несколько.
#
# Напишите функцию, которая принимает на вход абсолютный путь до директории и имя файла,
# проходит по всем вложенным файлам и папкам и выводит на экран все абсолютные пути с этим именем.
#
# Пример:
#
# Ищем в: C:/Users/Roman/PycharmProjects/Skillbox
# Имя файла: lesson2
#
# Найдены следующие пути:
# C:/Users/Roman/PycharmProjects/Skillbox\Module15\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module16\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module17\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module18\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module19\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module20\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module21\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module22\lesson2.py

import os


def file_finder(cur_path, file):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if file == i_elem:
            print(path)
        if os.path.isdir(path):
            file_finder(path, file)


folder_name = input('Ищем в: ')
file_name = input('Имя файла: ')

print('Найдены следующие пути: ')
file_finder(folder_name, file_name)
