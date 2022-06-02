# Задача 2. Содержимое
#
# Выберите любую директорию на своём диске и затем напишите программу,
# выводящую на экран абсолютные пути к файлам и папкам, которые находятся внутри этой директории.
#
# Результат программы на примере директории проекта python_basic:
#
# Содержимое каталога G:\PycharmProjects\python_basic
#     G:\PycharmProjects\python_basic\.git
#     G:\PycharmProjects\python_basic\.idea
#     G:\PycharmProjects\python_basic\Module14
#     G:\PycharmProjects\python_basic\Module15
#     G:\PycharmProjects\python_basic\Module16
#     G:\PycharmProjects\python_basic\Module17
#     G:\PycharmProjects\python_basic\Module18
#     G:\PycharmProjects\python_basic\Module19
#     G:\PycharmProjects\python_basic\Module20
#     G:\PycharmProjects\python_basic\Module21
#     G:\PycharmProjects\python_basic\Module22

import os

directory = 'SkillBox_lessons'
dir_path = os.path.abspath(os.path.join('..', '..', '..', directory))
for elem in os.listdir(dir_path):
    path = os.path.join(dir_path, elem)
    print('   ', path)

