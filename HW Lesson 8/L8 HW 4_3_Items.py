
    # атрибуты класса:
    # Конструктор с атрибутами объекта:
    # методы класса:
# Объект класса:


class ElectronicsGoods:
    pass
    # атрибуты класса:
    # Конструктор с атрибутами объекта:
    # def __init__(self):
    #     self.br = brand
    #     self.md = model
    #     self.clr = color
    #     self.prtM = printMethod

    # методы класса:
# Объект класса:

class Printers(ElectronicsGoods):
    pass
    # атрибуты класса:
    itmType = 'Printer'
    forInput = ['Введите производителя принтера: ', 'Введите модель принтера: ', 'Введите цвет принтера: ',
            'Введите тип печати: ', 'Введите колличество единиц техники: ']
    # Конструктор с атрибутами объекта:

    # методы класса:
    """Метод формирует список для отправки на хранение (по средствам ввода)"""
    def makePrinterList(self):
        pass
        prtList = [input(i) for i in Printers.forInput[0: len(Printers.forInput) - 1]]
        while True:
            try:
                inputTry = int(input(Printers.forInput[-1]))

                while True:
                    if inputTry < 0:
                        print('Вы ввели отрицательное число! Повторите ввод!\nВведите целое положительное число')
                        inputTry = int(input(Printers.forInput[-1]))
                    else:
                        break
                prtList.append(inputTry)
                break
            except ValueError as error:
                print(error)
                print('Вы ввели не число! Повторите ввод!')


        prtList.insert(0, Printers.itmType)

        return prtList

# Объект класса:


# class Scaners(ElectronicsGoods):
#     pass
#     # атрибуты класса:
#     itmType = 'Scaner'
#     forInput = ['Введите производителя сканера: ', 'Введите модель сканера: ', 'Введите цвет сканера: ',
#                 'Введите колличество единиц техники: ']
#     # Конструктор с атрибутами объекта:
#
#     # методы класса:
#     """Метод формирует список для отправки на хранение (по средствам ввода)"""
#
#     def makeScanerList(self):
#         pass
#         scnList = [input(i) for i in Scaners.forInput[0: len(Scaners.forInput) - 1]]
#         while True:
#             try:
#                 scnList.append(int(input(Scaners.forInput[-1])))
#                 break
#             except ValueError as error:
#                 print(error)
#                 print('Вы ввели не число! Повторите ввод!')
#
#         scnList.insert(0, Scaners.itmType)
#
#         return scnList
    # Конструктор с атрибутами объекта:
    # методы класса:
# Объект класса:

"""Активизация ввода подклассов Изделий/Товаров"""
somePrtInput = Printers()
# someScnrInput = Scaners()

print(somePrtInput.makePrinterList())
# print(someScnrInput.makeScanerList())