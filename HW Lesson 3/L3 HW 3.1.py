#3) Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.
#

# For Teacher. Решение было подсмотренно) Но я об этом не просил))))

def my_func(my_list):
    my_list.remove(min(my_list))
    return sum(my_list)

num_1 = int(input('a = '))
num_2 = int(input('b = '))
num_3 = int(input('c = '))

print(f'Сумма наибольших двух аргументов равна: {my_func([num_1, num_2, num_3])}')