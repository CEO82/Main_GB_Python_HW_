#6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 %
# относительно предыдущего. Требуется определить номер дня,
# на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b
# и выводить одно натуральное число — номер дня.
#Например: a = 2, b = 3.
#Результат:
#1-й день: 2
#2-й день: 2,2
#3-й день: 2,42
#4-й день: 2,66
#5-й день: 2,93
#6-й день: 3,22

#Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

print('Добро пожаловать в программу по расчету продолжительности бега')
while True:
    firstDist = int(input('Введите начальное расстояние дистанции которое вы пробежите, в колометрах: '))
    aimDist = int(input('Введите вашу целевую дистанцию в км: '))
    if aimDist > firstDist:
        a = firstDist
        count = 1
        while a < aimDist:
            a = a*1.1
            count += 1
        print(f'На {count}-й день вы пробежите более {a:.2f} километров')
        break
    else:
        print('Вы ввели вашу целевую дистанцию меньше стартовой, пожалуйста задайте целевую дистанцию больше стартовой')

