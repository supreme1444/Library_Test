import json
from book.book_class import Book

class SearchBook:
    def search_book_panel(self):
        while True:
            search_panel = input("Нажмите 1 для поиска по названию книги\n"
                                 "Нажмите 2 для поиска по автору книги\n"
                                 "Нажмите 3 для поиска по году книги\n"
                                 "Нажмите 4 для выхода\n")
            try:
                choice = int(search_panel)
                if choice == 1:
                    if not self.search_title():
                        return
                elif choice == 2:
                    if not self.search_author():
                        return
                elif choice == 3:
                    if not self.search_year():
                        return
                elif choice == 4:
                    print("Выход из программы.")
                    break
                else:
                    print("Неверный выбор, попробуйте снова.")
            except ValueError:
                print('Недопустимый ввод, пожалуйста, введите число.')

    def search_title(self):
        while True:
            title = input("Введите название: ").strip()
            if not title:
                print("Название не может быть пустым.")
                continue
            books = self.open_file()
            found = False
            for book in books:
                if book.title.lower() == title.lower():
                    self.output(book.dict())
                    found = True
            if not found:
                print("Книга не найдена.")
            if not self.ask_to_continue():
                return False
            return True

    def search_author(self):
        while True:
            author = input("Введите автора: ").strip().title()
            if not author:
                print("Автор не может быть пустым.")
                continue
            books = self.open_file()
            found = False
            for book in books:
                if book.author == author:
                    self.output(book.dict())
                    found = True
            if not found:
                print("Книга не найдена.")
            if not self.ask_to_continue():
                return False
            return True

    def search_year(self):
        while True:
            year = input("Введите год: ").strip()
            if not year.isdigit():
                print("Пожалуйста, введите корректный год.")
                continue
            books = self.open_file()
            found = False
            for book in books:
                if str(book.year) == year:
                    self.output(book.dict())
                    found = True
            if not found:
                print("Книга не найдена.")
            if not self.ask_to_continue():
                return False
            return True

    def open_file(self) -> list[Book]:
        try:
            with open('books.json', 'r', encoding='utf-8') as file:
                book_data = json.load(file)
                return [Book(**book) for book in book_data]
        except FileNotFoundError:
            print("Файл books.json не найден.")
            return []
        except json.JSONDecodeError:
            print("Ошибка при чтении файла JSON.")
            return []

    def output(self, dict_book):
        output = ', '.join(f"{key}: {value}" for key, value in dict_book.items())
        print(output)

    def ask_to_continue(self):
        while True:
            response = input("Хотите попробовать снова? (да/нет): ").lower()
            if response == "да":
                return True
            elif response == "нет":
                return False
            else:
                print("Неверный ввод. Пожалуйста, введите 'да' или 'нет'.")
