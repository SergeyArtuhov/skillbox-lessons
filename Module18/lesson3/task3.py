# Задача 3. Разделители символов
#
# Человек хочет сделать рассылку поздравлений для определённого списка людей.
# Поздравления для разных людей он хочет написать по-разному.
#
# Напишите программу, которая запрашивает у пользователя:
#
# Шаблон поздравления (туда вставляется ФИ и возраст)
# ФИ людей (в одну строку, разделяются запятой)
# Возраст каждого человека (в одну строку через пробел)
# В конце  программа выводит поздравления и всех именинников в одну строку вместе с их возрастом.
#
# Пример:
# Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: С днём рождения, {name}! С {age}-летием тебя!
# Список людей через запятую: Иван Иванов, Петя Петров, Лена Ленова
# Возраст людей через пробел: 20 30 18
#
# С днём рождения, Иван Иванов! С 20-летием тебя!
# С днём рождения, Петя Петров! С 30-летием тебя!
# С днём рождения, Лена Ленова! С 18-летием тебя!
#
# Именинники: Иван Иванов 20, Петя Петров 30, Лена Ленова 18

gratters = input('Введите шаблон поздравления, в шаблоне можно использовать конструкцию'
                 '{name} и {age}: ')
names_list = input('Список людей через запятую: ').split(', ')
ages_str = input('Возраст людей через пробел: ')
ages_list = [int(i_num) for i_num in ages_str.split()]

for i_man in range(len(names_list)):
    print(gratters.format(name=names_list[i_man], age=ages_list[i_man]))

people = [
    ' '.join([names_list[i_man], str(ages_list[i_man])])
    for i_man in range(len(names_list))
]
people_str = ', '.join(people)
print('Именниники:', people_str)