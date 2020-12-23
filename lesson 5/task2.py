# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('task_2.txt', 'r', encoding='UTF-8') as file:
    data = file.readlines()

for i in range(len(data)):
    data[i] = data[i].replace('\n', '')
num_of_str = len(data)
print(f'Кол-во строк в файле: {num_of_str}')

for k in range(len(data)):
    num_of_words = len(data[k].split(' '))
    print(f'В строке {k + 1} всего слов: {num_of_words}')
