#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

monthDict = {1: 'Январь',
             2: 'Февраль',
             3: 'Март',
             4: 'Апрель',
             5: 'Май',
             6: 'Июнь',
             7: 'Июль',
             8: 'Август',
             9: 'Сентябрь',
             10: 'Октябрь',
             11: 'Ноябрь',
             12: 'Декабрь',
             }
yearTimesDict = {'Январь': 'Зимнй',
             'Февраль': 'Зимнй',
             'Март': 'Весенний',
             'Апрель': 'Весенний',
             'Май': 'Весенний',
             'Июнь': 'Летний',
             'Июль': 'Летний',
             'Август': 'Летний',
             'Сентябрь': 'Осенний',
             'Октябрь': 'Осенний',
             'Ноябрь': 'Осенний',
             'Декабрь': 'Зимний',
             }

monthList = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
yearTimesList = ['Зима', 'Весна', 'Лето', 'Осень']
usrMonth = input('Введите номер календарного месяца от 1 до 12: ')
usrMonth.isdigit()
print(usrMonth.isdigit())
while usrMonth.isdigit() == False or 1 > int(usrMonth) or int(usrMonth) > 12:
    print('Вы ввели не правильное число, попробуйте еще раз')
    usrMonth = input('Введите номер календарного месяца от 1 до 12: ')
usrMonth = int(usrMonth)
print(' ')
print(f'Вы выбрали {monthDict[usrMonth]} это {yearTimesDict[monthDict[usrMonth]]} месяц')
print(' ')
if 3 <= usrMonth <= 5:
    season = yearTimesList[1]
elif 6 <= usrMonth <= 8:
    season = yearTimesList[2]
elif 6 <= usrMonth <= 8:
    season = yearTimesList[3]
else:
    season = yearTimesList[0]

print(f'{season} это время года для месяца {monthList[usrMonth - 1]}')


# Вариант учителя через if in
# if usrMonth in monthDict:
#     print(...)
