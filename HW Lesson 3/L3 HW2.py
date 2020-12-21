# 2) Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Реализовать вывод данных о
# пользователе одной строкой.

def user_info_input(**kwargs):
    print(kwargs)

usrName = 'Введите ваше имя: '
usrSurName = 'Введите вашу фамилию: '
usrBirthYear = 'Введите год вашего рождения: '
usrSity = 'Введите город вашего проживания: '
usrEmail = 'Введите вашу элю почту: '
usrPhone = 'Введите ваш № телефон, без знака + и скобок в формате 89********: '

questUserInfo = []


user_info_input(name = input(usrName), surName = input(usrSurName), birthYear = input(usrBirthYear), sity = input(usrSity), email = input(usrEmail), phone = input(usrPhone))