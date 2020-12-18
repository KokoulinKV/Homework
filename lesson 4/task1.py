# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, work_time, per_hour, bonus = argv


def check(num):
    if num.isdigit():
        num = int(num)
        if num >= 0:
            return num

    else:
        num = float(num)
        if num >= 0:
            return num


try:
    salary = (check(work_time) * check(per_hour)) + check(bonus)
    print(
        f'Заработная плата сотрудника за {work_time} часов, при ставке в час {per_hour} и премии в размере {bonus}, составляет: {salary}')

except ValueError:
    print('Введите выроботку в часах, ставку в час и премию в виде чисел.')
except TypeError:
    print('Значение не может быть меньше 0!')
