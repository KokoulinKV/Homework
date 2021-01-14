# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class MyZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


def is_num(num):
    if num.isdigit():
        return int(num)
    else:
        return float(num)


dividend = input('Введите делимое: ')
divider = input('Введите делитель: ')

try:
    if is_num(divider) == 0:
        raise MyZeroDivision('Нельзя делить на нуль!!!')
    result = is_num(dividend) / is_num(divider)
    print(f'Частное равно: {result}')
except MyZeroDivision as e:
    print(e)
