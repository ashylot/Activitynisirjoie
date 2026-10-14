class Book:
    def __init__(self, title: str = "", number_of_pages: int = 0, is_fictional: bool = False):
        self.title = title
        self._number_of_pages = number_of_pages
        self.is_fictional = is_fictional

    def get_title(self) -> str:
        return self._title

    def set_title(self, title: str):
        self._title = title

    def get_number_of_pages(self) -> int:
        return self._number_of_pages

    def set_number_of_pages(self, pages: int):
        self._number_of_pages = pages

    def get_is_fictional(self) -> bool:
        return self._is_fictional

    def set_is_fictional(self, is_fictional: bool):
        self._is_fictional = is_fictional

    def display(self):
        print("Title:", self._title)
        print("Number of Pages:", self._number_of_pages)
        print("Is Fictional:", self._is_fictional)
