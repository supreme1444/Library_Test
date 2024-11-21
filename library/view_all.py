import json
import os
import sys


class Viewallbooks:
    def view_all_books(self):
        file_path = 'books.json'
        if not os.path.exists(file_path):
            print("Указанный файл не существует.")
            return
        if os.path.getsize(file_path) == 0:
            print("Файл пустой.")
            return
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                book_list = json.load(file)
                for books in book_list:
                    output = ', '.join(f"{key}: {value}" for key, value in books.items())
                    print(output)
            exit_choice = input("Хотите вернуться в главное меню? (да/нет): ").strip().lower()
            if exit_choice == 'нет':
                print("Выход из приложения.")
                sys.exit()
        except FileNotFoundError:
            print("Указанный файл не существует.")
        except json.JSONDecodeError:
            print("Ошибка при чтении файла JSON.")
