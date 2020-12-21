#2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

sec = int(input('Введите колличество секунд: '))
hour = sec // 3600
minutes = (sec - (hour * 3600)) // 60
seconds = sec - (hour * 3600) - minutes * 60
seconds2 = sec % 60
print(f'{hour:02}:{minutes:02}:{seconds:02}')
print(seconds2)

