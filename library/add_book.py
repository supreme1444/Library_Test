import json
import sys
import uuid

from book.book_class import Book


class AddBook:
    def load_book(self):
        while True:
            try:
                print("Введите информацию о книге:")
                author = input("Введите автора: ")
                title = input("Название книги: ")
                year_input = input("Год издания: ")
                try:
                    year = int(year_input)
                except ValueError:
                    print("Ошибка: Пожалуйста, введите корректный год.")
                    continue
                id_book = str(uuid.uuid4())
                while True:
                    status = input("Статус книги (по умолчанию 'доступна'. Или введите 'выдана'): ").strip().lower()
                    if status in ['доступна', 'выдана', '']:
                        if status == '':
                            status = 'доступна'
                        break
                    else:
                        print("Ошибка: введите 'доступна' или 'выдана'.")
                new_book = Book(id_book=id_book, author=author, title=title, year=year, status=status)
                json_data = new_book.dict()
                if not self.duplicate_book(json_data):
                    self.append_book(json_data)
                another = input("Хотите добавить еще одну книгу? (да/нет): ").strip().lower()
                if another != 'да':
                    exit_choice = input("Хотите выйти из приложения? (да/нет): ").strip().lower()
                    if exit_choice == 'да':
                        print("Выход из приложения.")
                        sys.exit()
                    else:
                        break

            except ValueError as e:
                print(f"Ошибка ввода. Введите данные заново: {e}")
            except Exception as e:
                print(f"Произошла ошибка: {e}")

    def duplicate_book(self, json_book):
        try:
            with open('books.json', 'r', encoding='utf-8') as file:
                book_list = json.load(file)
        except FileNotFoundError:
            book_list = []
        except json.JSONDecodeError:
            print("Ошибка при чтении файла JSON.")
            return False  # Возвращаем False, если ошибка

        for book in book_list:
            if (json_book['title'].strip().lower() == book['title'].strip().lower() and
                    json_book['author'].strip().lower() == book['author'].strip().lower() and
                    json_book['year'] == book['year']):
                choice_made = False
                while not choice_made:
                    choice = input("Такая книга есть. Продублировать ее нажмите 1 или выйти нажмите 2: ")
                    try:
                        choice_uppend = int(choice)
                        if choice_uppend == 1:
                            self.append_book(json_book)
                            choice_made = True
                            return True
                        elif choice_uppend == 2:
                            sys.exit()
                        else:
                            print("Ошибка: введите 1 для продублирования или 2 для выхода.")
                    except ValueError:
                        print("Ошибка: пожалуйста, введите число 1 или 2.")

        return False

    def append_book(self, json_book):
        with open('books.json', 'r', encoding='utf-8') as file:
            book_uppend = json.load(file)
            book_uppend.append(json_book)
        with open('books.json', 'w', encoding='utf-8') as file:
            json.dump(book_uppend, file, ensure_ascii=False, indent=2)
            print("Книга добавлена")
