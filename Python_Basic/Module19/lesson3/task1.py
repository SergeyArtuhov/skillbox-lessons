# Задача 1. Член семьи
#
# Дана структура, которая содержит описание одного из членов семьи (имя, фамилия, хобби, сколько лет и дети):
# family_member = {
#     "name": "Jane",
#     "surname": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "name": "Alice",
#             "age": 6
#         },
#         {
#             "name": "Bob",
#             "age": 8
#         }
#     ]
# }
#
# Напишите программу, которая реализует такую структуру: имя, фамилия, хобби, кол-во лет и дети.
# Затем, с помощью метода get и установки значения по умолчанию, проверьте есть ли ребёнок с именем Bob.
# Затем в отдельную переменную получите фамилию этого ребёнка и выведите её на экран. Если у него нет фамилии,
# то получите значение ‘Nosurname’.

family_member = dict()
family_member['name'] = 'Jane'
family_member['surname'] = 'Doe'
family_member['hobbies'] = ['running', 'sky diving', 'singing']
family_member['age'] = 35
family_member['children'] = [
    {
        'name': 'Alice',
        'age': 6
    },
    {
        'name': 'Bob',
        'age': 8
    }
]
surname = ''
for child in family_member.get('children', {}):
    if child.get('name') == 'Bob':
        print('Ребенок с именем Bob есть в списке')
        if family_member.get('surname', {}):
            surname = family_member.get('surname', {})
        else:
            surname = 'Nosurname'

print('Фамилия ребенка:', surname)



