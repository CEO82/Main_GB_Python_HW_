# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
# её на экран.


import random
from functools import reduce

genList = [f'{round(random.random() * n)}' for n in range(1,100)]
genStr = ' '.join(genList)

with open('Rnd_numb_out1.txt', 'w', encoding='utf-8') as usrFileNumb:
    usrFileNumb.writelines(genStr)

with open('Rnd_numb_out1.txt', 'r', encoding='utf-8') as usrFileNumbKonv:
    fileContent = usrFileNumbKonv.readline()
    fileList = fileContent.split()
    sumary = reduce(lambda x,y: int(x) + int(y), fileList)

print(sumary)
print(genList)

