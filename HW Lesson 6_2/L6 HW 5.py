# 5. Реализовать класс Stationery (канцелярская принадлежность).
# ● определить в нём атрибут title ( название) и метод draw ( отрисовка). Метод выводит
# сообщение «Запуск отрисовки»;
# ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ● в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;
# ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.


class Stationery:
    # атрибуты класса:
    title = 'Принадлежность для рисования'

    # методы класса:
    def draw(self):
        print(f'Отрисовка начата, при помощи {self.title}!')

class Pen(Stationery):

    # атрибуты класса:
    title = 'Шариковая ручка'

    # методы класса:
    def draw(self):
        print(f'Отрисовка начата, при помощи {self.title}!')

class Pencil(Stationery):

    # атрибуты класса:
    title = 'Карандаш'

       # методы класса:
    def draw(self):
        print(f'Отрисовка начата, при помощи {self.title}!')

class Handle(Stationery):
    pass
    # атрибуты класса:
    title = 'Маркер'

    def draw(self):
        print(f'Отрисовка начата, при помощи {self.title}!')

# Объект
bicPen = Pen()
bicPen.draw()
print()
attachPencil = Pencil()
attachPencil.draw()
print()
errdingHandle = Handle()
errdingHandle.draw()