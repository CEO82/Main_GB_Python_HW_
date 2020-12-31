# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
# учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
# были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по
# нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

from functools import reduce

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


academicLesVal = {}

with open('Academic_Lessons.txt', 'r', encoding='utf-8') as usrFileAcademic:
    fileContent = usrFileAcademic.readlines()
    for fileList in fileContent:
        listKonvert = fileList.split()
        summaryList = []
        for str in listKonvert:
            numb = ''
            for symb in str:
                if isfloat(symb) == True:
                    numb = numb + symb
            summaryList.append(numb)
        genSum =[n for n in summaryList if isfloat(n) == True]
        summaryEnd = reduce(lambda x,y: int(x) + int(y), genSum)
        academicLesVal[fileList[0:fileList.find(':')]] = int(summaryEnd)

        print(academicLesVal)
