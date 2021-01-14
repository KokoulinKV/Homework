# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def convert_to_num(cls, date):
        result = []
        for el in date.split('-'):
            result.append(int(el))
        return result

    @staticmethod
    def validation(date):
        check_list = []
        for el in date.split('-'):
            check_list.append(int(el))
        if check_list[0] in range(1, 32):
            if check_list[1] in range(1, 13):
                if check_list[2] in range(0, 2021):
                    return 'Validation successful'
                else:
                    return 'Year validation unsuccessful'
            else:
                return 'Month validation unsuccessful'
        else:
            return 'Day validation unsuccessful'


birth_date = Date('11-02-1995')
print(Date.convert_to_num('11-02-1995'))
print(Date.validation('11-02-1995'))
