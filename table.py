from string import ascii_lowercase as alc, ascii_uppercase as auc, digits
from random import randrange as rr, choice

DEBUG = False

col1 = []
for _ in range(rr(10, 20)):
    # col1 += [''.join( [choice(choice((alc, auc))) for _ in range(rr(3,6))] )]
    word = []
    for _ in range(rr(3,6)):
        word += [choice(choice((alc, auc)))]
    if DEBUG:
        print(f"{word = }")
    col1 += [''.join(word)]

col2 = [str(num) for num in range(rr(15, 25))]

col3 = [''.join([choice(choice((auc, digits))) for _ in range(4)]) 
        for _ in range(15)]


rows = max(len(col1), len(col2), len(col3))

width_col1 = max([len(el) for el in col1]) + 2
width_col2 = max([len(el) for el in col2]) + 2
width_col3 = max([len(el) for el in col3]) + 2

width = width_col1 + width_col2 + width_col3 + 4

for i in range(rows):
    print('|' + '|'.join([''.join(col1[i:i+1]).center(width_col1), 
                          ''.join(col2[i:i+1]).center(width_col2), 
                          ''.join(col3[i:i+1]).center(width_col3)]) + '|')
    print('—'*width)
