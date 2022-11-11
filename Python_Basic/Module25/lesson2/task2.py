# Задача 2. Человек
#
# Реализуйте класс «Человек», который инициализируется именем (имя должно состоять только из букв)
# и возрастом (должен быть в диапазоне от 0 до 100),
# а внутри класса считается общее количество инициализированных объектов.
# Реализуйте сокрытие данных для всех атрибутов (как статических, так и динамических),
# а для изменения и получения данных объекта напишите специальные геттеры и сеттеры.
#
# При тестировании класса измените приватный атрибут (например, возраст) двумя способами:
# сеттером и «крайне не рекомендуемым», который был показан в уроке.

class Human:
    __count = 0

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        Human.__count += 1

    def set_name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            raise Exception('Имя содержит не только буквы')

    def set_age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            raise Exception('Возраст должен быть од 1 до 99')

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_count(self):
        return self.__count


max = Human('Max', 80)
print(max.get_name())
max.set_name('jhon')
print(max.get_name())
print(max.get_age())

print(max._Human__count)

print(max.get_count())
