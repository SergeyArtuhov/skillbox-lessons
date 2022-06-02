# Задача 1. Результаты
#
# Одному программисту дали задачу для обработки неких результатов тестирования двух групп людей.
# Файл первой группы (group_1.txt) находится в папке task, файл второй группы (group_2.txt) — в папке Additional_info.
#
# Содержимое файла group_1.txt
# Бобровский Игорь 10
# Дронов Александр 20
# Жуков Виктор 30
#
# Содержимое файла group_2.txt
# Павленко Геннадий 20
# Щербаков Владимир 35
# Marley Bob 15
#
# На экран нужно было вывести сумму очков первой группы,
# затем разность очков опять же первой группы и напоследок — произведение очков уже второй группы.
#
# Программист оказался не очень опытным, писал код наобум и даже не стал его проверять.
# И оказалось, этот код просто не работает. Вот что он написал:
#
# Исправьте код для решения поставленной задачи.
# Для проверки результата создайте необходимые папки (task, Additional_info, Dont touch me)
# на своём диске в соответствии с картинкой и также добавьте файлы group_1.txt и group_2.txt.

file = open('/Users/artuhovse/PycharmProjects/SkillBox_lessons/Module22/lesson3/task/group_1.txt',
            'r', encoding='utf-8')
summa = 0
for i_line in file:
    info = i_line.split()
    summa += int(info[2])

file = open('/Users/artuhovse/PycharmProjects/SkillBox_lessons/Module22/lesson3/task/group_1.txt',
            'r', encoding='utf-8')
diff = 0
for i_line in file:
    info = i_line.split()
    diff -= int(info[2])

file_2 = open('/Users/artuhovse/PycharmProjects/SkillBox_lessons/Module22/lesson3/task/Additional_info/group_2.txt',
              'r', encoding='utf-8')
compose = 1
for i_line in file_2:
    info = i_line.split()
    compose *= int(info[2])

print(summa)
print(diff)
print(compose)
