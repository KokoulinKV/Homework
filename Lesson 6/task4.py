# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Автомобиль поехал.')

    def stop(self):
        print('Автомобиль остановился.')

    def turn(self, direction):
        if direction == 'left':
            print('Автомобиль повернул налево.')
        elif direction == 'right':
            print('Автомобиль повернул направо.')
        else:
            print('Команда не распознана, автомобиль продолжает движение прямо.')

    def show_speed(self):
        print(f'Ваша скорость - {self.speed}.')




class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превышаете ограничение скорости в 60 км/ч! Ваша скорость - {self.speed}.')
        else:
            print(f'Ваша скорость - {self.speed}.')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превышаете ограничение скорости в 40 км/ч! Ваша скорость - {self.speed}.')
        else:
            print(f'Ваша скорость - {self.speed}.')


class PoliceCar(Car):
    pass


solaris = TownCar(65, 'grey', 'Hyundai Solaris')
ferrari = SportCar(120, 'red', 'Ferrari')
kamaz = WorkCar(38, 'orange', 'Kamaz')
granta = PoliceCar(80, 'white-blue', 'Lada Granta', True)

if solaris.is_police:
    print(f'{solaris.name} цвета {solaris.color} является полицейской машиной.')
else:
    print(f'{solaris.name} цвета {solaris.color}.')
solaris.go()
solaris.turn('right')
solaris.show_speed()
solaris.stop()
print()

if ferrari.is_police:
    print(f'{ferrari.name} цвета {ferrari.color} является полицейской машиной.')
else:
    print(f'{ferrari.name} цвета {ferrari.color}.')
ferrari.go()
ferrari.turn('left')
ferrari.show_speed()
ferrari.stop()
print()

if kamaz.is_police:
    print(f'{kamaz.name} цвета {kamaz.color} является полицейской машиной.')
else:
    print(f'{kamaz.name} цвета {kamaz.color}.')
kamaz.go()
kamaz.turn('right')
kamaz.show_speed()
kamaz.stop()
print()

if granta.is_police:
    print(f'{granta.name} цвета {granta.color} является полицейской машиной.')
else:
    print(f'{granta.name} цвета {granta.color}.')
granta.go()
granta.turn('left')
granta.show_speed()
granta.stop()

