# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(f'создано комплексное число: {a} + {b}i')

    def __add__(self, other):
        return f'сложение: {self.a + other.a} + {self.b + other.b}j'

    def __mul__(self, other):
        return f'умножение: {self.a * other.a - self.b * other.b} + {self.b * other.a + self.a * other.b}j'


cn1 = ComplexNum(1, 2)
cn2 = ComplexNum(3, 4)
print(cn1 + cn2)
print(cn1 * cn2)

# сравним с результатом работы перегруженных методов
a = 1 + 2j
b = 3 + 4j
print(a + b)
print(a * b)
