# 6) Реализовать функцию i nt_func(), принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) ->
# Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать
# вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
# использовать написанную ранее функцию int_func() .

testStr = 'mama Rama мыла Раmu miloM utrom 1515 utr155'


def text_konverter(usrStr):
    usrList = usrStr.split()
    konvertedList = []
    for word in usrList:
        count = 0
        for simbol in word:
            lenth = len(word)
            if 97 <= ord(simbol) <= 122:
                count += 1
        if lenth == count:
            word = word.title()
            konvertedList.append(word)
    print(konvertedList)
    konvertedStr = ' '.join(konvertedList)
    print(konvertedStr)







a = text_konverter(testStr)