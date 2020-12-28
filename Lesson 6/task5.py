# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Начинаем рисовать ручкой.')


class Pencil(Stationery):
    def draw(self):
        print('Начинаем рисовать карандашем.')


class Handle(Stationery):
    def draw(self):
        print('Начинаем рисовать маркером.')


stationery = Stationery('Brush')
pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')

print(f'Берем в руки {stationery.title}')
stationery.draw()
print()

print(f'Берем в руки {pen.title}')
pen.draw()
print()

print(f'Берем в руки {pencil.title}')
pencil.draw()
print()

print(f'Берем в руки {handle.title}')
handle.draw()