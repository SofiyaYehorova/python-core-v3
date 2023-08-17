# comment

"""
comments
"""
import poplib

''''
comments
'''

# print("hello world")

# print(1, 2, 3, 4)
# print(1, 2, 3, 4, sep='-')

# print(1, 2, 3, 4, sep='*', end='End\n')

# i = 3  # int
# f = 1.3  # float
# b = True  # bool
# s = "text"  # str
# n = None  # NoneType
#
# print(type(i))
# print(type(f))
# print(type(b))
# print(type(s))
# print(type(n))

# a = b = c = 10
# print(a, b, c)

# fs = str(f) # float str
# print(fs)
# print(type(fs))

#     МАТЕМАТИЧНІ ОПЕРАТОРИ

# a = 5
# # a += 1 # a=a+1
# b = 2
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)  # рузультат= завжди число з плаваючою точкою
# print(a // b)  # рузультат= відкине все що після коми
# print(round(a / b))  # результат = заокругти до найближчого парного числа
# print(a ** b) # піднесення до степеня
# print(a % b) # ділення по модулю


#  INPUT

#
# name = input('Enter your name: ')
# print(name)


#   ЛОГІЧНІ ОПЕРАТОРИ

# a = 2
# b = 3
#
# print('a < b', a < b)
# print('a <= b', a <= b)
# print('a == b', a == b)  # print('a==b', a is b)
# print('a >= b', a >= b)
# print('a > b', a > b)
# print('a != b', a != b)  # print ('a!=b', is not b)
#
# res = isinstance(a, int)
# print(res) # True
# res = isinstance(a, str)
# print(res) # False


# УМОВНІ ОПЕРАТОРИ

# name = input('Enter your name: ')
# print(name)

# age = input('Enter your age: ')
# num = int(age)
#
# if num > 10:
#     print('num>10')
# elif num == 10:
#     print('num==10')
# else:
#     print('num<10')


# check = False
#
# if not check:
#     print('Ok')

# ТЕРНАРНІ ОПЕРАТОРИ

# num = int(input('Enter num: '))
#
# res = 'yes' if num > 5 else 'no'
# print(res)


#                                                       COLLECTIONS

#                                                       list   #масив

# l = [1, 2, 3, 'hcbjsdhvhjv', True]
# print(l[2])  # 3
# print(l[-1])  # True
# l[2] = 6
# print(l[2])  # 6
# print(len(l))  # 5


#                                                        СИЛОЧНІ ТИПИ ДАНИХ


# l = [1, 2, 3, 'hcbjsdhvhjv', True]
# l2 = l
# l2[0] = 555
# print(l[0])  # 555
# print(l)
# print(l2)

# l = [1, 2, 3, 'hcbjsdhvhjv', True]
# l2 = l.copy()
# l2[0] = 555
# print(l[0])  # 1
# print(l)
# print(l2)

# МЕТОДИ

# l = [1, 2, 3, 'hcbjsdhvhjv', True, 2, 3]
# l2 = [6, 8, 3, 4, 5]
# l3 = ['b', 'z', 'm']
# l.append(55) # додаємо значення до кінця
# l.insert(0, 100) # вказуємо в який індекс що вствавляємо
# pop = l.pop()  # по замовчуванні видаляє останню значення в списку
# print(pop) # повертає значення що видалив
# pop = l.pop(1) # можна вказати значення індексу який потрібно видалити
# l.remove(2) # знайде і видалити перше значення з ліва на право
# l.extend(l2) # обєднає два списка
# #        АБО
# l = l+l2 # l+=l2
# print(l.index(3))
# print(l.index(3, 3)) # значення і з якого індексу починати
# l2.sort()
# l3.sort()
# print(l2)
# print(l3)
# print(l.count(3)) # 2 шт
# l.clear() # очищає весь список
# l2.reverse()


#                                                            ЗРІЗИ

# l = [1, 2, 3, 'hcbjsdhvhjv', True, 2, 3]

# sub = l[0:4]  # [1, 2, 3, 'hcbjsdhvhjv']  OR sub = l[:4]
# print(sub)
# sub = l[2:4]
# print(sub)  # [3, 'hcbjsdhvhjv']

# sub = l[0:4:2]
# print(sub)  # [1, 3] step 2

# sub = l[::-1] # revers
# print(sub)


#                                                                tuple


# my_tuple = (1, 2, 3, 4, 5, 5)
# print(my_tuple[1])  # 2
# my_tuple[1] = 4  # кортежі не можна змінювати
# print(my_tuple.count(5)) # 2 items
# print(my_tuple.index(3)) # 2


#                                                                  dict

# dict1 = {
#     'name': 'Max',
#     'age': 15
# }
#
# dict2 = {
#     'house': 65
# }

# print(dict1)
# print(dict1['age']) # 15

#                                                                METHOD
# get = dict1.get('name')
# print(get) # Max
# dict.get('name1', 'haha')
# print(get) # haha та як такого ключа нема, то видасть слово haha

# print(dict1.items())
# print(list(dict1.items()[0]))
# print(dict1.keys())

# pop = dict1.pop('name')
# print(pop) # Max
# print(dict1)

# popitem = dict1.popitem()
# print(popitem) # видалить останній ключ

# dict1.setdefault('age3', 55) # можна додати лише нові ключі та значення
# print(dict1)

# dict1.update(dict2)  # обєднання словників
# #                                                                АБО
# dict1 |= dict2
# print(dict1)

# print(dict1.values()) # поверне значення ключів


#                                                                  set

# set1 = {1, 2, 3, 4, 5, 2, 3, 8}  # поверне лише унікальні значення
# set2 = set()  # для сворення порожнього set
# set3 = {}  # type 'dict'
# print(type(set1))  # set
# print(type(set2))  # set
# print(type(set3))  # dict

# set2.add(4)
# set2.add(7)
# set2.add(3)
# set2.add(4)
# set2.add(7)
# print(set2)  # {3,4,7}

# set1 = {1, 2, 3, 4}
# set2 = {5, 6, 7, 8, 1, 2}
# print(set1.issuperset(set2))  # мають ті самі елементи що в іншому False
# print(set1.issubset(set2))  # чи є цей set підсетом іншого False
# print(set1.isdisjoint(set2))  # якщо нема спільних елементів False
# print(set1.intersection(set2))  # що одинакове і зробить новий set
# print(set1.symmetric_difference(set2))  # що різне та унікальне і зробить новий set

# difference = set1.symmetric_difference(set2)
# l = list(difference)
# print(difference)
# print(l)
# print(type(difference)) # set
# print(type(l)) # list

# set1.remove(2) # видаляє значення а не індекс
# set1.discard(656898)  # видаляє значення, але якщо його нема не викидає помилку
# set1.pop()  # видаляє випадковий елемент
# pop = set1.pop()
# print(pop)  # і поверає його


#                                                        string

# string = "name = 'Vasyl \"'"
# print(string)

# st = '*'*50
# print(st)

# name = 'Max'
# age = 18
# weight = 70.6
#
# string = 'Hello my name is Max, I`m 18 and my weight 70.6 kg'
# string = 'Hello my name is ' + name + ', I`m ' + str(age) + ' and my weight ' + str(weight) + ' kg'
# string = 'Hello my name is %s, I`m %i and my weight %f kg' %(name, age, weight)
# string = 'Hello my name is {}, I`m {} and my weight {} kg'.format(name, age, weight)
# string = 'Hello my name is {name}, I`m {age} and my weight {weight} kg'.format(age=age, weight=weight, name=name)
# string = f'Hello my name is {name}, I`m {age} and my weight {weight} kg'
# print(string)

# METHODS

# print(string.index('llo')) #2
# print(string.count('l')) # 2
# print(string.capitalize())
# print(string.upper())
# print(string.lower())
# print(string.islower())
# print(string.isupper())

# print('hello world'.title()) # Hello World
# print('Hello World'.swapcase()) #hELLO wORLD
# print('asd'.isalpha()) #чи все букви
# print('11111'.isdigit()) # чи все цифри
# print('111і11'.isalnum()) # чи цифри і букви якщо є пробіли буде False
# print('hello'.startswith('h')) # True
# print('hello'.endswith('h')) # False

# print(['         jffjsf         '.strip()])  # обріже пробіли з обох сторін
# print(['         jffjsf         '.lstrip()])  # обріже пробіли з лівої сторін
# print(['         jffjsf         '.rstrip()])  # обріже пробіли з правої сторін
# print(['aaaaaaaa        jffjsf         aaaaaaaaaaa'.strip('a ')])  # обріже пробіли з обох сторін за вказанити параметрами

# print('hello world'.split()) # сплітане по пробілу ['hello', 'world']
# print('hello-world'.split('-')) # сплітане по сепаратору ['hello', 'world']
# print('hello is hello'.partition('is')) # ('hello ', 'is', ' hello')

# l= ['1', '2', '3']
# print(''.join(l)) #123
# print('-'.join(l)) #1-2-3

# print('      '.isspace()) # чи є пробіли True
# print(''.isspace()) # чи є пробіли False

# print('hello world'.replace('l', 'L')) #heLLo worLd

# print('hello world'[1]) # e
# print('hello world'[:8]) # hello wo


# print(min([4, 2, 5, 10]))
# print(max([4, 2, 5, 10]))
# print(sum([4, 2, 5, 10]))
# l = sorted([1, 5, 4, -15, 3])
# l2 = print(sorted([1, 5, 9, -15, 50], reverse=True))
# res = pow(2, 5)  # ** поднести два до пятої степені
# print(res)
#
#                                                      FUNCTIONS

# def func():
#     print('hello')
#
# func()

# def func(a, b, c):
#     print(a, b, c)
#
# func(1, 2, 3)

# def func(a, b, c=22, *args, **kwargs):
#     print(a, b, c)
#     print(args)
#     print(kwargs)
#
# func(1, 2 , 3333, 5, 6, 8 , name='Max', age=18)


# l = [1, 2, 3]
# user = {
#     'name': 'Max',
#     'age': 15
# }
#
# def func(a, b,c, name, age):
#     print(a, b,c)
#     print(name, age)
#
# func(*l, **user)
# func(*l, *user)


#                                                          ЦИКЛИ
#                                 WHILE
# i=5
#
# while i>0:
#     i-=1
#     if i == 2:
#         continue
#     print(i)
# else:
#     print('finish')


#                                             FOR IN
# users = ['Olga', 'Igor', 'Masha']

# for user in users:
#     print(user)

# for i, user in enumerate(users): # index, value
#     print(i, user)

# for i in range(50):
#     print(i)

# for i in range(5, 50, 5): # from to step
#     print(i)


# user = {
#     'name': 'Max',
#     'age': 18,
#     'house': 85
# }
#
# for k, v in user.items():
#     print(k)
#     print(v)


# l = [i for i in range(10)]
# print(l)

# l = [1, 2, 3, 4, 5, 6]

# res = [i for i in l if i % 2 == 0]# [2, 4, 6]
# res = [i**2 for i in l] # [1, 4, 9, 16, 25, 36]
# res = [str(i**2) for i in l] # ['1', '4', '9', '16', '25', '36']
# res=[str(i**2) for i in l if i%2==0] #['4', '16', '36']
# print(res)


#                                            ЦИКЛ В ЦИКЛІ

# super_list = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10]
# ]

# res = [i for j in super_list for i in j] #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#                                                   АБО

# res = []
# for j in super_list:
#     for i in j:
#         res.append(i)
#
# print(res)



dict1 = {'NaMe': 'Olga', 'aGe':20}

dict2= {k.lower(): v for k,v in dict1.items()}  #{'name': 'Olga', 'age': 20}
print(dict2)

