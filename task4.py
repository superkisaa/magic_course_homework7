# Создайте класс Triangle, который имеет:

# Атрибуты a, b и c для хранения длины сторон.

# Метод is_valid, который проверяет, можно ли из этих
# сторон составить треугольник (сумма любых двух сторон
# должна быть больше третьей).

# Метод perimeter, который возвращает периметр треугольника,
# если он существует, или выводит сообщение "Треугольник недопустим".

class Triangle:
    def __init__(self, a, b, c):
        self.length1 = a
        self.length2 = b
        self.length3 = c

    def is_valid(self):
        if (self.length1 + self.length2 < self.length3) or (self.length1 + self.length3 < self.length2) or (self.length2 + self.length3 < self.length1):
            return "Треугольник составить нельзя"

        return "Треугольник можно составить"

    def perimeter(self):
        if self.is_valid() == "Треугольник составить нельзя":
            return "Треугольник недопустим"
        return self.length1 + self.length2 + self.length3

treygolnik = Triangle(1, 4, 2)
print(treygolnik.is_valid())
print(treygolnik.perimeter())

treygolnik2 = Triangle(7, 8, 9)
print(treygolnik2.is_valid())
print(treygolnik2.perimeter())

