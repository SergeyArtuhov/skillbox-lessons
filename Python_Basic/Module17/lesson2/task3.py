# Задача 3. Повышение цен
#
# Дан список цен на пять товаров с точностью до копейки.
# Так как экономика даёт о себе знать, мы спрогнозировали,
# что через год придётся повышать цены на X процентов,
# а ещё через один год — ещё на Y процентов.
#
# Напишите программу, которая получает на вход список цен на товары
# (вещественные числа, список генерируется также с помощью list comprehensions)
# и выводит в одну строку общую сумму стоимости товаров за каждый год.
#
# Пример:
# Цена на товар: 1.09
# Цена на товар: 23.56
# Цена на товар: 57.84
# Цена на товар: 4.56
# Цена на товар: 6.78
#
# Повышение на первый год: 0
# Повышение на второй год: 10
# Сумма цен за каждый год: 93.83 93.83 103.22

def new_prices(price, percent):
    return round(price * (1 + percent / 100), 2)


curr_prices = [float(input('Цена за товар: ')) for i_price in range(5)]
print()
first_percent = int(input('Повышение на первый год: '))
second_percent = int(input('Повышение на второй год: '))

first_rise = [new_prices(i_price, first_percent) for i_price in curr_prices]
second_rise = [new_prices(i_price, second_percent) for i_price in first_rise]

print(f'Сумма цен за каждый год: {round(sum(curr_prices), 2)}, {round(sum(first_rise), 2)}, {round(sum(second_rise), 2)}')