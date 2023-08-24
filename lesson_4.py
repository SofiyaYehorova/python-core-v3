#

#                                                   TRY EXCEPT
# try:
#     s = int(input('Enter num'))
#     print(4/0)
# except KeyboardInterrupt as err:
#     print('stopped by user')
# except Exception as err:
#     print(err)
# else:
#     print('all right')
# finally:
#     print('finish')
#
# print('end')


#                                                ГЕНЕРАТОРИ

# l = [i * 25 for i in range(50000000)]
# input()

# g = (i * 25 for i in range(50000000))
# input()
# print(type(g)) #<class 'generator'> генератори менше їдять оперативної памяті

# ГЕНЕРАТОРИ ПРАЦЮЮТЬ З ЛІВА НА ПРАВО, ПІСЛЯ ВІДПРАЦЮВАННЯ НЕ МОЖНА ПОВЕРНУТИСЯ НАЗАД(ВІДПРАЦЬОВУЄ ЛИШЕ ОДИН РАЗ)

# print(next(g))  # 0
# print(next(g))  # 25
# print(next(g))  # 50
# print('my work')  # my work
# print(next(g))  # 75
# print(next(g))  # 100
# print('go to eat!')  # go to eat!
# print(next(g))  # 125


# g = (i for i in range(5))
# # цикл відпрацьовує лише один раз
# for item in g:
#     print(item)

#                                             ГЕНЕРАТОРИ ЗА ДОПОМОГОЮ ФУНЦІЙ

# def gen(name):
#     for ch in name:
#         yield ch
#         print('jjsvjvbjhd')
#
#
# g = gen('Max')
# print(next(g))  # M
# print(next(g))  # a
# print(next(g))  # x


# def gen():
#     yield 1
#     yield 2
#     yield 3
#     return 'return' # StopIteration: return
#
#
# g = gen()
# print(next(g))  # 1
# print(next(g))  # 2
# print(next(g))  # 3
# print(next(g)) # StopIteration: return

# def gen_file_name():
#     count = 0
#     while True:
#         yield f'file-{count}.jpg'
#         count += 1
#
#
# gen = gen_file_name()
#
# print(next(gen))  # file-0.jpg
# print(next(gen))  # file-1.jpg
# print(next(gen))  # file-2.jpg
# print(next(gen))  # file-3.jpg

# def my_range(length):
#     count = 0
#     while count < length:
#         yield count
#         count += 1
#
#
# for i in my_range(5):
#     print(i)

# ЗА ДОПОМОЮ ГЕНЕРАТОРІВ МОЖНА РОБИТИ ЧЕРГУ

# def gen1(n):
#     for i in range(1, n + 1):
#         yield f'{i}-Team1'
#
#
# def gen2(n):
#     for i in range(1, n + 1):
#         yield f'{i}-Team2'
#
#
# teams = [gen1(8), gen2(6)]
#
# while teams:
#     team = teams.pop(0)
#     try:
#         print(next(team))
#         teams.append(team)
#     except StopIteration:
#         pass


#                                 РЕАЛІЗАЦІЯ ГЕНЕРАТОРІВ ЗА ДОПОМОГОЮ КЛАСІВ

# class MyRange:
#     def __init__(self, length):
#         self.__length = length
#         self.__counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__counter < self.__length:
#             res = self.__counter
#             self.__counter += 1
#             return res
#         raise StopIteration
#
#
# # for i in MyRange(5):
# #     print(i)
#
# my_range = MyRange(3)
# print(next(my_range))  # 1
# print(next(my_range))  # 2
# print(next(my_range))  # 3


#                                                                              РОБОТА З ТЕКСТОВИМИ ФАЙЛАМИ

# file = open('1.txt')
# print(file.read()) # прочитає весь файл, можна передати скільки Байтів хочеш прочитати 1 символ=1байт(латиниця), кирилиця 1сим=2 байт
# print(file.readline()) # прочитає по стрічково, залежно від к-сті запитів, працює як next
# print(file.readlines()) # повертає список свіх строчок
# file.seek(2) #переводить курсол на символ який вказаний у ньому
# file.close() # закривати обовязково після роботи з файлами

#                                                                                    АБО
# try:
#     file = open('1.txt')
#     try:
#         print(file.read())
#     finally:
#         file.close()
# except Exception as err:
#     print(err)

#                                                            КОНТЕКСНИЙ МЕНЕДЖЕР WITH

#                                                      READ
# try:
#     with open('1.txt') as file:
#         print(file.read())
# except Exception as err:
#     print(err)

#                                                           WRITE (створить новий файл і запише дані)
#                                            (якщо записувати в файл в якому щось є, то видалить все що там є і запише нову інфу)
# try:
#     with open(file='2.txt', mode='w') as file:
#         file.write('some\ntext\n')
#         # file.writelines(['max', 'hello', 'world']) # maxhelloworld запише все в одну лінію без пробілів
#         file.writelines(['max\n', 'hello\n', 'world']) # запише все з нового рядка
# except Exception as err:
#     print(err)


#                                                                ДОДАВАННЯ ДО ІСНУЮЧОГО
# try:
#     with open(file='1.txt', mode='a') as file:  # буде створювати файл якщо він не існує, помилок майже не кидає a=append
#         file.write('asd')
# except Exception as err:
#     print(err)

#                                                                   ГІБРИДНІ ВИДИ
# mode='r+'  режим читання та запису
# mode='w+' якщо файл існував то він його затре
# mode='x' створює файл і повертє помилку якщо такий файл вже існує

# try:
#     with open(file='2.txt', mode='r+') as file:
#         print(file.readline()) # some
#         file.write('sssssssssssssssssssssss\n')
# except Exception as err:
#     print(err)

# #                                              РОБОТА З БІНАРНИМИ ФАЙЛАМИ ЗА ДОПОМОГОЮ ГЕНЕРАТОРА(для їх розмноження)
# # mode='rb' читання бінарних даних
# def gen_file_name():
#     count = 0
#     while True:
#         yield f'file-{count}.jpg'
#         count += 1
#
#
# gen = gen_file_name()
#
# try:
#     with open('panda.jpeg', 'rb') as file:
#         for i in range(5):
#             with open(next(gen), 'wb') as f:
#                 read = file.read()
#                 f.write(read)
#                 file.seek(0)
# except Exception as err:
#     print(err)


#                                           ЗБЕРІГАННЯ ДАНИХ В ФОРМАТІ JSON
# import json
#
# users = [
#     {'name': 'Max', 'age': 20},
#     {'name': 'Kira', 'age': 15},
#     {'name': 'Marina', 'age': 25},
#     {'name': 'Maria', 'age': 22}
# ]
# #                                               ЗАПИС ФАЙЛІВ
# try:
#     with open('users.json', 'w') as file:
#         json.dump(users, file)
# except Exception as err:
#     print(err)
#
# #                                                   ПРОЧИТАТИ ДАНІ
#
# try:
#     with open('users.json', 'r') as file:
#         users: list = json.load(file)
#         for i in users:
#             print(i)
# except Exception as err:
#     print(err)


#                                ЗАПИС ТА ЗБЕРІГАННЯ РІЩНИХ ТИПІВ ДАНИХ

import pickle

# users = [
#     {'name': 'Max', 'age': 20},
#     {'name': 'Kira', 'age': 15},
#     {'name': 'Marina', 'age': 25},
#     {'name': 'Maria', 'age': 22}
# ]
#
# try:
#     with open('data', 'wb') as file:
#         pickle.dump(users, file)
# except Exception as err:
#     print(err)

#                                        ЧИТАННЯ БІНАРНИХ ДАНИХ


# try:
#     with open('data', 'rb') as file:
#         users: list = pickle.load(file)
#         for i in users:
#             print(i)
# except Exception as err:
#     print(err)


#                                                     PATTERN MATCH (СХОЖЕ НА SWITCH CASE IN JS)
# може перевіряти типи даних і щось з ними робити

# choice = input('Make your choice: ')
#
# match choice:
#     case '1':
#         print('1')
#     case '2':
#         print('2')
#     case _:
#         print('default')

# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# user = User('Max', 20)
#
# user_dict = {
#     'name': 'Alise',
#     'age': 20
# }


# def matcher(source: User | dict):
#     if isinstance(source, User):
#         print(source.name)
#     if isinstance(source, dict):
#         print(source['name'])
#
#
# matcher(user)  # Max
# matcher(user_dict)  # Alise

# class User:
#     __match_args__ = ('name', 'age')
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# user = User('Max', 66)
#
# user_dict = {
#     'name': 'Alise',
#     'age': 20
# }
#
#
# def matcher(source: User | dict):
#     match source:
#         case User(_, age=3 as age):
#             print(f'{age=}')
#         case User(_, age):
#             print('User(_, age)', age)
#         case {'name': 'Alise' as name}:
#             print(name)
#         case {'name': name}:
#             print(name)
#         case _:
#             print('Not found!')
#
#
# matcher(user)

#                                         ДЕСТРУКТУРИЗАЦІЯ

action = 'left 350 fhsfg hgsjghs'.split()

match action:
    case 'top' | 'left' as ac, '150'| '350' as val:
        print("'top' | 'left' as ac, '150'")
    case ac, val:
        print(f'{ac=} {val=}')
    case ac, val, *arg:
        print(f'{ac=} {val=} {arg=}')