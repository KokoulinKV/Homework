# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_div(x, y):
    return x / y


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


print('Для нахождения частного двух чисел введите: ')
a = input('Делимое а = ')
b = input('Делитель b = ')
try:
    a = num(a)
    b = num(b)
    res = my_div(a, b)
    print(res)
except ZeroDivisionError:
    print('Неверный ввод: на нуль делить нельзя!')
except ValueError:
    print('Неверный ввод: вводить можно только числа!')
