#1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

hero = input('Введите имя вашего любимого героя: ')

numb = int(input('Введите ваше любимое число: '))
numb = numb ** 3

print(f'Ваш любимый герой {hero} и возможно ему нравится число {numb}')