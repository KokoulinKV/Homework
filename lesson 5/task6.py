# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.


with open('task_6.txt', 'r', encoding='UTF-8') as file:
    data = file.readlines()

subjects = {}
for i in range(len(data)):
    data[i] = data[i].replace('\n', '')
    data[i] = data[i].split(': ')
    subjects[data[i][0]] = data[i][1]

for k, v in subjects.items():
    hours = 0
    subjects[k] = subjects[k].replace('(л)', '')
    subjects[k] = subjects[k].replace('(пр)', '')
    subjects[k] = subjects[k].replace('(лаб)', '')
    subjects[k] = subjects[k].split()
    for nums in range(len(subjects.get(k))):
        if subjects.get(k)[nums].isdigit():
            hours += int(subjects.get(k)[nums])
    subjects[k] = hours

print(subjects)
