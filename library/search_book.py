import json
from book.book_class import Book
from typing import List, Dict, Any

class SearchBook:
    """
    Класс для поиска книг в библиотеке.

    Этот класс предоставляет функциональность для поиска книг по различным критериям,
    таким как название, автор и год. Данные книг загружаются из файла JSON.

    Attributes:
        None
    """

    def search_book_panel(self) -> None:
        """
        Отображает панель поиска и обрабатывает выбор пользователя.

        Пользователь может выбрать, по какому критерию искать книги (название, автор, год).
        Если пользователь решает выйти, программа завершает работу.

        Returns:
            None
        """
        while True:
            search_panel: str = input("Нажмите 1 для поиска по названию книги\n"
                                      "Нажмите 2 для поиска по автору книги\n"
                                      "Нажмите 3 для поиска по году книги\n"
                                      "Нажмите 4 для выхода\n")
            try:
                choice: int = int(search_panel)
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

    def search_title(self) -> bool:
        """
        Ищет книги по названию.

        Запрашивает у пользователя название книги и ищет совпадения в списке книг.
        Если книга найдена, выводит её данные. Позволяет пользователю продолжить поиск.

        Returns:
            bool: True, если пользователь хочет продолжить, иначе False.
        """
        while True:
            title: str = input("Введите название: ").strip()
            if not title:
                print("Название не может быть пустым.")
                continue
            books: List[Book] = self.open_file()
            found: bool = False
            for book in books:
                if book.title.lower() == title.lower():
                    self.output(book.to_dict())
                    found = True
            if not found:
                print("Книга не найдена.")
            if not self.ask_to_continue():
                return False
            return True

    def search_author(self) -> bool:
        """
        Ищет книги по автору.

        Запрашивает у пользователя имя автора и ищет совпадения в списке книг.
        Если книга найдена, выводит её данные. Позволяет пользователю продолжить поиск.

        Returns:
            bool: True, если пользователь хочет продолжить, иначе False.
        """
        while True:
            author: str = input("Введите автора: ").strip().title()
            if not author:
                print("Автор не может быть пустым.")
                continue
            books: List[Book] = self.open_file()
            found: bool = False
            for book in books:
                if book.author == author:
                    self.output(book.to_dict())
                    found = True
            if not found:
                print("Книга не найдена.")
            if not self.ask_to_continue():
                return False
            return True

    def search_year(self) -> bool:
        """
        Ищет книги по году.

        Запрашивает у пользователя год и ищет совпадения в списке книг.
        Если книга найдена, выводит её данные. Позволяет пользователю продолжить поиск.

        Returns:
            bool: True, если пользователь хочет продолжить, иначе False.
        """
        while True:
            year: str = input("Введите год: ").strip()
            if not year.isdigit():
                print("Пожалуйста, введите корректный год.")
                continue
            books: List[Book] = self.open_file()
            found: bool = False
            for book in books:
                if str(book.year) == year:
                    self.output(book.to_dict())
                    found = True
            if not found:
                print("Книга не найдена.")
            if not self.ask_to_continue():
                return False
            return True

    @staticmethod
    def open_file() -> List[Book]:
        """
        Открывает файл с книгами и загружает их в виде объектов Book.

        Returns:
            List[Book]: Список объектов Book, загруженных из файла.
        """
        try:
            with open('books.json', 'r', encoding='utf-8') as file:
                book_data: List[Dict[str, Any]] = json.load(file)
                return [Book(**book) for book in book_data]
        except FileNotFoundError:
            print("Файл books.json не найден.")
            return []
        except json.JSONDecodeError:
            print("Ошибка при чтении файла JSON.")
            return []

    @staticmethod
    def output(dict_book: Dict[str, Any]) -> None:
        """
        Выводит информацию о книге.

        Args:
            dict_book (Dict[str, Any]): Словарь с данными книги для вывода.

        Returns:
            None
        """
        output: str = ', '.join(f"{key}: {value}" for key, value in dict_book.items())
        print(output)

    @staticmethod
    def ask_to_continue() -> bool:
        """
        Запрашивает у пользователя, хочет ли он продолжить поиск.

        Returns:
            bool: True, если пользователь хочет продолжить, иначе False.
        """
        while True:
            response: str = input("Хотите попробовать снова? (да/нет): ").lower()
            if response == "да":
                return True
            elif response == "нет":
                return False
            else:
                print("Неверный ввод. Пожалуйста, введите 'да' или 'нет'.")
