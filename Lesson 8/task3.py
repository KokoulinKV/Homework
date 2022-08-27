# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
# соответствующее сообщение. При этом работа скрипта не должна завершаться.

class NoNumberException(Exception):
    def __init__(self, txt):
        self.txt = txt


def is_num(num):
    if num.isdigit():
        return int(num)
    elif str(num):
        if num == 'stop' or num == 'STOP':
            return False
        else:
            raise NoNumberException('Введенный элемент не является числом!')
    else:
        return float(num)


print('Если Вы захотите завершить программу, то введите "STOP" вместо очередного элемента списка.')
ls = []
while True:
    new_el = input('Введите число для внесения в список: ')
    try:
        new_el = is_num(new_el)
        if not new_el:
            break
        else:
            ls.append(new_el)

    except NoNumberException as e:
        print(e)
print(f'Получившийся список: {ls}')
