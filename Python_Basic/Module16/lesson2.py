# task 1

# zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
# zoo.insert(1, 'bear')
# zoo.remove('elephant')
# i_lion = zoo.index('lion')
# i_monkey = zoo.index('monkey')
# print('Зоопарк:', zoo)
# print(f'Лев сидит в клетке номер {i_lion + 1}')
# print(f'Обезьяна сидит в клетке номер {i_monkey + 1}')

# task 2

# N = int(input('Кол-во сотрудников: '))
# salary_list = []
# workers_count = 0
# for num in range(N):
#     print(f'Зарплата {num + 1} сотрудника: ', end='')
#     salary = int(input())
#     if salary != 0:
#         salary_list.append(salary)
#         workers_count += 1
# print()
# print(f'Осталось сотрудников: {workers_count}')
# print(f'Зарплаты: {salary_list}')
# print(f'Максимальная зп: {max(salary_list)}')
# print(f'Минимальная зп: {min(salary_list)}')

# task 3

def film_exist(movie, films):
    for i_movie in films:
        if i_movie == movie:
            return True
    return False

films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]
my_films = []

while True:
    print('Ваш текущий топ фильмов:', my_films)
    new_movie = input('Название фильма: ')
    if film_exist(new_movie, films):
        print('Команды: добавить, вставить, удалить')
        command = input('Введите команду: ')
        if command.lower() == 'добавить':
            if not film_exist(new_movie, my_films):
                my_films.append(new_movie)
            else:
                print('Этот фильм уже есть в вашем списке')
        elif command.lower() == 'вставить':
            if not film_exist(new_movie, my_films):
                index = int(input('На какое место поставить фильм?'))
                my_films.insert(index - 1, new_movie)
        elif command.lower() == 'удалить':
            if film_exist(new_movie, my_films):
                my_films.remove(new_movie)
    else:
        print('Такого фильма нет в нашем списке')
    print()



