# Задача 2. Всё в одном
#
# Ваш друг, который тоже проходит курс Python Basic, поехал с ноутбуком в другой город, и там у него случилась беда:
# его диск пришлось отформатировать, а доступ в интернет отсутствует. Остался только телефон с мобильным интернетом.
# Так как со связью (и с памятью) проблемы, друг попросил вас скинуть одним файлом все решения и скрипты,
# которые у вас сейчас есть.
#
# Напишите программу, которая копирует код каждого скрипта в папке проекта python_basic в файл scripts.txt,
# разделяя код строкой из 40 символов *.
#
# Пример содержимого файла scripts.txt:

import os


def finder(curr_path):
    for i_elem in os.listdir(curr_path):
        path = os.path.join(curr_path, i_elem)
        if os.path.isfile(path) and not path.endswith('.DS_Store'):
            print(f'Переходим к файлу {path}')
            file = open(path, 'r', encoding='utf-8')
            data = file.read()
            scripts.write(f'\nСодержимое файла {path}:\n')
            scripts.write(f'{data}\n')
            scripts.write('*' * 40)
            file.close()
        elif os.path.isdir(path):
            print(f'Это папка: {path}')
            print(f'Переходим в неё')
            finder(path)


scripts = open('scripts.txt', 'w')
folder = '/Users/artuhovse/PycharmProjects/SkillBox_lessons'
finder(folder)
scripts.close()
