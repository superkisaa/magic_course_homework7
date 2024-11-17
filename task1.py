# Создайте класс Book, который имеет:

# Атрибуты title, author и year.
# Метод get_info, который возвращает строку с информацией о книге в формате:
# "Название: [title], Автор: [author], Год издания: [year]".

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        info = f"Название: {self.title}, Автор: {self.author}, Год издания: {self.year}"
        return info

book = Book("Martin Iden", "Jake London", 1910)
print(book.get_info())