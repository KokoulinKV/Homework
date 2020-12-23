# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1, Two — 2, Three — 3, Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
translate = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
with open('task_4.txt', 'r', encoding='UTF-8') as file:
    data = file.readlines()

for k, v in translate.items():
    for i in range(len(data)):
        data[i] = data[i].replace(k, v)

with open('task_4_new.txt', 'w', encoding='UTF-8') as new_file:
    new_file.writelines(data)
