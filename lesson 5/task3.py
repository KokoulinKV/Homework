# Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('task_3.txt', 'r', encoding='UTF-8') as file:
    data = file.readlines()

average = 0
staff = 0
count = 1
for i in range(len(data)):
    data[i] = data[i].replace('\n', '')
    data[i] = data[i].split(' ')
print('Список сотрудников с ЗП меньше 20000:')

for i in range(len(data)):
    data[i][1] = int(data[i][1])
    staff += 1
    average += data[i][1]
    if data[i][1] < 20000:
        print(f'{count}. {data[i][0]} имеет ЗП в размере {data[i][1]}')
        count += 1
print(f'Средняя ЗП сотрудников составляет: {(average / staff): .2f}')
