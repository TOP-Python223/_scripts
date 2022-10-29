"""Single Responsibility Principle — Принцип Единственной Ответственности"""

from pathlib import Path
from sys import path, executable
from time import sleep
from typing import Optional

from datetime import datetime as dt


class Journal:
    def __init__(self):
        self.__entries: list[str] = []

    def add_entry(self, entry: str):
        self.__entries += [f'{dt.now():%d.%m.%Y - %H:%M}\n{entry}\n']

    # нарушение SRP — взаимодействие с файловой системой не является ответственностью Журнала
    # default_path: str | Path
    # def save_to_file(self):
    #     with open(self.default_path, 'w', encoding='utf-8') as fileout:
    #         fileout.write(str(self))

    def __str__(self):
        return '\n'.join(self.__entries)


# соблюдение SRP — отдельный класс для взаимодействий с файловой системой
class FileManager:
    default_path: str | Path = Path(Path(executable).drive) / 'windows/temp/journal.log'

    @classmethod
    def save_to_file(cls, text: str, file_path: Optional[str | Path] = None):
        if file_path is None:
            file_path = cls.default_path
        with open(file_path, 'w', encoding='utf-8') as fileout:
            fileout.write(text)


journal = Journal()

journal.add_entry('test_entry_1')
sleep(70)
journal.add_entry('test_entry_2')

# journal.save_to_file()
FileManager.save_to_file(str(journal))
