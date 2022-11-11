# Задача 2. Семья
# Реализуйте класс «Семья», который состоит из атрибутов «Имя», Деньги» и «Наличие дома»
# и объекты которого могут выполнять следующие действия:
#
# Отобразить информацию о себе.
# Заработать денег (подаётся число, которое прибавляется к текущему значению денег).
# Купить дом (подаётся стоимость дома и необязательный аргумент «Скидка»).
# Вывести соответствующее сообщение об успешной/неуспешной покупке дома.
# Создайте как минимум один экземпляр класса и проверьте работу методов.
#
# Пример работы программы (вывод информации, покупка дома, заработок, очередная покупка):
#
# Family name: Common family
# Family funds: 100000
# Having a house: False
#
# Try to buy a house
# Not enough money!
#
# Earned 800000 money! Current value: 900000
# Try to buy a house again
# House purchased! Current money: 0.0
#
# Family name: Common family
# Family funds: 0.0
# Having a house: True

class Family:
    name = 'Common family'
    money = 100000
    have_a_house = False

    def info(self):
        print(
            'Family name: {}\nFamily funds: {}\nHaving a house: {}\n'.format(
                self.name, self.money, self.have_a_house
            )
        )

    def earn_money(self, amount):
        self.money += amount
        print(
            'Earned {} money!. Current values: {}\n'.format(
                amount, self.money
            )
        )

    def buy_house(self, price, discount=0):
        print('Try to buy a house')
        price -= price * discount / 100
        if self.money >= price:
            self.money -= price
            self.have_a_house = True
            print(
                'House purchased! Current money: {}\n'.format(
                    self.money
                )
            )
        else:
            print('Not enough money\n')


my_family = Family()
my_family.info()
my_family.buy_house(10 ** 6)
my_family.earn_money(800000)
my_family.buy_house(10 ** 6, 10)
my_family.info()