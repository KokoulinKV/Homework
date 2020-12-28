# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        last_light = 'red'
        counter = 0
        while counter < 8:
            if self.__color == 'red':
                print('Включен красный сигнал светафора на 7 секунд.')
                self.__color = 'yellow'
                last_light = 'red'
            elif self.__color == 'yellow':
                print('Включен желтый сигнал светафора на 2 секунд.')
                if last_light == 'red':
                    self.__color = 'green'
                else:
                    self.__color = 'red'
            elif self.__color == 'green':
                print('Включен зеленый сигнал светафора на 20 секунд.')
                self.__color = 'yellow'
                last_light = 'green'
            else:
                break

            counter += 1


traffic_light = TrafficLight('green')
traffic_light.running()
