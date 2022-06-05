# Задача 3. IP-адрес
#
# IP-адрес компьютера состоит из 4 чисел, разделённых точкой.
# Каждое число находится в диапазоне от 0 до 255 (включительно).
#
# Пример правильного адреса: 192.168.1.0
# Пример неправильного адреса: 192.168.300.0
#
# Напишите программу, которая получает на вход 4 числа и выводит на экран IP-адрес.
# Используйте переменную ip_address в качестве шаблона. Обеспечьте контроль ввода.

# nums = [input('Введите число: ') for _ in range(4)]
# for i in nums:
#     print(i, end='.')

nums = []
count = 0
while count < 4:
    num = int(input('Введите число: '))
    if num <= 255:
        nums.append(num)
        count += 1
    else:
        print('Неверное число!')

ip_address = '{0}'

for i in nums:
    print(ip_address.format(i), end='.')
