# class Point:
#
#     f = 0
#
#     def __new__(cls, *args, **kwargs):
#         print('method new')
#         return super().__new__(cls)
#
#     def __init__(self, y, x=0):
#         self.x = x
#         self.y = y
#
#
# p = Point(2, 8)
# print(p.x)

# class DataBase:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#
#     def __init__(self, user, password, port):
#         self.user = user
#         self.password = password
#         self.port = port
#
#     def __del__(self):
#         print('wefs')
#         DataBase.__instance = None
#
#     def connect(self):
#             print(f'соединение с БД: {self.user}, {self.password}, {self.port}')
#
#     def close(self):
#         print('соединение прервано')
#
#     def read(self):
#         print('чтение данных')
#
#     def write(self, data):
#         print(f'Записываем данные {data}')
#
# db = DataBase('user1', 'psw1', '8000')
# db2 = DataBase('user2', 'psw2', '7000')
# print(db)
# print(db2)

# class Test:
#
#     def __bool__(self):
#         return True
#
# t = Test()
# if t:
#     print('jhrbigres')

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError('введите целое')
#         self.seconds = seconds % self.__DAY
#
#     def get_time(self):
#         s = self.seconds % 60
#         m = self.seconds // 60 % 60
#         h = self.seconds // 3600 % 24
#         return f'{h}:{m}:{s}'
#
#     def __eq__(self, other):
#         if not isinstance(other, int):
#             raise TypeError('введите целое')
#         if isinstance(other, int):
#             other = other
#         else:
#             other = other.seconds
#         p = 5**8
#         sc = other if isinstance(other, int) else other.seconds
#         return Clock(self.seconds == sc)
#
#     def __lt__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise TypeError('TypeError')
#         sc = other if isinstance(other, int) else other.seconds
#         return Clock(self.seconds <= sc)
#
#     def __add_(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError('не сложить')
#
#         sc = other if isinstance(other, int) else other.seconds
#         return Clock(self.seconds + sc)
#
#
# cl = Clock(86400)
# cl2 = Clock(54)
# print(cl.get_time())
# cl = cl + cl2
# print(cl.get_time())

#1
# class Passport:
#
#     def __init__(self, first_name, last_name, country, date_of_birth, num_of_passport):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.country = country
#         self.date_of_birth = date_of_birth
#         self.num_of_passport = num_of_passport
#
#     def printInfo(self):
#         print(f'''
# Full name: {self.first_name} {self.last_name}
# Date of Birth: {self.date_of_birth}
# Country: {self.country}
# Passport: {self.num_of_passport}''')
#
#     def __repr__(self):
#         return f'Name: {self.first_name} {self.last_name}, {self.num_of_passport}'
#
# class ForeignPassport(Passport):
#
#     def __init__(self, first_name, last_name, country, date_of_birth, num_of_passport, visa):
#         super().__init__(first_name, last_name, country, date_of_birth, num_of_passport)
#         self.visa = visa
#
#     def printInfo(self):
#         super().printInfo()
#         print('Visa: ', self.visa)
#
# MFC = []
# p = Passport('Ivan', 'Ivanov', 'Russia', '14.05.2005', '8221 453083')
# MFC.append(p)
# fp = ForeignPassport('Petr', 'Petrov', 'Russia', '25.03.1999', '4372 987643', 'China')
# MFC.append(fp)
# for item in MFC:
#     item.printInfo()


#2
# class Equipment:
#
#     def __init__(self, name, make, year):
#         self.name = name
#         self.make = make
#         self.year = year
#
#     def action(self):
#         return 'Не определено'
#
#     def __str__(self):
#         return f'{self.name}, {self.make}, {self.year}, умеет {self.action()}'
#
#     def __le__(self, other):
#         if not isinstance(other, Equipment):
#             raise TypeError
#         return self.year <= other.year
#
#
#
#
#
#
#
# class Printer(Equipment):
#
#     def __init__(self, series, name, make, year):
#         super().__init__(name, make, year)
#         self.series = series
#
#     def action(self):
#         return 'печатает'
#
#     def __str__(self):
#         return f'{self.series} {self.name} {self.make} {self.year}'
#
# class Scaner(Equipment):
#
#     def __init__(self, name, make, year):
#         super().__init__(name, make, year)
#
#     def action(self):
#         return 'сканирует'
#
# class Xerox(Equipment):
#
#     def __init__(self, name, make, year):
#         super().__init__(name, make, year)
#
#     def action(self):
#         return 'копирует и печатает'
#
#
# sklad = []
# e = Equipment('Noname', 'X', 2000)
# sklad.append(e)
# p = Printer('refe', 'wefwef', 'rgesrg', 2015)
# sklad.append(p)
# x = Xerox('ewfwef', 'qewfwe', 2031)
# sklad.append(x)
# e = Equipment('Nona', 'Xx', 2060)
# sklad.append(e)
# p = Printer('ree', 'weef', 'esrg', 215)
# sklad.append(p)
# x = Xerox('ewef', 'qewe', 201)
# sklad.append(x)
# for item in sklad:
#     if isinstance(item, Printer):
#         print(item)

#3
# import random
# class Soldier:
#
#     def __init__(self, name='Noname', health=100):
#         self.name = name
#         self.health = health
#
#     def set_name(self, name):
#         self.name = name
#
#     def make_kick(self, enemy):
#         enemy.health -= 20
#         if enemy.health < 0:
#             enemy.health = 0
#             self.health += 10
#             print(self.name, "бьет", enemy.name)
#             print('%s = %d' % (enemy.name, enemy.health))
#
# class Battle:
#     def __init__(self,u1,u2):
#         self.u1 = u1
#         self.u2 = u2
#         self.result = "Сражения не было"
#     def battle(self):
#         while self.u1.health > 0 and self.u2.health > 0:
#             n = random.randint(1, 2)
#             if n == 1:
#
#                 self.u1.make_kick(self.u2)
#             else:
#
#                 self.u2.make_kick(self.u1)
#         if self.u1.health > self.u2.health:
#
#             self.result = self.u1.name + " ПОБЕДИЛ"
#         elif self.u2.health > self.u1.health:
#
#             self.result = self.u2.name + " ПОБЕДИЛ"
#     def who_win(self):
#         print(self.result)
#
# first = Soldier('Mr. First',140)
# second = Soldier()
# second.set_name('Mr. Second')
# b = Battle(first, second)
# b.battle()
# b.who_win()

#4
# import random
# class Card:
#     NumsList = ["Джокер",'2','3','4','5','6','7','8','9','10',
#                             "Валет","Дама","Король","Туз"]
#     MastList = ["пик","крестей","бубей","червей"]
#
#     def __init__(self, i, j):
#         self.Mastb = self.MastList[i-1]
#         self.Num = self.NumsList[j-1]
#
# class DeckOfCards:
#     def __init__(self):
#         self.deck = [None] * 56
#         k = 0
#         for i in range(1, 4 + 1):
#             for j in range(1, 14 + 1):
#                 self.deck[k] = Card(i, j)
#                 k += 1
#
#     def shuffle(self):
#         random.shuffle(self.deck)
#     def get(self, i):
#         if 0 <= i <= 55:
#             answer = self.deck[i].Num
#             answer += " "
#             answer += self.deck[i].Mastb
#         else:
#             answer = "В колоде только 56 карт"
#         return answer
#
# deck = DeckOfCards()
# deck.shuffle()
# print('Выберите карту из колоды в 56 карт:')
# n = int(input())
# if n<=56:
#     card = deck.get(n-1)
#     print('Вы взяли карту: ', card, end='.\n')
# else:
#     print("В колоде только 56 карт")

# Автобус
# class Bus:
#
#     def __init__(self, speed, capacity, maxSpeed, passengers, hasEmptySeats, seats):
#         self.speed = speed
#         self.capacity = capacity
#         self.maxSpeed = maxSpeed
#         self.passengers = passengers
#         self.hasEmptySeats = hasEmptySeats
#         self.seats = seats
#
#     def posadka(self):
#         return f'посажено {len(self.passengers) + 1}'
#
#     def vysadka(self):
#         return f'высажено {len(self.passengers) - 1}'
#
#
#     def higherspeed(self):
#         return f'после ускорения {self.speed + 5}'
#
#
# b = Bus(45, 10, 50, ['Grisha','Arina','Andrey'], 7, 10)
# print(b.higherspeed())
# print(b.posadka())
# print(b.vysadka())






