# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def check(num):
    if num.isdigit:
        num = int(num)
        return num
    else:
        num = float(num)
        return num


name = input('Введите имя файла, файл будет создан с разрешением .txt: ')
nums = input('Введите числа, которые хотите ввести в файл, через пробел: ')
data_list = []
try:
    name_file = name + '.txt'
    count = 0
    nums = nums.split()
    for i in range(len(nums)):
        if nums[i] != '':
            data_list.append(nums[i])

    for i in range(len(data_list)):
        data_list[i] = check(data_list[i])

    with open(name_file, 'w', encoding='UTF-8') as file:
        for i in range(len(data_list) - 1):
            data_list[i] = f'{data_list[i]}, '
            file.write(data_list[i])
        file.write(str(data_list[len(data_list) - 1]))

    with open(name_file, 'r', encoding='UTF-8') as file1:
        data = file1.read()
        data = data.split(', ')
        for i in range(len(data)):
            data[i] = check(data[i])
            count += data[i]
    print(f'Сумма введенных чисел составляет: {count}, а сами числа записаны в файл {name}')
except ValueError:
    print('Вводить можно только числа!')
