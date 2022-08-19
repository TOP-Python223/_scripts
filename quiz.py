"""Викторина"""

from random import randrange as rr, choice

QUESTIONS = {
    'Первый советский чемпион мира по шахматам?': 'Ботвинник',
    'Как звали маму Алексаднра Македонского?': 'Олимпиада',
    'Как называется пчелиный клей?': 'прополис',
    'Бумага для чертежей имеет название?': 'ватман'
}


def hint(answer: str, mask: str = '') -> str:
    """Возвращает замаскированный ответ, открывая по одной букве за вызов."""
    if not mask:
        mask = '*'*len(answer)
        return mask
    while True:
        i = rr(len(answer))
        if mask[i] == '*':
            break
    return mask[:i] + answer[i] + mask[i+1:]


for question, answer in QUESTIONS.items():
    print('\n'+question)
    print(mask := hint(answer))
    for _ in range(len(answer)):
        user_answer = input(' ответ > ').lower()
        if user_answer != answer.lower():
            print(mask := hint(answer, mask))
        else:
            print('Верно!')
            break
    else:
        print('Стыдно не знать!')
