from words_from_text import poem


class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
        self.__text = ''

    def add_text(self, text: str):
        self.__text += text

    def __enter__(self):
        if self.pages < len(self.__text):
            chars_on_page = len(self.__text) // self.pages
        else:
            self.pages = len(self.__text)
            chars_on_page = 1
        return (
            self.__text[i*chars_on_page : (i+1)*chars_on_page]
            for i in range(self.pages)
        )

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


b1 = Book('Руслан и Людмила', 'Александр Пушкин', 226)
b1.add_text(poem)

with b1 as pages:
    b1_p = list(pages)

print(f'{len(b1_p) = }')
print(f'{len(b1_p[0]) = }')
print(b1_p[:2], end='\n\n')

for i in range(10):
    print(b1_p[i], end='\n\n')
