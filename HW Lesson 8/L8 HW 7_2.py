# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров. Проверьте корректность
# полученного результата.


class ComplexNumbers:
    pass
    # атрибуты класса:
    # Конструктор с атрибутами объекта:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # методы класса:
    def __add__(self, other):
        return f'Результат сложения комплексного числа: ({(self.x + other.x)} + {(self.y + other.y)}j)\n'

    def __mul__(self, other):
        return f'Результат умножения комплексного числа: ({(self.x * other.x) - (self.y * other.y)} + {(self.y * other.x) + (self.x * other.y)}j)\n'

# Объект класса:

xC = ComplexNumbers(10, 8)
yC = ComplexNumbers(7, 10)

print(xC + yC)
print(xC * yC)
