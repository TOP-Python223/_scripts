# валет – 11, дама – 12, король – 13

from random import randrange as rr

def checkhand(cards: tuple[int]) -> str:
    """Проверяет переданный кортеж на наличие комбинаций покера (холдем)."""
    unique = set(cards)
    u_len = len(unique)
    if u_len == 4:
        return 'пара'
    elif u_len == 3:
        if max([cards.count(card) for card in unique]) == 2:
            return 'две пары'
        else:
            return 'сет'
    elif u_len == 5:
        hand_sort = sorted(cards)
        if hand_sort == range(hand_sort[0], hand_sort[0]+5):
            return 'стрит'
    elif u_len == 2:
        if max([cards.count(card) for card in unique]) == 3:
            return 'фулл-хаус'
        else:
            return 'каре'
    elif u_len == 1:
        return 'Шулер!'
    return 'старшая карта'


# применение функций значительно повышает читаемость кода верхнего уровня
while True:
    if input("\n > хотите выйти(q)? ").lower() == 'q':
        break
    # генерация руки
    hand = tuple(rr(1, 14) for _ in range(5))
    print(f"\n{hand = }")
    # проверка на наличие комбинаций
    print(checkhand(hand))
