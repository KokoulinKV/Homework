# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, income=None):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position)
        self._income = income

    def get_full_name(self):
        print(f'{self.name} {self.surname} занимает должность: {self.position}.')

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        print(f'Доход сотрудника составил: {total_income}')


profit_lawyer = {
    "wage": 20000,
    "bonus": 5000
}

profit_judge = {
    "wage": 80000,
    "bonus": 15000
}

lawyer = Position('Jim', 'Jefferson', 'Юрист', profit_lawyer)
judge = Position('Kelvin', 'Smith', 'Судья', profit_judge)

lawyer.get_full_name()
lawyer.get_total_income()
judge.get_full_name()
judge.get_total_income()
