#2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

#elcount = input('Введите колличество элементов в списке')

usrList = []
n = 1
while True:
    qest1 = input('Если вы хотите добавить элемент списка введите: д - да, \nесли вы хотите завершить ввод данных нажмите н - нет \nваш выбор: ')
    if qest1 == 'д':
        c = input('Введите элемент списка: ')
        usrList.append(c)
        print(f'Вы ввели {n} элементов списка')
        n += 1

    elif qest1 == 'н':
        print('no')
        break
    else:
        print('Не верный ввод')

print(usrList)
#usrList = [1, 'in', True, 3.5, [55, 'out'], 'Om', 'Shanti', 'goods', 'perfekt']
for i in range(1, len(usrList), 2):
    a = usrList[i - 1]
    b = usrList[i]
    usrList.pop(i - 1)
    usrList.insert(i - 1, b)
    usrList.pop(i)
    usrList.insert(i, a)
print(usrList)
