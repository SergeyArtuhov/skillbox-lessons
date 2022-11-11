# Задача 2. Замедление кода 2
#
# Продолжаем работать с нашим старым кодом. Ранее мы уже писали декоратор,
# который перед выполнением декорируемой функции ждёт несколько секунд.
#
# Модернизируйте этот декоратор так, чтобы количество секунд можно было передавать в качестве аргумента.
# По умолчанию декоратор ждёт одну секунду.
# Помимо этого сделайте так, чтобы декоратор можно было использовать как с аргументами, так и без них.

import time
import functools
from collections.abc import Callable
from typing import Optional


def sleep_with_sec(_func: Optional[Callable] = None, *, sec: int = 1):
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            print(f'Ждем {sec} секунд')
            time.sleep(sec)
            return func(*args, **kwargs)
        return wrapped
    if _func is None:
        return decorator
    else:
        return decorator(_func)


@sleep_with_sec(sec=5)
def some_func():
    print('Что-то происходит')


some_func()