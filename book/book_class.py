class Book:
    """
    Класс Book представляет книгу с определенными атрибутами.

    Атрибуты:
        id_book (str): Уникальный идентификатор книги.
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.
        status (str): Статус книги (например, "доступна", "взята", "зарезервирована").

    Методы:
        to_dict() -> dict: Преобразует объект книги в словарь для удобного представления и
        возможно для сериализации данных.
    """

    def __init__(self, id_book: str, title: str, author: str, year: int, status: str) -> None:
        """
        Инициализирует новый экземпляр класса Book.

        Параметры:
            id_book (str): Уникальный идентификатор книги.
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
            status (str): Статус книги (например, "доступна", "взята", "зарезервирована").
        """
        self.id_book: str = id_book
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: str = status

    def to_dict(self) -> dict:
        """
        Преобразует объект книги в словарь.

        Возвращает:
            dict: Словарь, представляющий книгу с ее атрибутами.
        """
        return {
            "id_book": self.id_book,
            "author": self.author,
            "title": self.title,
            "year": self.year,
            "status": self.status,
        }