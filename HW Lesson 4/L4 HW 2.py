# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

testList = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 100, 78, 85, 55, 77,123, 433, 2, 5, 54]
"""Решение с циклом"""
konvertedList = []
for n in range(0,len(testList) - 1):
    if float(testList[n + 1]) > float(testList[n]):
        konvertedList.append(testList[n+1])
resault = konvertedList
print(resault)

"""Решение с генератором"""
generList = [testList[n + 1] for n in range(0,len(testList) - 1) if float(testList[n + 1]) > float(testList[n])]
print(generList)