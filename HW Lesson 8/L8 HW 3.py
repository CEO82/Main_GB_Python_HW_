# 3. Создайте собственный класс-исключение,
#   Который должен проверять содержимое списка на наличие только чисел.
#   Проверить работу исключения на реальном примере. Запрашивать у
# пользователя данные и заполнять список необходимо только числами. Класс-исключение
# должен контролировать типы данных элементов списка.
#   Примечание: длина списка не фиксирована.
#   Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
# введя, например, команду «stop». При этом скрипт завершается, сформированный список с
# числами выводится на экран.
#   Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа
# элемента. Вносить его в список, только если введено число. Класс-исключение должен не
# позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

class MyExeptions(Exception):

    # атрибуты класса:
    # Конструктор с атрибутами объекта:
    def __init__(self, txt):
        self.txt = txt
    # методы класса:

# Объект класса:
usrList = []
while True:
    usrNumb = input(f'If you want to Exit enter only symbol ~ \nPlease enter a any Number, just Nubmers: \n')
    if usrNumb == '~':
        break
    try:
        if isfloat(usrNumb) == False:
            raise MyExeptions('Not allowed argument,\nplease enter only nubers\n')

    except (ValueError, MyExeptions, ZeroDivisionError, NameError) as error:
        print(error)
    else:
        usrList.append(float(usrNumb))

print(f'Filtred list of arguments:\n{usrList}')