# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def max_sum(fst, snd, trd):
    x = 0
    y = 0
    ls = [fst, snd, trd]
    for i in range(len(ls)):
        if x < ls[i]:
            x = ls[i]

    for k in ls:
        if y < k != x:
            y = k

    return x + y


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


a = input('Введите первое число a = ')
b = input('Введите второе число b = ')
c = input('Введите третье число c = ')

try:
    a = num(a)
    b = num(b)
    c = num(c)
    print(max_sum(a, b, c))
except ValueError:
    print('Неверный ввод: вводить можно только числа!')
