# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
# этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.


numbDict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
}

with open('English_numb_in2.txt', 'r', encoding='utf-8') as usrFile:
    usrList = usrFile.readlines()
    count = 0
    for i in usrList:
        strKonv = i.rstrip('\n')
        listKonv = strKonv.split()
        translate = numbDict[listKonv[0].lower()]
        listKonv.pop(0)
        listKonv.insert(0, translate.title())
        strKonv = ' '.join(listKonv)
        if count > 0:
            ind = 'a'
        else:
            ind = 'w'

        with open('English_numb_out2.txt', ind, encoding='utf-8') as usrFileRu:
            print(strKonv, file=usrFileRu)
        count = 2
