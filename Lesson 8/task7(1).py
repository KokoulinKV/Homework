# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
# умножение созданных экземпляров. Проверьте корректность полученного результата.


class Complex:
    def __init__(self, complex_num):
        self.complex_num = complex_num

    def __add__(self, other):
        a = str(self.complex_num)[1:-1].split('+')
        b = str(other.complex_num)[1:-1].split('+')
        e = [(int(a[0]) + int(b[0])), (int((a[1].split('j'))[0]) + int((b[1].split('j'))[0]))]
        f = '+'.join([str(el) for el in e]) + 'j'
        return f

    def __mul__(self, other):
        a = str(self.complex_num)[1:-1].split('+')
        b = str(other.complex_num)[1:-1].split('+')
        a[1] = (a[1].split('j'))[0]
        b[1] = (b[1].split('j'))[0]
        for i in range(len(a)):
            a[i] = int(a[i])
            b[i] = int(b[i])
        e = [(a[0]*b[0] - a[1]*b[1]), (a[0]*b[1] + b[0]*a[1])]
        f = '+'.join([str(el) for el in e]) + 'j'
        return f


comp1 = Complex(1+2j)
comp2 = Complex(2+3j)
print(comp1 + comp2)
print(comp1 * comp2)