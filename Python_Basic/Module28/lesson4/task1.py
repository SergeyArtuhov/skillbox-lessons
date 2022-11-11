# Задача 1. Работа с файлом
#
# Реализуйте класс File — контекстный менеджер для работы с файлами.
# Он должен принимать на вход имя файла и режим чтения/записи и открывать сам файл.
# В начале работы менеджер возвращает файловый объект, а в конце — закрывает файл.
#
# Пример основного кода:
#
# with File(‘example.txt’, ‘w’) as file:
#
#     file.write(‘Всем привет!’)


class File:
    def __init__(self, name: str, mode: str) -> None:
        self.name = name
        self.mode = mode

    def __enter__(self):
        self.file_object = open(self.name, self.mode)
        return self.file_object

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_object.close()


with File('example.txt', 'w') as file:
    file.write('Всем привет!')