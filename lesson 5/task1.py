# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

name = input('Введите имя файла, файл будет создан с разрешением .txt: ')
num_of_strings = input('Введите количество строк, которые хотите ввести в файл: ')
data_list = []
try:
    num_of_strings = int(num_of_strings)
    if num_of_strings >= 0:
        for i in range(num_of_strings):
            input_string = input(f'Введите данные, которые хотите записать в {i + 1} строку файла: ')
            data_list.append(input_string + '\n')

        with open(name + '.txt', 'w', encoding='UTF-8') as file:
            file.writelines(data_list)

        if num_of_strings == 0:
            print('Вы создали пустой файл!')
    else:
        raise ValueError

except ValueError:
    print('Вводить можно только целые положительные числа!')
