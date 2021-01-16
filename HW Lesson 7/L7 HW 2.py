# 2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер ( для пальто) и рост ( для костюма) . Это могут быть обычные числа: V и
# H , соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5) , для костюма (2*H + 0.3) . Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property .

from abc import ABC, abstractmethod

class Clothes(ABC):

    # атрибуты класса:
    # Конструктор с атрибутами объекта:
    # методы класса:
    @abstractmethod
    def fabricCalc(self):
        pass

class Coat(Clothes):
    pass
    # атрибуты класса:
    # Конструктор с атрибутами объекта:
    def __init__(self, size):
        self.s = size

    # методы класса:
    @property
    def fabricCalc(self,):
        textile = float(self.s) / 6.5 + 0.5
        return f"Требуемое кол-во ткани для Пальто: {textile:.02f}"

class Suit(Clothes):
    pass
    # атрибуты класса:

    # Конструктор с атрибутами объекта:
    def __init__(self, growth):
        self.growth = growth

    # методы класса:
    @property
    def growth(self):
        return self.__growth

    @growth.setter
    def growth(self,growth):
        if growth > 220:
            self.__growth = 220
        elif growth < 130:
            self.__growth = 130
        else:
            self.__growth = growth

    @property
    def fabricCalc(self):
        textile = float(self.growth) * 2 + 0.3
        return f"Требуемое кол-во ткани для Костюма: {textile:.02f}"

# Объект класса:

versachiCoat = Coat(90)
bossSuit = Suit(155)

print(versachiCoat.fabricCalc)
print(bossSuit.fabricCalc)
