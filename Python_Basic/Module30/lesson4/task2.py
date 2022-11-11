# Задача 2. Сортировка
#
# Таблица базы данных состоит из строк, в которых хранится информация о каждом человеке:
# его имя, возраст и остальные данные.
# Вас попросили реализовать для этой базы сортировку по возрасту (по убыванию и по возрастанию).
#
# Реализуйте класс Person с соответствующей инициализацией, а также сеттерами и геттерами.
# Затем создайте список из хотя бы трёх людей и отсортируйте их. Для сортировки используйте лямбда-функцию.

class Person:
    def __init__(self, name: str, age: int, other: str) -> None:
        self.__name = name
        self.__age = age
        self.__other = other

    def __str__(self):
        return f'Имя: {self.name}, возраст: {self.age}, примечание: {self.other}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def other(self):
        return self.__other

    @other.setter
    def other(self, other):
        self.__other = other


person_1 = Person('Tom', 25, 'Nothing')
person_2 = Person('Kate', 44, 'Football')
person_3 = Person('Oleg', 32, 'Paint')

my_list = [person_1, person_2, person_3]

for i_person in sorted(my_list, key=lambda person: person.age):
    print(i_person)