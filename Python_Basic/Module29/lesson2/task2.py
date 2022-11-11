# Задача 2. Директории
#
# Реализуйте функцию in_dir, которая принимает в качестве аргумента путь и временно меняет текущую рабочую директорию
# на новую. Функция должна быть контекст-менеджером. Также реализуйте обработку ошибок
# (например, если такого пути не существует).
# Вне зависимости от результата выполнения контекст-менеджера нужно возвращаться в изначальную рабочую директорию.
#
# Пример основного кода:
#
# with in_dir('C:\\'):
#     print(os.listdir())
#
# Результат:
# <тут все папки из вашего диска C>


import os
from contextlib import contextmanager
from collections.abc import Iterator


@contextmanager
def in_dir(path: str) -> Iterator:
    try:
        yield os.chdir(path)
    except FileNotFoundError:
        print('Такой путь не найден')
        yield


with in_dir('/usr'):
    print(os.listdir())