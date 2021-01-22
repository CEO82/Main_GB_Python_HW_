somePrtList = ['Printer', 'HP', 'Color Jet 3000', 'Black', 'Laser', 23]

    # атрибуты класса:
    # Конструктор с атрибутами объекта:
    # методы класса:
# Объект класса:

class ElectronicsWarehouse:
    pass
    # атрибуты класса:
    locationsKeys = ['warehouse', 'contractors', 'internalDept']
    itemKeys = ['Printer', 'Scaner']
    dictWarehose = {}

    # Конструктор с атрибутами объекта:
    def __init__(self, itmList):
        self.itmList = itmList
    # методы класса:
    """Метод формирования словаря изделий на складе"""
    def warehoseDict(self):
        choise = int(input('Введите куда требуется распределить товар:\n'
                       'На склад хранения, введите 1\n'
                       'На выдачу заказчику введите 2\n'
                       'На выдачу внутреннему подразделению введите 3\n'
                       'ваш ввод: '))
        while True:
            if choise == 1 or choise == 2 or choise == 3:
                print('yes')
                break

            else:
                print('Не верный выбор!')
                choise = int(input('Введите куда требуется распределить товар:\n'
                                   'На склад хранения, введите 1\n'
                                   'На выдачу заказчику введите 2\n'
                                   'На выдачу внутреннему подразделению введите 3\n'
                                   'ваш ввод: '))
        if choise == 1:



        ElectronicsWarehouse.dictWarehose[self.itmList[0]] = self.itmList[1:]
        return ElectronicsWarehouse.dictWarehose



        """Метод показывает наличие изделий"""
    def ShowItems(self):
        pass




# Объект класса:

someAction = ElectronicsWarehouse(somePrtList)
print(someAction.warehoseDict())




