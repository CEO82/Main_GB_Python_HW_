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

class Printer(ElectronicItems):
    # атрибуты класса:
    # Конструктор с атрибутами объекта:
    def __init__(self, brand, model, color, paperType, price, printingType):

        self.printingType = printingType
        super().__init__(brand, model, color, paperType, price)


    # методы класса:
# Объект класса:

class Scanner(ElectronicItems):
    # атрибуты класса:
    # Конструктор с атрибутами объекта:
    def __init__(self, brand, model, color, paperType, price, resolution):
        super().__init__(brand, model, color, paperType, price)
        self.resolution = resolution

    # методы класса:
# Объект класса:


class Monitor(ElectronicItems):
    # атрибуты класса:
    # Конструктор с атрибутами объекта:
    def __init__(self, brand, model, color, price, width, resolution):
        self.resolution = resolution
        self.width = width
        self._brand = brand
        self._model = model
        self._color = color
        self._price = price
    # методы класса:
# Объект класса:


class Storage:
    # атрибуты класса:
    __itemIn = dict()
    __itemOut = dict()

    # Конструктор с атрибутами объекта:
    # методы класса:
    """Ввод изделий на склад"""
    def inputItems(self, key, arg):
        if self.__itemIn.get(key - 1) ==None:
            self.__itemIn[key - 1] = 0
        self.__itemIn[key - 1] = arg
        # print(f'Список внесенных на склад позиций: {self.__itemIn}')

    """Выдача со склада"""
    def outputItems(self, key, arg):
        rest = self.__itemIn.get(key - 1)
        if rest != None and rest >= arg:
            self.__itemIn[key - 1] -= arg
            if self.__itemIn[key - 1] == 0:
                del self.__itemIn[key - 1]

    def num(self, key):
        value = self.__itemIn.get(key - 1)
        return value if value != None else 0

    """Наличие на складе"""
    def itemsInStock(self):
        print(f'\n----------------------\nЗапасы на складе\n----------------------')
        for i in self.__itemIn:
            print(f'{models[i]._model} - {self.num(i + 1)} шт.')
        print('----------------------')

    """Вывод выданного оборудования"""
    def itemsOut(self):
        print(f'\nВыдано со склада:\n{self.__itemIn}')

"""Список техники"""
# Printer_ self, brand, model, color, paperType, price, printingType
# Monitor self, brand, model, color, width, price, resolution
# Scaner self, brand, model, color, paperType, price, resolution
models = [Printer('HP', 'Laserjet 610', 'Black', 'A4', 10500, 'Ink'),
          Printer('Xerox', 'Phazer 3241', 'White', 'A4', 6351, 'Laser',),
          Monitor('LG', '34GN850-B', 'Silver', '34', 72000, '3440x1440'),
          Scanner('Canon', 'imageFORMULA DR-G2140', 'Grey', 'A4', 1020000, '600x600 dpi')]

"""Вызывает метод проверки запасов на складе"""
storage = Storage()
storage.itemsInStock()

# printer = Monitor('HP', 'Laserjet 610', 'Black', 'A4', 10500, 'Ink')
# print(printer._brand)

while True:
    """Меню операций"""
    print('\nВведите тип операции:\n<1> Принять на склад.\n<2> Выдать со склада.\n<Enter> Выход.')
    action = input('> ')
    if action in ['1', '2']:  # если выбрана операция
        # формируем список оргтехники
        s = ''
        for i, eq in enumerate(models, 1):
            s += f'\n<{i}> {eq._brand} {eq._model} ({storage.num(i)} шт.)'

        """Меню оргтехники"""
        while True:
            print(f'\nВведите модель оргтехники и кол-во:{s}')
            # выбираем модель
            try:
                model = int(input('модель > '))
                if model in range(len(models) + 1):
                    # вводим кол-во
                    n = int(input('кол-во > '))
                    if (n <= 0):
                        raise ValueError
                else:
                    raise ValueError

            except ValueError:
                print(f'Некорректный ввод. Введите число от <0> до <{len(models)}>.')
                continue
            else:
                # совершаем операцию
                print('\nОперация:')
                if (action == '1'):  # принимаем технику на склад
                    print(f'Принято на склад {models[model - 1]._model} - {n} шт.')
                    storage.inputItems(model, n)
                elif (action == '2'):  # выдаём технику со склада
                    max = storage.num(model)
                    if (n > max):  # если запрошено больше, чем есть
                        n = max
                        print(f'Внимание: На складе всего {n} шт. {models[model - 1]._model}!')
                    print(f'Выдано со склада {models[model - 1]._model} - {n} шт.')
                    storage.outputItems(model, n)

                # выводим остатки по складу
                storage.itemsInStock()
                break

            if (input('\nPress <Enter> to continue or any key to exit...') != ''):
                break
    elif action == '':  # если выбран выход - завершаем работу
        break
    else:
        print('Некорректный ввод. Для выбора введите <1> или <2>.')


# Объект класса:
