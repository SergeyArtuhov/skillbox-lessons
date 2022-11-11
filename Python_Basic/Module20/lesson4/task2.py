# Задача 2. Сервер
#
# У вас есть данные о сервере, которые хранятся в виде вот такого словаря:
#
# server_data = {
#     "server": {
#         "host": "127.0.0.1",
#         "port": "10"
#     },
#     "configuration": {
#         "access": "true",
#         "login": "Ivan",
#         "password": "qwerty"
#     }
# }
#
# Напишите программу, которая выводит для пользователя эти данные так же красиво и понятно,
# как они представлены в словаре.
#
# Результат работы программы:
# server:
#     host: 127.0.0.1
#     port: 10
# configuration:
#     access: true
#     login: Ivan
#     password: qwerty

server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for i_key, i_value in server_data.items():
    print(f'{i_key}:')
    for j_key, j_value in i_value.items():
        print(f'\t{j_key}: {j_value}')