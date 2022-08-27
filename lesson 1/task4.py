# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num = input('Введите положительное целое число: ')
max_num = 0
i = 0
len_num = len(num)

while True:
    if i == len_num:
        print(max_num)
        break
    if max_num < int(num[i]):
        max_num = int(num[i])
    i += 1
