# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 0:
            self.__size = 0
        elif size > 60:
            self.__size = 60
        else:
            self.__size = size

    def consumption(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, h):
        self.height = h

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 0:
            self.__height = 0
        elif height > 2:
            self.__height = 2
        else:
            self.__height = height

    def consumption(self):
        return 2 * self.height + 0.3


coat = Coat(50)
print(f'Расход ткани на пальто размера {coat.size} составляет: {coat.consumption()}')

costume = Costume(1.8)
print(f'Расход ткани на костюм на рост {costume.height} составляет: {costume.consumption()}')

full_consumption = f'Общий расход ткани составил: {coat.consumption() + costume.consumption()}'
print(full_consumption)
