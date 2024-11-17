# Создайте класс Student, который имеет:

# Атрибуты name, age и grades (список оценок).

# Метод add_grade(grade), который добавляет новую оценку
# в список.

# Метод average_grade, который возвращает средний балл студента.


class Student:
    def __init__(self, name: str, age: int, grades: list):
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        sum = 0
        count = 0
        for grade in self.grades:
            sum += grade
            count += 1
        medium = sum / count
        return medium

student = Student('Marina', 20, [5, 5, 3, 4, 5, 4, 5, 5, 5])
student.add_grade(5)
print(student.average_grade())

