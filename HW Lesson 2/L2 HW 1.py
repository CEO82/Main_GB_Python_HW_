#1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

dataList = [1, 3.5, ['in', 'out'], {'age': 38, 'sex': 'male'}, (1, 2, 3, 'Hadgehog'), 'Rabbit', None, True, False]
print(dataList[4])
position = 0
for elemType in dataList:
    print(f'В позиции {position} тип данных = {type(elemType)}')
    position += 1
print(len(dataList))

