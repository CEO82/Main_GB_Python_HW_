# 2. Создайте собственный класс-исключение,
#   Обрабатывающий ситуацию деления на ноль.
#   Проверьте его работу на данных, вводимых пользователем.
#   При вводе нуля в качестве  делителя программа должна корректно
#обработать эту ситуацию и не завершиться с ошибкой.

def division(x, y):
    res = x/y
    return res

class MyExeptions(Exception):

    # атрибуты класса:
    # Конструктор с атрибутами объекта:
    def __init__(self, txt):
        self.txt = txt
    # методы класса:

# Объект класса:

print('Attention operation Divsion!')

try:
    x = float(input('Enter number: '))
    y = float(input('Enter divisior argument: '))
    if y == 0:
        raise MyExeptions('Forbidden to use 0 as divisior argument')
    res = division(x, y)
    print(res)
except (ValueError, MyExeptions, ZeroDivisionError, NameError) as error:
    print(error)


