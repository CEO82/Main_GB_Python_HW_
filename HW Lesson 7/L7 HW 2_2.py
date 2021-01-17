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

# For Teacher: Добрый день! К сожалению не додумал как из класса выводить персонализовано по объектам
# название конкретного изделия поэтому незвания зашил в одном общем принте в самом конце, после объектов класса
# как пойму как это можно сделать более правильно исправлю код;)

from abc import ABC, abstractmethod

class Clothes(ABC):

    # атрибуты класса:

    # Конструктор с атрибутами объекта:
    def __init__(self, size, growth):
        self.s = size
        self.growth = growth

    # методы класса:
    @abstractmethod
    def fabricCalc(self):
        pass



class Coat(Clothes):

    # атрибуты класса:
    # Конструктор с атрибутами объекта:
    # методы класса:
    @property
    def fabricCalc(self,):
        textileCoat = float(self.s) / 6.5 + 0.5
        textileCoat is globals()
        return textileCoat
        # return f"Требуемое кол-во ткани для Пальто: {textileCoat:.02f}"

class Suit(Clothes):

    # атрибуты класса:
    # Конструктор с атрибутами объекта:
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
        textileSuit = float(self.growth) * 2 + 0.3
        textileSuit is globals()
        return textileSuit


# Объект класса:

versachiCoat = Coat(90, 154)
bossSuit = Suit(70, 190)
aVerText = versachiCoat.fabricCalc
bBosTExt = bossSuit.fabricCalc
totalText = aVerText + bBosTExt

print(f'Для производства Пальто потребуется {aVerText:.02f}m ткани,\nДля производства костюма {bBosTExt:.02f}m ткани,\nВсего нужно будет {totalText:.02f}m ткани')



