# 1. Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка.


usrStr = ''
count = 0
while True:
    usrStr = input('Введите ваш тектс, или число. Если вы хотите выйти просто нажмите "Enter": ')
    if not usrStr:
        break
    else:
        if count > 0:
            ind = 'a'
        else:
            ind = 'w'
        with open('new_text_file.txt', ind, encoding='utf-8') as usrFile:
            print(usrStr, file=usrFile)
    count = 2
