class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def str(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def repr(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    @classmethod
    def check_pages(cls, value):
        if type(value) != int:
            raise TypeError('attribute pages bust be int')
        if not (1 < value < 255):
            raise ValueError('attribute pages is out of range')

    def __init__(self, name: str, author: str, pages: int) -> None:
        super().__init__(name, author)
        self.check_pages(pages)
        self._pages = pages

    @property
    def pages(self):
        return self.pages

    @pages.setter
    def pages(self, value):
        self.check_pages(value)
        self.pages = value


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float):
            raise TypeError('attribute duration bust be float')
        if not (0.5 < value < 255.66):
            raise ValueError('attribute duration is out of range')
        self._duration = value