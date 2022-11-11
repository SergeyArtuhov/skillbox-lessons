# Задача 1. Сумма чисел
#
# Во входном файле numbers.txt записано N целых чисел, каждое в отдельной строке.
# Напишите программу, которая выводит их сумму в выходной файл answer.txt.
#
# Пример:
# Содержимое файла numbers.txt:
# 1
# 2
# 3
# 4
# 10
#
# Содержимое файла answer.txt
# 20

numbers = open('numbers.txt', 'r')
summa = 0
for i_number in numbers:
    summa += int(i_number)
numbers.close()

answer = open('answer.txt', 'w')
answer.write(str(summa))
answer.close()

