# 2) Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Реализовать вывод данных о
# пользователе одной строкой.

"""Данная функция для проверки число ли введенный символ?"""
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

"""Упаковка введенных данных в словарь и проверка года и тел №"""
def user_info_input(**kwargs):
    if isfloat(kwargs['birthYear']) == False or isfloat(kwargs['phone']) == False or len(kwargs['phone']) != 11 or len(kwargs['birthYear']) != 4:
        print('В полях год рождения и № телефона вы ввели не верные данные! \nПожалуйста повторите ввод, год содержит 4 цыфры, № телефона 11 цыфр')
        check = False
        return check
    print(f'Введены следующие данные пользователя: {kwargs}')


usrName = 'Введите ваше имя: '
usrSurName = 'Введите вашу фамилию: '
usrBirthYear = 'Введите год вашего рождения: '
usrSity = 'Введите город вашего проживания: '
usrEmail = 'Введите вашу эл. почту: '
usrPhone = 'Введите ваш № телефон, без знака + и скобок в формате 89********: '


while True:
    a = user_info_input(name=input(usrName), surName=input(usrSurName), birthYear=input(usrBirthYear), sity=input(usrSity), email=input(usrEmail), phone=input(usrPhone))
    if a == False:
        print('Повторный ввод')
        a = user_info_input(name=input(usrName), surName=input(usrSurName), birthYear=input(usrBirthYear), sity=input(usrSity), email=input(usrEmail), phone=input(usrPhone))
    else:
        break
print('Ввод данных успешно завершен!')