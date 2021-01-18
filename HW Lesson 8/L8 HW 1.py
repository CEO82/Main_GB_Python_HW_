# 1. Реализовать класс «Дата»,
#   1) функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год».
#   2) В рамках класса реализовать два метода.
#   Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число».
#   Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12).
#   Проверить работу полученной структуры на реальных данных.

class Date:

    # атрибуты класса:
    # Конструктор с атрибутами объекта:
    def __init__(self, day, mounth, year):
        self.d = day
        self.m = mounth
        self.y = year

    # методы класса:
    @classmethod
    def dateKonvert(cls, date):
        pass
        try:
            date = date.split('-')
            dateList = list(map(int, date))
            d, m, y = dateList

        except (ValueError, AttributeError):
            print('Entered wrong date or wrong format of date! Please repeat enter!')
        else:
            return cls(d, m, y)

    @staticmethod
    def checkDate(obj):
        if 32 > obj.d > 0 and obj.m != 2:
            obj.d = obj.d
        elif obj.m == 2 and 28 > obj.d > 0:
            obj.d = obj.d
        else:
            obj.d = 0
            print('Wrong Day! Please reenter date')

        if 13 > obj.m > 0:
            obj.m = obj.m
        else:
            obj.m = 0
            print('Wrong Month! Please reenter date')

        if 2022 > obj.y > 1899:
            obj.y = obj.y
        else:
            obj.y = 0
            print('Wrong Year! Please reenter date')

        if obj.y != 0 and obj.m != 0 and obj.d != 0:
            return f'Date is correct! {obj.d}-{obj.m}-{obj.y}'

# Объект класса:
print(f'Enter date from 01-01-1900 to 31-12-2021')
usrDate = '15-12-2021'
print(f'Entered date: {usrDate}\n')

myDate = Date.dateKonvert(usrDate)
try:
    print(f'Day is: {myDate.d}')
    print(f'Month is: {myDate.m}')
    print(f'Year is: {myDate.y}')
    print(Date.checkDate(myDate))
except AttributeError:
    print('Entered wrong date or wrong format of date! Please repeat enter!')


