# task 1

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in matrix:
#     for k in i:
#         print(k, end=' ')
#     print()

# task 2

# N = int(input('Кол-во участников: '))
# K = int(input('Кол-во человек в команде: '))
# team_list = []
# z = 1
# if N % K == 0:
#     for _ in range(N // K):
#         team_list.append(list(range(z, z + K)))
#         z += K
#     print('Общий список команд:', team_list)
# else:
#     print(f'{N} участников невозможно поделить на команды по {K} человек')

# task 3

goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
new_goods = []
print('Текущий ассортимент:', goods)

fruit_name = input('\nНовый фрукт: ')
price = int(input('Цена: '))

new_goods.extend(goods)
new_goods.append([fruit_name, price])
print('Новый ассортимент:', new_goods)

for i in new_goods:
    i[1] = round(i[1] * 1.08, 2)
print('Новый ассортимент с увел. ценой:', new_goods)