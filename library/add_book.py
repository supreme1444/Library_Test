import json
import sys
import uuid
from typing import Dict, Any, Union

from book.book_class import Book

class AddBook:
    """
    Класс для добавления книг в систему.

    Этот класс позволяет пользователю вводить информацию о книге и сохранять
    ее в формате JSON. Он обрабатывает ввод пользователя, проверяет корректность
    данных и управляет добавлением книг в файл.

    Attributes:
        None
    """

    def load_book(self) -> None:
        """
        Запрашивает у пользователя информацию о книге и добавляет ее в систему.

        Метод бесконечно запрашивает у пользователя данные о книге, такие как
        автор, название, год издания и статус. После успешного ввода данных
        книга добавляется в файл JSON. Если ввод некорректен, метод повторяет
        запрос.

        Returns:
            None
        """
        while True:
            try:
                print("Введите информацию о книге:")
                author: str = input("Введите автора: ").title()
                title: str = input("Название книги: ").title()
                year_input: str = input("Год издания: ").strip()
                try:
                    year: int = int(year_input)
                except ValueError:
                    print("Ошибка: Пожалуйста, введите корректный год.")
                    continue

                id_book: str = str(uuid.uuid4())
                while True:
                    status: str = input(
                        "Статус книги (по умолчанию 'доступна'. Или введите 'выдана'): ").strip().lower()
                    if status in ['доступна', 'выдана', '']:
                        if status == '':
                            status = 'доступна'
                        break
                    else:
                        print("Ошибка: введите 'доступна' или 'выдана'.")
                new_book: Book = Book(id_book=id_book, author=author, title=title, year=year, status=status)
                json_data: Dict[str, Any] = new_book.to_dict()
                self.append_book(json_data)
                if not self.handle_next_action():
                    return
            except ValueError as e:
                print(f"Ошибка ввода. Введите данные заново: {e}")
            except Exception as e:
                print(f"Произошла ошибка: {e}")

    @staticmethod
    def handle_next_action() -> Union[bool, None]:
        """
        Обрабатывает действие, которое пользователь хочет выполнить после добавления книги.

        Запрашивает у пользователя, что он хочет сделать дальше: добавить
        еще одну книгу, вернуться в главное меню или выйти из приложения.

        Returns:
            bool: True, если пользователь хочет добавить книгу, False, если
            он хочет вернуться в меню, или None при выходе из приложения.
        """
        while True:
            action: str = input(
                "Что вы хотите сделать дальше? (1 - добавить книгу, "
                "2 - вернуться в главное меню, "
                "3 - выйти из приложения): ").strip()
            print(f"Пользователь ввел: '{action}'")

            if action == '1':
                return True
            elif action == '2':
                print("Возвращение в главное меню...")
                return False
            elif action == '3':
                print("Выход из приложения.")
                sys.exit()
            else:
                print("Ошибка: введите 1, 2 или 3.")

    @staticmethod
    def append_book(json_book: Dict[str, Any]) -> None:
        """
        Добавляет книгу в файл JSON.

        Метод читает существующий файл 'books.json', добавляет в него новую
        книгу и сохраняет изменения. Если файл не существует, он будет создан.

        Args:
            json_book (Dict[str, Any]): Словарь с информацией о книге.

        Returns:
            None
        """
        try:
            with open('books.json', 'r', encoding='utf-8') as file:
                book_uppend: list = json.load(file)
        except FileNotFoundError:
            book_uppend = []
        except json.JSONDecodeError:
            print("Ошибка при чтении файла JSON.")
            return

        book_uppend.append(json_book)
        with open('books.json', 'w', encoding='utf-8') as file:
            json.dump(book_uppend, file, ensure_ascii=False, indent=2)
            print("Книга добавлена")
