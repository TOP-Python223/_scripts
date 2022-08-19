"""Модуль для определния часов и минут из входного количества минут.

Использует согласование окончаний существительных."""


def get_minutes() -> int | None:
    """Циклически обрабатывает stdin для корректного получения числа."""
    while True:
        try:
            res = int(input('\nКоличество минут: '))
        except ValueError:
            print(' ! необходимо ввести число')
            continue
        else:
            return None if not res else res


def noun_ending_minute(number: int) -> str:
    """Подставляет нужное окончание для существительного 'минута' в зависимости от согласуемого числительного."""
    endings = {5: '', 6: '', 7: '', 8: '', 9: '', 0: '', 11: '', 12: '', 
               13: '', 14: '', 1: 'а', 2: 'ы', 3: 'ы', 4: 'ы'}
    last_digit, two_last_digits = number % 10, number % 100
    q = endings.get(two_last_digits)
    return q if q is not None else endings[last_digit]


def noun_ending_hour(number: int) -> str:
    """Подставляет нужное окончание для существительного 'час' в зависимости от согласуемого числительного."""
    endings = {5: 'ов', 6: 'ов', 7: 'ов', 8: 'ов', 9: 'ов', 0: 'ов', 
               11: 'ов', 12: 'ов', 13: 'ов', 14: 'ов', 1: '', 
               2: 'а', 3: 'а', 4: 'а'}
    last_digit, two_last_digits = number % 10, number % 100
    q = endings.get(two_last_digits)
    return q if q is not None else endings[last_digit]


while True:
    if (total := get_minutes()) is None:
        break
    hours, mins = total // 60, total % 60
    t_end = noun_ending_minute(total)
    h_end = noun_ending_hour(hours)
    m_end = noun_ending_minute(mins)
    print(f"{total} минут{t_end} — {hours} час{h_end} {mins} минут{m_end}")
