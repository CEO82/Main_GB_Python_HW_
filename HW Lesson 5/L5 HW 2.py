# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.

# For Teacher: Подсчитывал только заполненные строки в файле, т.к. другого не указано в задании.



with open('new_text_file.txt', 'r', encoding='utf-8') as usrFile:
    content = usrFile.read()
    usrFile.seek(0)
    lines = usrFile.readlines()

newList = []
for num, i in enumerate(lines, 1):
    strKonv = i.rstrip('\n')
    strKonv = strKonv.split()
    print(f'В {num}-й строке {len(strKonv)} слов ')
    newList.append(strKonv)

strCount = content.count('\n')
print(f'Всего в файле {strCount} заполненных строк')
print(lines)
