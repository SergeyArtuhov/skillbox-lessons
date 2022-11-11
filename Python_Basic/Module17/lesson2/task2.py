# Задача 2. Сообщение
#
# Илья решил безобидно подшутить над другом и написал программу для смартфона,
# которая при отправке сообщения удваивает каждый символ строки
# и заодно к каждому удвоенному добавляет ещё один дополнительный.
#
# Пользователь вводит строку и дополнительный символ.
# Напишите программу, которая генерирует два списка:
# в первом списке каждый элемент — удвоенная буква первой строки,
# во втором списке каждый элемент — конкатенация элемента первого списка
# и дополнительного символа.
#
# Пример:
# Введите строку: привет
# Введите дополнительный символ: !
#
# Список удвоенных символов: ['пп', 'рр', 'ии', 'вв', 'ее', 'тт']
# Склейка с дополнительным символом: ['пп!', 'рр!', 'ии!', 'вв!', 'ее!', 'тт!']

text = input('Введите строку: ')
sym = input('Введите дополнительный символ: ')

double = [i_sym * 2 for i_sym in text]
sym_add = [j_sym + sym for j_sym in double]

print()
print('Список удвоенных символов:', double)
print('Склейка с дополнительным символом:', sym_add)