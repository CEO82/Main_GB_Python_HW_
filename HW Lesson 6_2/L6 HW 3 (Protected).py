# 3. Реализовать базовый класс Worker (работник).
# ● определить атрибуты: name , surname , position (должность), income (доход);
# ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# ● создать класс Position (должность) на базе класса Worker ;
# ● в классе Position реализовать методы получения полного имени сотрудника
# ( get_full_name ) и дохода с учётом премии ( get_total_income );
# ● проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.


class Worker:
    # атрибуты класса:


    # Конструктор с атрибутами объекта:
    def __init__(self, name , surname , position, salary, bonus):
        self.nam = name
        self.sur = surname
        self.pos = position
        self._inc = {'wage': float(salary), 'bonus': float(bonus)}

    # методы класса:
    # def get_full_name(self):
    #     fulName = self.nam + ' ' + self.sur
    #     print(f'Имя и Фамилия сторудника: {fulName}')
    #
    # def get_total_income(self):
    #     salary = self._inc['wage'] + self._inc['bonus']
    #     print(f'Полный доход сотрудника составляет {salary} рублей')

    # Объект класса:

class Position(Worker):
    # атрибуты класса:


    # методы класса:
    def get_full_name(self):
        fulName = self.nam + ' ' + self.sur
        print(f'Имя и Фамилия сторудника: {fulName}')

    def get_total_income(self):
        salary = self._inc['wage'] + self._inc['bonus']
        print(f'Полный доход сотрудника составляет {salary} рублей')


# Объект класса:
worker1 = Position(input('Введите имя: '), input('Введите фамилию: '), input('Введите должность: '), input('Введите оклад в рублях: '), input('Введите размер бонуса в рублях: '),)
worker1.get_full_name()
worker1.get_total_income()
