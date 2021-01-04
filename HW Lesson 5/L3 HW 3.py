# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
# сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
# emp_salary_romashka
# new_text_file

with open('emp_salary_romashka2.txt', 'r', encoding='utf-8') as usrFile:
    usrLines = usrFile.readlines()

count = 0
salaryGros = []
konvDict = {}
loosers = []
for i in usrLines:
    if i[0:1].isalpha() == True or i[0:1] != '\n':
        strKonv = i.rstrip('\n')
        strKonv = strKonv.split()
        salaryGros.append(float(strKonv[1]))
        if float(strKonv[1]) < 20000:
            loosers.append(strKonv[0])

averSalary = sum(salaryGros) / len(salaryGros)
print(f'Средняя заработанная плата сотрудников в фирме составляет:{averSalary: .2f} рублей')
print(f'Сотрудники с зароботной платой менее 20000 рубелй:')
for i in loosers:
    print(i)