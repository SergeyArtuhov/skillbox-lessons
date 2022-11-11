# Задача 2. Декорацию знаешь?
#
# На новой работе вы познакомились с middle-разработчиком на Python,
# который согласился научить вас всему, что умеет сам.
# Но перед этим он решил точечно проверить ваши знания.
# Он показал код, где один и тот же декоратор логирования использовался для каждого метода класса отдельно:
#
# Зная, что классы тоже можно декорировать, вы сразу поняли, как можно упростить код.
#
# Реализуйте декоратор logging, который должен декорировать класс и логировать каждый метод в нём.
# Логирование реализуйте на своё усмотрение:
# это может быть, например, вывод названия метода, его аргов, кваргов и документации на экран;
# либо вывод всей этой информации в отдельный файл вместе с датой и временем.
import functools
from typing import Callable


def logging(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(
            f'Название метода: {func.__name__}\n'
            f'Документация метода:\n'
            f'{func.__doc__}'
        )
        result = func(*args, **kwargs)
        return result
    return wrapper

def for_all_methods(decorator: Callable) -> Callable:
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                cur_method = getattr(cls, i_method_name)
                decorated = decorator(cur_method)
                setattr(cls, i_method_name, decorated)
        return cls
    return decorate


@for_all_methods(logging)
class MyClass:

    def method_1(self) -> None:
        """Документация метода 1"""
        print('Я метод 1')

    def method_2(self) -> None:
        """Документация метода 2"""
        print('Я метод 2')

    def method_3(self) -> None:
        """Документация метода 3"""
        print('Я метод 3')


instance = MyClass()
instance.method_1()
