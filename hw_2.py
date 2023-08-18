# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
# 2) протипізувати перше завдання

# from typing import Callable
#
#
# # def notebook() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
# def notebook():
#     list_todo: list[str] = []
#
#     def add_todo(todo: str) -> None:
#         nonlocal list_todo
#         list_todo.append(todo)
#
#     def get_all() -> list[str]:
#         nonlocal list_todo
#         return list_todo.copy()
#
#     return add_todo, get_all
#
#
# add, all_todo = notebook()
# add('Wake up')
# add('Eat')
# add('Brush your teeth')
# add('Comb hair')
# add('Go to work')
#
# todos = all_todo()
# print(todos)


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

# def expanded_form(num: int) -> str:
#     st = str(num)
#     length = len(st) - 1
#     res = []
#     for i, ch in enumerate(st):
#         if ch!='0':
#             res.append(ch + '0' * (length - i))
#
#     return ' + '.join(res)
#
#
# print(expanded_form(111))  # 100 + 10 + 1

# def expanded_form(num: int) -> str:
#     st = str(num)
#     length = len(st) - 1
#     return ' + '.join(ch + '0' * (length - i) for i, ch in enumerate(st) if ch != '0')
#
#
# print(expanded_form(101))  # 100 + 1

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором, та буде виводити це значення після
# виконання функцій

def count_decor(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        func(*args, **kwargs)
        print(f'{count=}')

    return inner


@count_decor
def func1():
    print('func1')


@count_decor
def func2():
    print('func2')


func1()
func1()
func2()
func1()
func2()
func1()
