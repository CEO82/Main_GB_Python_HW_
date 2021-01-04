# 4. Реализуйте базовый класс Car .
# ● у класса должны быть следующие атрибуты: speed, color, name, i s_police ( булево). А
# также методы: go, stop, t urn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar , SportCar , WorkCar , PoliceCar ;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 ( TownCar) и 40 ( WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Вызовите методы и покажите результат.



class Car:
    # атрибуты класса:


    # Конструктор с атрибутами объекта:
    def __init__(self, speed , color, model, is_police):
        self.spd = speed
        self.col = color
        self.md = model
        self.plc = is_police


    # методы класса:
    def show_speed(self):
        print(f'Ваша скорость {self.spd} км/ч')

    def go(self):
        if self.plc == False:
            print(f'Автомобиль {self.md} в движении')
        else:
            print(f'Автомобиль {self.md} в движении! Спец сигналы включены!')

    def stop(self):
        if self.plc == False:
            print(f'Автомобиль {self.md} в остановился')
        else:
            print(f'Автомобиль {self.md} в остановился! Спец сигналы выключены! Погоня завершена!')

    def turn(self):
        print('Через 300 метров перверните на право')


# Объект

class TownCar(Car):

    # атрибуты класса:

    # Конструктор с атрибутами объекта:

    # методы класса:
    def show_speed(self):
        if float(self.spd) > 60:
            print(f'Вы превысили скрость на {float(self.spd) - 60} км/ч! Снизте скорости до 60 км/ч!')
        else:
            print(f'Ваша скорость {self.spd} км/ч')


# Объект

class SportCar(Car):
    pass

# атрибуты класса:

# Конструктор с атрибутами объекта:

# методы класса:

# Объект

class WorkCar(Car):
    # pass

# атрибуты класса:

# Конструктор с атрибутами объекта:

# методы класса:
    def show_speed(self):
        if float(self.spd) > 40:
            print(f'Вы превысили скрость на {float(self.spd) - 40} км/ч! Снизте скорости до 40 км/ч!')
        else:
            print(f'Ваша скорость {self.spd} км/ч')

# Объект

class PoliceCar(Car):
    pass

# атрибуты класса:

# Конструктор с атрибутами объекта:

# методы класса:

# Объект
dodgeViper = SportCar(280, 'Black', 'Viper', False)
dodgeViper.go()
dodgeViper.show_speed()
dodgeViper.turn()
dodgeViper.stop()
print()
solaris = TownCar(100, 'Silver', 'Solaris', False)
solaris.go()
solaris.show_speed()
solaris.turn()
solaris.stop()
print()

vwTransporter = WorkCar(60, 'White', 'Transporter_T_6', False)
vwTransporter.go()
vwTransporter.show_speed()
vwTransporter.turn()
vwTransporter.stop()
print()

crownVictoria = PoliceCar(300, 'Black_and_White', 'CrownVictoria', True)
crownVictoria.go()
crownVictoria.show_speed()
crownVictoria.turn()
crownVictoria.stop()
print()
