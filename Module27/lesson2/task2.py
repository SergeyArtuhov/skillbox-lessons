# Задача 2. Таймер
#
# Вы работаете в отделе тестирования, и вам поручили с помощью различных функций замерить скорость передачи данных
# на нескольких десятках сайтов. Конечно же, вручную «щёлкать» сайты и замерять время вам было лень,
# поэтому возникла идея написать «автотест», который всё сделает сам.
#
# С помощью понятия функции высшего порядка реализуйте функцию-таймер,
# которая замеряет время работы переданной функции func и выдаёт ответ на экран.
#
# Проверьте работу таймера на какой-нибудь «тяжеловесной» функции.

import time
from typing import Any, Callable


def timer(func: Callable, *args, **kwargs) -> Any:
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


def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 3 for i_num in range(100000)])
    return result


my_cubes = timer(cubes_sum, 10)
x = my_cubes()
print(x)

