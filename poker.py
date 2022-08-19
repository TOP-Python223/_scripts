from random import randrange as rr

while True:
    if input("\n > хотите выйти(q)? ").lower() == 'q':
        break
    # валет – 11, дама – 12, король – 13
    hand = tuple(rr(1, 14) for _ in range(5))
    print(f"\n{hand = }")
    
    comb_label = 'старшая карта'
    
    unique = set(hand)
    u_len = len(unique)
    
    if u_len == 4:
        comb_label = 'пара'
    
    elif u_len == 3:
        if max([hand.count(card) for card in unique]) == 2:
            comb_label = 'две пары'
        else:
            comb_label = 'сет'
    
    elif u_len == 5:
        hand_sort = sorted(hand)
        if hand_sort == range(hand_sort[0], hand_sort[0]+5):
            comb_label = 'стрит'
    
    elif u_len == 2:
        if max([hand.count(card) for card in unique]) == 3:
            comb_label = 'фулл-хаус'
        else:
            comb_label = 'каре'

    elif u_len == 1:
        comb_label = 'Шулер!'
    
    print(comb_label)
