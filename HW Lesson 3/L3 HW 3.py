# 3) Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.

# For Taecher. Т.к. в условии не сказано что аргументы должны быть числами,
# выполнил задание так что программа выполняет конкатинацию (суммирование строк)
# в 17:29 21.12.2020 задал вопрос куратору допустимо ли это.


def my_func(a, b, c):
    listDef = []
    listDef.append(a)
    listDef.append(b)
    listDef.append(c)
    print(listDef)
    mx = max(listDef)
    listDef.remove(mx)
    mx2 = max(listDef)
    return mx + mx2


usrMax = my_func(input('Введите элемент a: '), input('Введите элемент b: '), input('Введите элемент c: '),)
print(usrMax)
