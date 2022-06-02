# Задача 1. Повторение кода
#
# В одной из практик вы уже писали декоратор do_twice, который повторяет вызов декорируемой функции два раза.
# В этот раз реализуйте декоратор repeat, который повторяет задекорированную функцию уже n раз.
import functools
from collections.abc import Callable


def repeat(num: int):
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)
            return None
        return wrapped
    return decorator


@repeat(num=5)
def some_func():
    print('Функция выполнена')


some_func()