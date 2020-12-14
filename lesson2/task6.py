# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
try:
    num_goods = int(input('Введите количество товаров, которое хотите внести в базу: '))
    if num_goods > 0:
        analytics = {}
        ls_tuple = []

        for i in range(num_goods):
            d = {}
            d['название'] = input(f'Введите название товара №{i + 1}: ')
            d['цена'] = int(input(f'Введите цену товара №{i + 1} в виде числа: '))
            if d.get('цена') < 0:
                raise ValueError
            d['количество'] = int(input(f'Введите количество товара №{i + 1} в виде числа: '))
            if d.get('количество') < 0:
                raise ValueError
            d['eд'] = input(f'Введите в чем измеряется количество товара №{i + 1} (ед.изм.): ')
            ls_tuple.append((i + 1, d))

        for el in ls_tuple:
            for k, v in el[1].items():
                if k in analytics:
                    if v not in analytics.get(k):
                        analytics[k].append(v)
                else:
                    analytics[k] = [v]
        print('Проведя аналитику товаров, получем: ')
        for v, k in analytics.items():
            print(f'{v} : {k}')
    elif num_goods == 0:
        print('Вы ввели 0, а значит не захотели добавлять товары.')
    else:
        print('Количество товаров не может быть отрицательным числом!')
except ValueError:
    print('Количество товаров, цена и количество определенного товара задается натуральным числом!')
