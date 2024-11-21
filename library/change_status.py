import json
import os
import sys


class Сhangestatus:
    def change_book_status_in_library(self):
        if not os.path.exists('books.json'):
            print("Файл books.json не существует.")
            return
        change_book_library = input("Введите id той книги, статус которой хотите изменить: ")
        try:
            with open('books.json', 'r', encoding='utf-8') as file:
                book_list = json.load(file)
            book_found = False
            for book in book_list:
                if book.get('id_book') == change_book_library:
                    if book['status'] == 'доступна':
                        book['status'] = 'выдана'
                    elif book['status'] == 'выдана':
                        book['status'] = 'доступна'
                    else:
                        print(
                            f"Статус книги с id {change_book_library} не может быть изменен, "
                            f"так как он не соответствует "
                            f"ожидаемым значениям.")
                        return
                    book_found = True
                    print(f"Статус книги с id {change_book_library} был изменен на '{book['status']}'.")
                    break
            if not book_found:
                print(f"Книга с id {change_book_library} не найдена.")
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
                "Что вы хотите сделать дальше? (1 - изменить статус еще одной книги, "
                "2 - вернуться в главное меню, "
                "3 - выйти из приложения): ")
            if action == '1':
                self.change_book_status_in_library()
                break
            elif action == '2':
                print("Возвращение в главное меню...")
                return
            elif action == '3':
                print("Выход из приложения...")
                sys.exit()
            else:
                print("Неверный ввод, пожалуйста, введите 1, 2 или 3.")
