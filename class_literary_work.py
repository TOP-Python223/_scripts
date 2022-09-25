from typing import Optional

class LiteraryWork:
    def __init__(self, title: str, author_name: str, year: int):
        self.title: str = title
        self.author: str = author_name
        self.year: int = year
        self.form: Optional[str] = None
        self.genre: Optional[str] = None
        self.chars: Optional[int] = None
        self.cycle: Optional[tuple[str, int]] = None
        self.annotation: Optional[str] = None
        self.tags: set[str] = set()
        self.similar: set['LiteraryWork'] = set()

    def add_similar(self, work: 'LiteraryWork'):
        self.similar.add(work)

    def __str__(self):
        return f"{self.author.title()}. {self.title.capitalize()}\n" \
               f"Год написания: {self.year}\n" \
               f"Форма: {self.form}. Жанр: {self.genre}\n" \
               f"{self.chars} зн.\n" \
               f"Цикл: {f'{self.cycle[0]} #{self.cycle[1]}' if self.cycle else '—'}"


catalog = [
    LiteraryWork('Дети времени', 'Адриан Чайковски', 2015),
    LiteraryWork('Костяные корабли', 'Роберт-Джеймс Баркер', 2019),
    LiteraryWork('Зона справедливости', 'Евгений Лукин', 1998),
    LiteraryWork('Прыг-скок', 'Эдгар Аллан По', 1849),
    LiteraryWork('Сердце-обличитель', 'Эдгар Аллан По', 1843)
]

for i in range(len(catalog)):
    book = catalog[i]
    if not book.similar:
        print(f'\nХотите добавить похожие произведения для {book.title}', end=' ')
        if input(r'[y\n]? ').lower() == 'y':
            title = input('Название: ')
            author = input('Автор: ')
            year = int(input('Год написания: '))
            new_book = LiteraryWork(title, author, year)

            # добавление ссылки на объект в множество
            book.add_similar(new_book)
            # добавление ссылки на объект в список
            catalog.append(new_book)

            print(new_book, end='\n'*2)

    print('\n', book, sep='', end='\n'*2)
