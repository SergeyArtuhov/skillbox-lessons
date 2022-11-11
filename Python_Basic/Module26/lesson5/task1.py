# Задача 1. Бесконечный генератор
#
# По аналогии с бесконечным итератором из практики предыдущего урока,
# реализуйте свой счётчик-генератор, который также в цикле будет бесконечно выдавать значения.
#
# Дополнительно: преобразуйте (или напишите с нуля) итератор простых чисел в функцию-генератор.

# def generator(number):
#     count = 0
#     for num in range(number):
#         if count != number:
#             yield count
#             count += 1


def prime(number):
    for num in range(2, number + 1):
            for i in range(2, (num // 2) + 1):
                if num % i == 0:
                    break
            else:
                yield num


# my_gen = generator(100)
# for num in my_gen:
#     print(num, end=' ')


my_prime = prime(50)
for i in my_prime:
    print(i, end=' ')