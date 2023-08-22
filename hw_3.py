# Створити клас Rectangle:
# -він має приймати дві сторони x, y
# -описати поведінку на арифметични методи:
# + сумма площин двох екземплярів ксласу
# - різниця площин двох екземплярів ксласу
# == площин на рівність
# != площин на не рівність
# >, < меньше більше
# при виклику метода len() підраховувати сумму сторін
#

# from typing import Self
#
#
# class Rectangle:
#     def __init__(self, x, y):
#         self.y = y
#         self.x = x
#         self.area = x * y
#
#     def __add__(self, other: Self):
#         return self.area + other.area
#
#     def __sub__(self, other: Self):
#         return self.area - other.area
#
#     def __eq__(self, other: Self):
#         return self.area == other.area
#
#     def __ne__(self, other: Self):
#         return self.area != other.area
#
#     def __lt__(self, other: Self):
#         return self.area < other.area
#
#     def __gt__(self, other: Self):
#         return self.area > other.area
#
#     def __len__(self):
#         return (self.x + self.y) * 2

# ###############################################################################
#
# створити класс Human(name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім 'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу також має бути метод классу який буде виводити це значення
#

class Human:
    def __init__(self, name, age):
        self.age = age
        self.name = name


class Cinderella(Human):
    __count = 0

    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.__count += 1

    @classmethod
    def get_count(cls):
        print(cls.__count)


class Prince(Human):
    def __init__(self, name, age, foot_size_found):
        super().__init__(name, age)
        self.foot_size_found = foot_size_found

    def find_cinderella(self, cinderellas: list[Cinderella]):
        for cinderella in cinderellas:
            if self.foot_size_found == cinderella.foot_size:
                print(cinderella.__dict__)
                return
        print('Not found!')


cinderellas = [
    Cinderella('Olga', 20, 35),
    Cinderella('Kamila', 25, 38),
    Cinderella('Marina', 28, 37),
    Cinderella('Sofiya', 30, 36),
    Cinderella('Halyna', 35, 37),
    Cinderella('Bogdana', 38, 38.5),
    Cinderella('Victorya', 40, 39)
]

prince = Prince('Max', 30, 38.5)
prince.find_cinderella(cinderellas)
# ###############################################################################
#
# 1) Створити абстрактний клас Printable, який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine. в кожного  в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати eкземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine
# инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
#
# Приклад:
#
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()
#
# для перевірки ксассів використовуємо метод isinstance, приклад:
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False

from abc import ABC, abstractmethod


class Printable(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def print(self):
        print(f'Book: {self.name}')


class Magazine(Printable):
    def print(self):
        print(f'Magazine: {self.name}')


class Main:
    __printable_list: list[Printable] = []

    @classmethod
    def add(cls, item: Printable):
        # if isinstance(item, Book) or isinstance(item, Magazine):
        # if isinstance(item, (Book, Magazine)):
        if isinstance(item, Printable):
            cls.__printable_list.append(item)
        else:
            print('Ignore....')

    @classmethod
    def show_all_book(cls):
        for item in cls.__printable_list:
            if isinstance(item, Book):
                item.print()

    @classmethod
    def show_all_magazine(cls):
        for item in cls.__printable_list:
            if isinstance(item, Magazine):
                item.print()


class Car:
    pass


Main.add(Book('Alhimik1'))
Main.add(Magazine('vogue2'))
Main.add(Magazine('vogue3'))
Main.add(Book('Alhimik5'))
Main.add(Magazine('vogue6'))
Main.add(Book('Alhimik4'))
Main.add(Magazine('vogue7'))
Main.add(Book('Alhimik5'))
Main.add(Magazine('vogue7'))
Main.add(Book('Alhimik8'))


Main.show_all_magazine()
print('*' * 20)
Main.show_all_book()
