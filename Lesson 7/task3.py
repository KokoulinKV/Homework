# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме
# ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count).count

    def __sub__(self, other):
        if self.count - other.count > 0:
            return Cell(self.count - other.count).count
        else:
            return 'Первая клетка меньше второй! Вычитание невозможно!'

    def __mul__(self, other):
        return Cell(self.count * other.count).count

    def __truediv__(self, other):
        return Cell(self.count // other.count).count

    def make_order(self, in_row):
        ls = []
        i = 0
        left = self.count
        while True:
            if i < self.count:
                if left > in_row:
                    ls.append('*' * in_row)
                else:
                    ls.append('*' * left)
                    break
            else:
                break
            i += in_row
            left -= in_row
        return '\n'.join(ls)


c1 = Cell(55)
c2 = Cell(30)
print(c1 + c2)
print(c1 - c2)
print(c2 - c1)
print(c1 * c2)
print(c1 / c2)

print(c1.make_order(10))