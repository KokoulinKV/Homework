# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Storage:
    catalog = {
        'Printer': None,
        'Scanner': None,
        'Xerox': None
    }

    def reception(self, equip):
        key_catalog = equip.__class__.__name__
        if Storage.catalog[key_catalog] == None:
            Storage.catalog[key_catalog] = equip.equipment
        else:
            Storage.catalog[key_catalog] = Storage.catalog[key_catalog], \
                                           equip.equipment
        return Storage.catalog

    def transfering(self, type_equip, name, quantity):
        result = 0
        for keys, val in Storage.catalog.items():
            if keys == type_equip:
                for el in val:
                    if el['name'] == name:
                        result += 1
                        if int(el['quantity']) - quantity < 0:
                            return f'Столько {type_equip} марки {name} нет на складе!'
                        else:
                            el['quantity'] = int(el['quantity']) - quantity
                            return f'Склад покинуло {quantity} {type_equip} марки {name}'
        if result == 0:
            return f'{type_equip} марки {name} нет на складе!'


class OfficeEquipment:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Printer(OfficeEquipment):
    def __init__(self, name, quantity, is_color=True):
        super().__init__(name, quantity)
        self.is_color = is_color
        self.equipment = {'name': name, 'quantity': quantity, 'is_color': is_color}

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity.isdigit():
            self.__quantity = int(quantity)
        else:
            raise ValueError

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name.isdigit():
            self.__name = name
        else:
            raise ValueError

    @property
    def is_color(self):
        return self.__is_color

    @is_color.setter
    def is_color(self, is_color):
        if bool(is_color):
            self.__is_color = is_color
        else:
            raise ValueError


class Scanner(OfficeEquipment):
    def __init__(self, name, quantity, with_flash=True):
        super().__init__(name, quantity)
        self.with_flash = with_flash
        self.equipment = {'name': name, 'quantity': quantity, 'with_flash': with_flash}

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity.isdigit():
            self.__quantity = int(quantity)
        else:
            raise ValueError

class Xerox(OfficeEquipment):
    def __init__(self, name, quantity, productivity):
        super().__init__(name, quantity)
        self.productivity = productivity
        self.equipment = {'name': name, 'quantity': quantity, 'productivity': productivity}

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity.isdigit():
            self.__quantity = int(quantity)
        else:
            raise ValueError


try:
    store = Storage()
    printers1 = Printer('Cannon', '24', 'False')
    store.reception(printers1)
    printers2 = Printer('hp', '12')
    store.reception(printers2)
    store.transfering('Printer', 'Cannon', 14)
    scanners = Scanner('hp', '21')
    store.reception(scanners)
    xeroxes = Xerox('Xerox', '4', 'high')
    store.reception(xeroxes)
    print(store.catalog)
except ValueError:
    print('Неверно введены данные!')