from pprint import pprint
from random import randrange as rr, choice
from typing import Optional


class Cat:
    hunter_mode: str = 'hunt mice'

    def __init__(self, name: str, gender: str):
        self.name = name
        self.gender = gender

    @staticmethod
    def meow() -> str:
        return 'meow'

    def ask_for_food(self) -> str:
        return rr(3, 6)*self.meow()

    def reproduce(self, name: str) -> Optional['Cat']:
        if self.gender.upper() == 'F':
            return self.__class__(name, choice(['M', 'F']))

    @classmethod
    def catch_mouse(cls, time: int):
        return choice(
            [cls.hunter_mode for _ in range(20 - time)]
            + ['mouse caught']
        )

    def __str__(self):
        return f'<Cat: {self.name}>'



yara = Cat('Яра', 'F')
# str(yara)
print(yara, end='\n\n')


# работа обычного метода
print(f'{Cat.ask_for_food = }')
print(f'{yara.ask_for_food = }')
print(yara.ask_for_food(), end='\n\n')
# yara.ask_for_food() -> Cat.ask_for_food(yara)
# instance.method(*args, **kwargs) -> Class.function(instance, *args, **kwargs)

kitten = yara.reproduce('котёнок')
print(kitten, end='\n\n')


# работа статического метода
print(f'{Cat.meow = }')
print(f'{yara.meow = }')
print(f'{Cat.meow is yara.meow = }')
print(yara.meow(), end='\n\n')


# работа классового метода
print(f'{Cat.catch_mouse = }')
print(f'{yara.catch_mouse = }')
print(yara.catch_mouse(15))
# yara.catch_mouse() -> Cat.catch_mouse(Cat)
# instance.classmethod(*args, **kwargs) -> Class.function(Class, *args, **kwargs)
