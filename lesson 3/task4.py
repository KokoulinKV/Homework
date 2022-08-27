# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def num(z):
    if z.isdigit():
        z = int(z)
        return z
    else:
        try:
            z = float(z)
            return z
        except ValueError:
            raise ValueError


def my_func(fst, snd):
    return fst ** snd


def my_func1(fst, snd):
    res = fst
    snd = abs(snd)
    for k in range(snd - 1):
        res = fst * res
    res = 1 / res
    return res


x = input('Введите действительное число x: ')
y = input('Введите целое отрицательное число y: ')
try:
    x = num(x)
    y = int(y)
    if y >= 0:
        raise ValueError
    print('Возведение числа "x" в степень "y" производится двумя способами:')
    print(f'С использованием оператора ** :{my_func(x, y)}')
    print(f'С использованием цикла, без оператора **: {my_func1(x,y)}')
except ValueError:
    print('Неверный ввод: "x" - должен быть действительным числом, а "y" - отрицательным целым!')
