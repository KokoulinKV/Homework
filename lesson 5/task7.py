# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
import json

firms = {}

with open('task_7.txt', 'r', encoding='UTF-8') as file:
    data = file.readlines()
for i in range(len(data)):
    data[i] = data[i].replace('\n', '')
    data[i] = data[i].split()
    firms[data[i][0]] = int(data[i][2]) - int(data[i][3])

average = 0
count = 0
exit_list = []
average_dict = {}
for k, v in firms.items():
    if firms[k] > 0:
        average += firms[k]
        count += 1
average_dict['average_profit'] = average / count
exit_list.append(firms)
exit_list.append(average_dict)
print(exit_list)

with open('firms.json', 'w', encoding='UTF-8') as file_ex:
    json.dump(exit_list, file_ex)
