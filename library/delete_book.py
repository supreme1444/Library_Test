import json
import os
import sys


class Delete:
    def delete_book_in_library(self):
        if not os.path.exists('books.json'):
            print("Файл books.json не существует.")
            return

        delete_book_library = input("Введите id той книги, которую хотите удалить: ")
        try:
            with open('books.json', 'r', encoding='utf-8') as file:
                book_list = json.load(file)

            book_found = False
            for book in book_list:
                if book.get('id_book') == delete_book_library:
                    book_list.remove(book)
                    book_found = True
                    print(f"Книга с id {delete_book_library} была удалена.")
                    break

            if not book_found:
                print(f"Книга с id {delete_book_library} не найдена.")
            else:
                with open('books.json', 'w', encoding='utf-8') as file:
                    json.dump(book_list, file, ensure_ascii=False, indent=4)
                print("Изменения сохранены в файл books.json.")

        except json.JSONDecodeError:
            print("Ошибка при чтении файла JSON.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

        while True:
            action = input(
                "Что вы хотите сделать дальше? (1 - удалить еще одну книгу, "
                "2 - вернуться в главное меню, "
                "3 - выйти из приложения): ")
            if action == '1':
                self.delete_book_in_library()
                break
            elif action == '2':
                print("Возвращение в главное меню...")
                return
            elif action == '3':
                print("Выход из приложения...")
                sys.exit()
            else:
                print("Неверный ввод, пожалуйста, введите 1, 2 или 3.")


