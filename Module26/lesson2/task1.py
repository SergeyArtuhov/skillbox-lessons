# Задача 1. Свой for (ну почти)
#
# Дан любой итерируемый объект, например список из N чисел.
# Реализуйте функцию, которая эмулирует работу цикла for с помощью цикла while
# и проходит во всем элементам итерируемого объекта. Не забудьте про исключение «конца итерации».


my_list = [10, 20, 30]

iterator = my_list.__iter__()

while True:
    try:
        print(iterator.__next__())
    except StopIteration:
        print('Итерируемый объект пуст')
        break