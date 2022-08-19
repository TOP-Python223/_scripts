from string import ascii_lowercase as alc, ascii_uppercase as auc, digits
from random import randrange as rr, choice

def printtable(columns: tuple, 
               border_h: str = '—',
               border_v: str = '|',
               center: bool = True) -> None:
    """Печатает таблицу по столбцам с границами."""
    # количество рядов
    rows = max(len(col) for col in columns)
    # ширина столбца для каждого из столбцов кортежем
    width_columns = tuple(max([len(cell) for cell in col]) + 2 
                          for col in columns)
    # общая ширина таблицы
    width = sum(width_columns) + len(columns) + 1
    
    # верхняя граница
    print(border_h*width)
    # построчный вывод
    for i in range(rows):
        # значения из столбцов выравниваем по ширине
        values = ()
        for j in range(len(columns)):
            if center:
                values += (''.join(columns[j][i:i+1]).center(width_columns[j]),)
            else:
                values += (''.join(columns[j][i:i+1]).ljust(width_columns[j]),)
        # разделяем занчения вертикальными границами
        cells = border_v.join(values)
        print(border_v + cells + border_v)
        print(border_h*width)
    

# генерация данных
col1 = []
for _ in range(rr(10, 20)):
    word = []
    for _ in range(rr(3,6)):
        word += [choice(choice((alc, auc)))]
    col1 += [''.join(word)]

col2 = [str(num) for num in range(rr(15, 25))]

col3 = [''.join([choice(choice((auc, digits))) for _ in range(4)]) 
        for _ in range(15)]

col4 = [str(num*5) for num in range(rr(15, 25))]

# вывод таблицы
printtable([col1, col2, col3, col4])
