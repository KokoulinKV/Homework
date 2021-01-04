# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        exit_ls = []
        for i in range(len(self.matrix)):
            local_ls = []
            for j in range(len(self.matrix[i])):
                local_ls.append(str(self.matrix[i][j]))
            exit_ls.append('  '.join(local_ls))
        return '\n'.join(exit_ls)

    def __add__(self, other):
        new_matrix = []
        try:
            for i in range(len(self.matrix)):
                local_matrix = []
                for j in range(len(self.matrix)):
                    local_matrix.append(self.matrix[i][j] + other.matrix[i][j])
                new_matrix.append(local_matrix)
            return Matrix(new_matrix)
        except IndexError:
            return 'Обе матрицы должны быть размера NxN. '


m = [[1, 2, 7], [3, 4, 8], [5, 6, 9]]
mat = Matrix(m)
m1 = [[2, 4, 2], [0, 2, 1], [-2, 0, 0]]
mat2 = Matrix(m1)
print(mat)
print()
print(mat + mat2)
