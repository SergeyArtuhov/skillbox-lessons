# task 1

# main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
# first_company = [0, 0, 0]
# second_company = [1, 0, 0, 1, 1]
# third_company = [1, 1, 1, 0, 1]
# main.extend(first_company)
# main.extend(second_company)
# main.extend(third_company)
#
# print('Общий список задач:', main)
# print('Кол-во невыполненных задач:', main.count(0))

# task 2

# first_message = input('Первое сообщение: ')
# second_message = input('Второе сообщение: ')
# if list(first_message).count('!') > list(second_message).count('?'):
#     first_message += second_message
#     print(first_message)
# elif list(first_message).count('!') < list(second_message).count('?'):
#     second_message += first_message
#     print(second_message)
# else:
#     print('Ой!')

# task 3

# pack = []
# decode = []
# N = int(input('Кол-во пакетов: '))
# bad_pack = 0
# for i in range(N):
#     print('\nПакет номер', i + 1)
#     for bit in range (4):
#         print(f'{bit + 1} бит:', end=' ')
#         pack.append(int(input()))
#     if pack.count(-1) <= 1:
#         decode.extend(pack)
#     else:
#         print('Много ошибок в пакете.')
#         bad_pack += 1
#     pack = []
#
# print(f'\nПолученное сообщение: {decode}')
# print(f'Кол-во ошибок в сообщении: {decode.count(-1)}')
# print(f'Кол-во потерянных пакетов: {bad_pack}')
