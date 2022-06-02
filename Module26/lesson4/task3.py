# Задача 3. Простые числа
#
# Реализуйте класс-итератор Primes, который принимает максимальное число N и выдаёт все простые числа от 1 до N.
#
# Основной код:
#
# prime_nums = Primes(50)
# for i_elem in prime_nums:
#     print(i_elem, end=' ')
#
# Ожидаемый результат кода:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47

class Primes:
    def __init__(self, max_num):
        self.number = 1
        self.max_num = max_num

    def __iter__(self):
        return self

    def __next__(self):
        if self.number < self.max_num:
            self.number += 1
            for i in range(2, (self.number // 2) + 1):
                if self.number % i == 0:
                    return self.__next__()
            return self.number
        else:
            raise StopIteration


prime_nums = Primes(50)

for i_elem in prime_nums:
    print(i_elem, end=' ')