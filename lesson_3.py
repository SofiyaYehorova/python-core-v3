#                                                               КЛАСИ

# class User:
#     # __slots__ = ('name', 'age')  # обмежує к-сть полів у екземплярі класуб зменшує навантаження на память
#     count = 0
#
#         self.age = age
#         self.name = name
#         self.count = 99
#
#
# print(User.count)  # 0
#
# user1 = User('Max', 20)
# # user2 = User('Maria', 20)
# # User.count = 95
# # print(user1.count)  # 99
# # print(user2.count)  # 99
# # print(User.count)  # 95
#
# #                                                       ДОДАВАННЯ ПРОПЕРТІВ
# user1.house = 65
# print(user1.house)  # 65
#
# #                                                       ВИДАЛЕННЯ ПРОПЕРТІВ
#
# del user1.house
# print(user1.house)  # 'User' object has no attribute 'house'

#                                                               ПРИВАТНІСТЬ

# __  # ПРИВАТНА ЗМІНА
# _  # ЗАХИЩЕНА ЗМІНА


# class User:
#     __count = 0
#
#     def __init__(self, name):
#         self.__name = name
#         self.age = 15
#
#
# # print(User.__count) # NameError: name '__' is not defined
# user = User('Max')
# print(user.age)
# # print(user._name)
#
# # print(user._User__name) # Max
# # print(User._User__count) # 0

#                                                                  НАСЛІДУВАННЯ

# class Car:
#     def __init__(self, brand, model, year):
#         self.year = year
#         self.model = model
#         self.brand = brand
#
#
# class Greeting:
#     def greeting(self):
#         print('Hello')
#
#
# class SuperCar(Car, Greeting):
#     def __init__(self, brand, model, year, battery):
#         super().__init__(brand, model, year)
#         self.battery = battery
#
#
# car = SuperCar('BMW', 'Z6', 2012, None)
# print(car.greeting())

#                                                               ІНКАПСУЛЯЦІЯ


# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def delete_name(self):
#         del self.__name
#
#
# user = User('Max')
# print(user.get_name()) # Max
# user.set_name('Karina')
# print(user.get_name()) # Karina
# user.delete_name()
# print(user.get_name()) # 'User' object has no attribute '_User__name'

#                                                         PROPERTIES


# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     def __set_name(self, name):
#         self.__name = name
#
#     def __get_name(self):
#         return self.__name
#
#     def __delete_name(self):
#         del self.__name
#
#     name = property(fget=__get_name, fset=__set_name, fdel=__delete_name)
#
#
# user = User('Max')
# user.name = "Karina"
# print(user.name) # Karina


#                                                         АБО

# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name=name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#
# user = User('Max')
# user.name = 'Karina'
# # del user.name
# print(user.name)

#                                                   ПОЛІМОРФІЗМ
#                                      (можливість представлення одного тиау даних через інший)

# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimetr(self):
#         pass
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.c = c
#         self.b = b
#         self.a = a
#
#     def area(self):
#         return self.a * self.b * self.c
#
#     def perimetr(self):
#         return self.a + self.b + self.c
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.b = b
#         self.a = a
#
#     def area(self):
#         return self.a * self.b
#
#     def perimetr(self):
#         return (self.a * self.b) * 2

#
# shapes: list[Shape] = [Triangle(1, 2, 3), Rectangle(4, 5), Triangle(5, 6, 7)]
#
# for shape in shapes:
#     print(shape.area())
#     print(shape.perimetr())


#                                                   ДЕКОРАТОРИ


#                                                               КЛАСОВИЙ МЕТОД

#     class User:
#         __count = 0
#
#         def __init__(self, name, age):
#             self.age = age
#             self.name = name
#
#         @classmethod
#         def get_count(cls):
#             return cls.__count
#
#         @classmethod
#         def inc_count(cls):
#             cls.__count += 1
# #     def __init__(self, name, age):
#
# User.inc_count()
# User.inc_count()
# User.inc_count()
# User.inc_count()
# User.inc_count()
# User.inc_count()
# User.inc_count()
# User.inc_count()
# print(User.get_count()) # 8

#                                                                  СТАТИЧНИЙ МЕТОД
# немає доступу до методів вказаного класу, роблять що стороне але в межах вказаного класу. Можна викликати як від екземплярів класу так і від самого класу

# class User:
#     __count = 0
#
#     def __init__(self, name, age):
#         self.age = age
#         self.name = name
#
#     @classmethod
#     def get_count(cls):
#         return cls.__count
#
#     @classmethod
#     def inc_count(cls):
#         cls.__count += 1
#
#     @staticmethod
#     def greeting():
#         print('hello')
#
# User.inc_count()
# User.inc_count()
# User.inc_count()
# User.inc_count()
# User.inc_count()
# print(User.get_count()) #5
# User.greeting() # hello


#                                                ПЕРЕГРУЗКА МЕТОДІВ

# class User:
#     def __init__(self, name, age):
#         self.age = age
#         self.name = name
#
#     def __str__(self):
#         return f'{self.name}-{self.age}'
#
#     def __len__(self):
#         return len(self.name)
#
#     def __add__(self, other):
#         return self.age + other.age
#
#     def __sub__(self, other):
#         return self.age - other.age
#
#     def __mul__(self, other):
#         return self.age * other.age
#
#     def __lt__(self, other):
#         return len(self.name) < len(self.name)
#
#
# user1 = User('Max', 15)
# user2 = User('Marina', 35)
#
# print(user1)  # Max-15
# print(len(user1))  # 3
#
# print(user1 + user2)  # 50
# print(user1 - user2)  # -20
# print(user1 * user2)  # 525
# print(user1 < user2)  # False


#                                     ПАТЕРНИ
# class User:
#     __instance = None
#     count = 0
#
#     def __new__(cls, *args, **kwargs):
#         if not isinstance(cls.__instance, cls):
#             cls.__instance = super().__new__(cls)
#
#         return cls.__instance
#
#     def __init__(self, name):
#         self.name = name
#         User.count += 1
#
#
# user1 = User('Karina')
# user2 = User('Marina')
# print(user1) # <__main__.User object at 0x7fd1f055bdc0>
# print(user2) # <__main__.User object at 0x7fd1f055bdc0>
# print(user1 is user2) # True


#                                                         CALL

# class Prod:
#     def __init__(self, value):
#         self.value = value
#
#     def __call__(self, inc):
#         self.value += inc
#
#     def __str__(self):
#         return str(self.value)
#
#
# prod = Prod(20)
# print(prod)  # 20
# prod(50)
# print(prod)  # 70


# class Array:
#     def __init__(self, *args):
#         self.__arr = [*args]
#
#     def __str__(self):
#         return str(self.__arr)
#
#     def length(self):
#         return len(self.__arr)
#
#     def __setitem__(self, key, value):
#         self.__arr[key] = value
#
#     def __getitem__(self, key):
#         return self.__arr[key]
#
#     def __delitem__(self, key):
#         del self.__arr[key]
#
#     def map(self, cb):
#         return Array(*[cb(item) for item in self.__arr])
#
#     def push(self, item):
#         return self.__arr.append(item)


# array = Array()
# print(array)  # []
# array.push(2)
# array.push(3)
# print(array)  # [2, 3]
# print(array[0], 'siddhdj') # 2 siddhdj
# array[1] = 'hvhjvchjv'
# del array[1]
# print(array.length())
# print(array)

# maps
# array = Array(1, 2, 3, 4, 5)
# array2 = array.map(lambda x: x ** 2)
# print(array) # [1, 2, 3, 4, 5]
# print(array2) # [1, 4, 9, 16, 25]
