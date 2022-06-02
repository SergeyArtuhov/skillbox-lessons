# Задача 2. Таймер 2
#
# Для замера времени передачи различных данных на множество сайтов вы написали специальную функцию,
# которая сделала всю работу за вас, что позволило большую часть времени смотреть видео с котиками в интернете.
# Однако, увидев свой код, вы как программист с опытом поняли, что этот код можно написать намного красивее и удобнее.
#
# Реализуйте декоратор, который замеряет время работы задекорированной функции и выводит ответ на экран.
# Для проверки примените декоратор к какой-нибудь «тяжеловесной» функции и вызовите её в основной программе.

import time
from typing import Callable, Any


def timer(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        run_time = round(end - start, 4)
        print(
            'Функция работала {} секунд(ы)'.format(
                run_time
            )
        )
        return result
    return wrapped_func


@timer
def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 3 for i_num in range(100000)])
    return result


my_cubes = cubes_sum(10)
print(my_cubes)