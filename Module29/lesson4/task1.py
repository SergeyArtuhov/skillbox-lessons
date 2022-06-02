# Задача 1. Createtime
#
# Реализуйте декоратор класса, который выдаёт дату и время создания,
# а также список всех методов объекта класса каждый раз, когда объект класса создаётся в основном коде.
import datetime
import functools
import time


def create_time(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print('Время создания класса:', datetime.datetime.utcnow())
        print('Список всех методов класса:', dir(cls))
        return instance
    return wrapper


@create_time
class Function:
    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    def squares_sum(self) -> int:
        number = 100
        result = 0
        for _ in range(number):
            result += sum([i_num ** 2 for i_num in range(1, self.max_num + 1)])
        return result

    def cubes_sum(self, number: int) -> int:
        result = 0
        for _ in range(number):
            result += sum([i_num ** 3 for i_num in range(1, self.max_num + 1)])
        return result


instance = Function(100)
