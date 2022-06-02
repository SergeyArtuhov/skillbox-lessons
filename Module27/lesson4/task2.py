# Задача 2. Плагины
#
# Один проект состоит из огромного количества разнообразных функций, часть из которых используется в других проектах
# в качестве плагинов, то есть они как бы «подключаются» и создают дополнительный функционал.
#
# Реализуйте специальный декоратор, который будет «регистрировать» нужные функции как плагины
# и заносить их в соответствующий словарь.


from typing import Callable, Dict


PLUGIN: Dict[str, Callable] = dict()


def registrator(func: Callable) -> Callable:
    PLUGIN[func.__name__] = func
    return func


@registrator
def say_hello(name):
    return 'Hello {name}!'.format(name=name)


@registrator
def say_goodbye(name):
    return 'Hello {name}!'.format(name=name)


print(PLUGIN)
print(say_goodbye.__name__)
print(PLUGIN)