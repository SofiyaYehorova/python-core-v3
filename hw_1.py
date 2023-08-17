# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.


# st = 'as 23 fdfdg544'
# print(', '.join(num for num in st if num.isdigit()))

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі


# st = 'as 23 fdfdg544 34'
# print(', '.join(''.join(ch if ch.isdigit() else ' ' for ch in st).split()))

# #################################################################################
#
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
#

#
# greeting = 'Hello, world'
# print([ch.upper() for ch in greeting])

# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
#

# print([i**2 for i in range(50) if i%2])


# function
#
# - створити функцію яка виводить ліст

l = [1, 2, 3, 4, 5]


def show_list(arr):
    print(arr)


show_list(l)


# - створити функцію яка приймає три числа та виводить та повертає найбільше.

def max_num(a, b, c):
    max_num = max(a, b, c)
    print(max_num)
    return max_num


max_num(5, 10, -9)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

def min_max(*args):
    print(max(args))
    return min(args)


min_max(5, 10, 15, -16, -60)


# - створити функцію яка повертає найбільше число з ліста

def max_of_list(arr):
    return max(arr)


# - створити функцію яка повертає найменьше число з ліста
def min_of_list(arr):
    return min(arr)


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

def sum_of_list(arr):
    return sum(arr)


# - створити функці:ю яка приймає ліст чисел та повертає середнє арифметичне його значень.
#
def avg_of_list(arr):
    return sum(arr) / len(arr)


#
#
# ################################################################################################
# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]

list_1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#   - знайти мін число

min_of_list(list_1)


#   - видалити усі дублікати

def duplicate():
    l_copy = list_1.copy()
    print(list(set(l_copy)))


duplicate()


#   - замінити кожне 4-те значення на 'X'

def to_X():
    l_copy = list_1.copy()
    # print(['X' if not (i+1)%4 else item for i, item in enumerate(l_copy)])

    for i in range(3, len(l_copy), 4):
        l_copy[i] = 'X'
    print(l_copy)


to_X()


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')


square(5)


# 3) вывести табличку множення за допомогою цикла while

def multi_table():
    size = 9
    i = 1
    while i <= size:
        j = 1
        while j <= size:
            res = i * j
            # print(' ' if res // 10 else ' ', end='')
            # print(res, end='')
            print(f'{res:4}', end='')
            j += 1
        print()
        i += 1


multi_table()

# 4) переробити це завдання під меню

while True:
    print('1) знайти мін число')
    print('2) видалити усі дублікати')
    print('3) замінити кожне 4-те значення на \'X\'')
    print('4) вивести на екран пустий квадрат з "*"')
    print('5) вывести табличку множення за допомогою цикла while')
    print('9) Вихід')

    choice = input('Зробіть свій вибір: ')

    if choice == '1':
        print(min_of_list(list_1))
    elif choice == '2':
        duplicate()
    elif choice == '3':
        to_X()
    elif choice == '4':
        square(5)
    elif choice == '5':
        multi_table()
    elif choice == '9':
        break
