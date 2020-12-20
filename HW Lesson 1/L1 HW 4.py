#4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
while True:
    usrNumb = int(input('Введите любое положительное число: '))
    if usrNumb > 0:
        z = 0
        while usrNumb >= 1:

            a = usrNumb % 10
            usrNumb = usrNumb // 10
            if a > z:
                z = a
            else:
                z = z

        print(z)
        print(usrNumb)
        break
    else:
        print('Вы ввели число меньше 1, пожалуйста введите положительное число больше 1')