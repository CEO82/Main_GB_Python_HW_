# 4.
#   Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
# параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# 5.
#   Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
# оргтехники на склад и передачу в определённое подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру (например, словарь).
# 6.
#   Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

    # атрибуты класса:
    # Конструктор с атрибутами объекта:
    # методы класса:
# Объект класса:

"""Через этот класс обрабатывается ввод типов оборудования"""
class ElectronicItems:

    # атрибуты класса:
    # Конструктор с атрибутами объекта:
    def __init__(self, brand, model, color, paperType, price):
        self._brand = brand
        self._model = model
        self._color = color
        self._paperType = paperType
        self._price = price
    # методы класса:
# Объект класса:

@property
def brand(self):
    return self._brand

class Printers(ElectronicItems):
    # атрибуты класса:
    # Конструктор с атрибутами объекта:
    def __init__(self, brand, model, color, paperType, price, printingType):
        ElectronicItems().__init__(brand, model, color, paperType, price)
        self.printingType = printingType
    # методы класса:
# Объект класса:

class Scaner(ElectronicItems):
    # атрибуты класса:
    # Конструктор с атрибутами объекта:
    def __init__(self, brand, model, color, paperType, price, resolution):
        ElectronicItems().__init__(brand, model, color, paperType, price)
        self.resolution = resolution
    # методы класса:
# Объект класса:

class Scaner(ElectronicItems):
    # атрибуты класса:
    # Конструктор с атрибутами объекта:
    def __init__(self, brand, model, color, paperType, price, resolution):
        ElectronicItems().__init__(brand, model, color, paperType, price)
        self.resolution = resolution
    # методы класса:
# Объект класса:


class Monitor(ElectronicItems):
    # атрибуты класса:
    # Конструктор с атрибутами объекта:
    def __init__(self, brand, model, color, paperType, price, resolution):
        ElectronicItems().__init__(brand, model, color, paperType, price)
        self.resolution = resolution
    # методы класса:
# Объект класса:


class Storage:
    # атрибуты класса:
    # Конструктор с атрибутами объекта:
    # методы класса:
# Объект класса: