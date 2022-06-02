# Задача 1. Кризис миновал
#
# Закупки грейпфрутов прекратились, и кризис в торговой компании закончился.
# И теперь можно вернуться к обыденным делам.
# Однако внезапно вы обнаружили, что старый скрипт,
# который выводит данные о фруктах, куда-то потерялся. Необходимо его восстановить.
#
# Дан словарь с парами «название фрукта — цена»:
#
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
#
# Вывести на экран словарь в следующем виде:
# apple -- 5600.2
# orange -- 3500.45
# banana -- 5000.0
# bergamot -- 3700.56
# durian -- 5987.23
# peach -- 10000.5
# pear -- 1020.0
# persimmon -- 310.0
#
# Не используйте обращение по ключу словаря.

incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

for item, price in incomes.items():
    print('{fruit} -- {cost}'.format(
        fruit=item,
        cost=price
    ))