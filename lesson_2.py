#                                                          ДЕСТРУКТИРИЗАЦІЯ TUPLES

# tuple1 = (1, 2)
# a, b = tuple1
#
# print(a, b)


# a = 5
# b = 7
#
# b, a = a, b
# print(a, b)  # a=7, b=5

# t = (1, 2, 3)
# a, b = t  # error
# print(a)


# l = [1, 2, 3, 4, 6, 8, 9]

# a, b, c, _, _, _, j = l
# print(a, b, c, j)  # 1, 2, 3, 9
#                                           OR
# a, b, *_=l
# print(a, b)  #1, 2
# print(_) # [3, 4, 6, 8, 9]

# a, b, *_, x, y = l
# print(a, b, x, y)  # 1 2 8 9


#                                                         РОЗПАКОВКА ОБЄКТІВ
# def func(name, age, house):
#     print(name, age, house)
#
#
# user = {
#     'name': 'Max',
#     'age': '15',
#     'house': 85
# }
#
# func(**user)  # Max 15 85
# func(*user)  # name age house

# l = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = [*l, *l2]
# print(l3)  # [1, 2, 3, 4, 5, 6]

#                                                           ДЕКОРАТОРИ
# def decor(func):
#     def inner():
#         print('*' * 20)
#         func()
#         print('*' * 20)
#
#     return inner
#
#
# def greeting():
#     print('hello')
#
#
# inner = decor(greeting)
# inner()


# def decor(func):
#     def inner(*args, **kwargs):
#         print('*' * 20)
#         func(*args, **kwargs)
#         print('*' * 20)
#
#     return inner
#
#
# def greeting(name, age):
#     print(f'hello , {name}-{age}')
#
#
# inner = decor(greeting)
# inner('Sofiya', 22)


# def decor(func):
#     def inner(*args, **kwargs):
#         print('*' * 20)
#         func(*args, **kwargs)
#         print('*' * 20)
#
#     return inner


# @decor
# def greeting(name, age):
#     print(f'hello , {name}-{age}')
#
#
# greeting('Sofiya', 35)

# @decor
# @decor
# def greeting(name, age):
#     print(f'hello , {name}-{age}')
#
#
# greeting('Sofiya', 35)

#                                      ІМПОРТ БІБЛІОТЕК
# import time
#
#
# def time_decor(func):
#     def inner(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         print(time.time() - start_time)
#
#     return inner
#
#
# @time_decor
# def foo():
#     for i in range(1000000):
#         pass
#     print('finish')
#
#
# foo()


#                                                          SCOPE

# for i in range(5):
#     print(i)
# print(i)

# name = 'Max'
#
#
# # def a():
# #     name = 'Karina'
# #
# #
# # a()
# # print(name)  # Max
#
# def a():
#     global name
#     name = 'Karina'
#
#
# a()
# print(name)  # Karina


# name = 'Max'
#
#
# def a():
#     name = 'Kiril'
#
#     def b():
#         name = 'Marina'
#         print(name)
#     b()
#     print(name)
# a()


#                                                             ЗАМИКАННЯ

# def counter():
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(count)
#     return inner
#
#
# c1 = counter()
# c2 = counter()
# c1()
# c1()
# c1()
# c2()
# c1()
# c2()

#                                                                LAMBDA
# func = lambda a, b: a + b
# print(func(3, 4))  # 7

# func = lambda: 5
# print(func()) #5

# users = [
#     {'name': 'Max', 'age': 15},
#     {'name': 'Marina', 'age': 65},
#     {'name': 'Karina', 'age': 17},
#     {'name': 'Sofiya', 'age': 38},
#     {'name': 'Mark', 'age': 5}
# ]
#
# sorter_users = sorted(users, key=lambda item: item['name'])
# sorter_users1 = sorted(users, key=lambda item: item['name'], reverse=True)
# sorter_users2 = sorted(users, key=lambda item: str(item['age'])[-1])
# print(sorter_users)
# print(sorter_users1)
# print(sorter_users2)

#                                                                АНОТАЦІЯ ТИПІВ
# def greeting(name: str):
#     print(name.upper())
#
#
# greeting('sofiya')  #SOFIYA

# def func(st: str, list_of_strings: list[str]) -> None:
#     list_of_strings.append('111')
#     for item in list_of_strings:
#         print(item.upper())
# 
# 
# func1 = func('aaa', [])  # 111
# print(func1)  # None

from typing import Callable


# def counter(start_num: int) -> Callable[[int, str], int]:
#     count = start_num
#
#     def inner(a: int, b: str) -> int:
#         nonlocal count
#         count += 1
#         print(count)
#
#     return inner


def counter(start_num: int) -> Callable[[], int]:
    count = start_num

    def inner() -> int:
        nonlocal count
        count += 1
        print(count)

    return inner


c1 = counter(5)
c2 = counter(6)
print(c1())  # 6
print(c2())  # 7
