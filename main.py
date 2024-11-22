from library.add_book import AddBook
from library.search_book import SearchBook
from library.view_all import Viewallbooks
from library.delete_book import Delete
from library.change_status import ChangeStatus

class Welcom:
    """
    Класс для приветствия пользователя и управления библиотекой.

    Этот класс предоставляет меню для взаимодействия с приложением
    для управления книгами, включая добавление, просмотр, удаление,
    поиск книг и изменение их статуса.

    Attributes:
        None
    """

    @staticmethod
    def welcom_library() -> None:
        """
        Отображает приветственное сообщение и меню управления библиотекой.

        Предоставляет пользователю выбор действий, таких как добавление книги,
        просмотр списка книг, удаление книги, поиск книги и изменение статуса.
        Меню продолжает отображаться до тех пор, пока пользователь не выберет выход.

        Returns:
            None
        """
        print("Добро пожаловать в приложение для поиска книг")
        while True:
            choise = input("Что вы хотите сделать?" + '\n' +
                           "1) Добавить книгу" + '\n' +
                           "2) Просмотреть список книг" + '\n' +
                           "3) Удалить книгу" + '\n' +
                           "4) Поиск книги" + '\n' +
                           "5) Поменять статус" + '\n' +
                           "6) Выход" + '\n')
            try:
                choise = int(choise)
                if choise == 1:
                    AddBook().load_book()
                elif choise == 2:
                    view_book = Viewallbooks()
                    view_book.view_all_books()
                elif choise == 3:
                    delete_book = Delete()
                    delete_book.delete_book_in_library()
                elif choise == 4:
                    search_book_instance = SearchBook()
                    search_book_instance.search_book_panel()
                elif choise == 5:
                    status = ChangeStatus()
                    status.change_book_status_in_library()
                elif choise == 6:
                    break
                else:
                    print('Недопустимый ввод')
                    continue
            except ValueError:
                print('Недопустимый ввод')
                continue


if __name__ == "__main__":
    welcom = Welcom()
    welcom.welcom_library()
