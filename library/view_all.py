import json
import os
import sys
from typing import List, Dict, Any

class Viewallbooks:
    """
    Класс для отображения всех книг из файла.

    Этот класс предоставляет функциональность для просмотра всех книг,
    хранящихся в файле JSON. Он проверяет наличие файла и его содержимое,
    а затем выводит информацию о каждой книге.

    Attributes:
        None
    """

    @staticmethod
    def view_all_books() -> None:
        """
        Отображает все книги из файла books.json.

        Проверяет наличие файла и его размер. Если файл существует и не пустой,
        загружает данные книг и выводит их на экран. После завершения отображения
        запрашивает у пользователя, хочет ли он вернуться в главное меню или выйти
        из приложения.

        Returns:
            None
        """
        file_path: str = 'books.json'
        if not os.path.exists(file_path):
            print("Указанный файл не существует.")
            return
        if os.path.getsize(file_path) == 0:
            print("Файл пустой.")
            return
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                book_list: List[Dict[str, Any]] = json.load(file)
                for books in book_list:
                    output: str = ', '.join(f"{key}: {value}" for key, value in books.items())
                    print(output)
            exit_choice: str = input("Хотите вернуться в главное меню? (да): ").strip().lower()
            if exit_choice == 'нет':
                print("Выход из приложения.")
                sys.exit()
        except FileNotFoundError:
            print("Указанный файл не существует.")
        except json.JSONDecodeError:
            print("Ошибка при чтении файла JSON.")
