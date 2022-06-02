# Задача 1. Пунктуация
#
# Напишите программу, которая считает количество знаков пунктуации в символьной строке.
# К знакам пунктуации относятся символы из набора ".,;:!?". Набор должен храниться в виде множества.
#
# Пример:
# Введите строку: Я! Есть. Грут?! Я, Грут и Есть.
# Количество знаков пунктуации: 6

punctuation = set('.,;:!?')
text = input('Введите строку: ')
count = 0
for symbol in text:
    if symbol in punctuation:
        count += 1
print(count)


