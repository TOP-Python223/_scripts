"""Модуль для кодирования и декодирования кириллических сообщений с помощью шифра Цезаря."""

ALPHABET = ({i-1071: chr(i) for i in range(1072, 1078)}
            | {7: 'ё'}
            | {i-1070: chr(i) for i in range(1078, 1104)})
ALPHABET_REV = {value: key for key, value in ALPHABET.items()}


def encode(message: str, shift: int) -> str:
    """Кодирует исходное сообщение с помощью шифра Цезаря с определённым сдвигом."""
    cypher = ''
    for char in message:
        try:
            ordnum = ALPHABET_REV[char]
        except KeyError:
            cypher += char
        else:
            resind = ordnum + shift
            if resind > 33:
                cypher += ALPHABET[resind-33]
            else:
                cypher += ALPHABET[resind]
    return cypher


def decode(cypher: str, shift: int) -> str:
    """Декодирует сообщение, зашифрованное с помощью шифра Цезаря, с определённым сдвигом."""
    message = ''
    for char in cypher:
        try:
            ordnum = ALPHABET_REV[char]
        except KeyError:
            message += char
        else:
            resind = ordnum - shift
            if resind < 1:
                message += ALPHABET[33+resind]
            else:
                message += ALPHABET[resind]
    return message


def decode_blind(cypher: str) -> tuple:
    """Декодирует сообщение, зашифрованное с помощью шифра Цезаря, перебирая все возможные варианты сдвига."""
    variants = ()
    for shift in range(1, 33):
        variants += ((decode(cypher, shift), shift),)
    return variants


while True:
    comm = input('\n > ')
    
    if not comm:
        break
    
    elif comm == 'encode':
        text = input(' _ сообщение > ')
        shift = int(input(' _ сдвиг > '))
        print(encode(text.lower(), shift))
    
    elif comm == 'decode':
        text = input(' _ шифр > ')
        shift = int(input(' _ сдвиг > '))
        print(decode(text.lower(), shift))
    
    elif comm == 'blind':
        text = input(' _ шифр > ')
        print(*decode_blind(text.lower()), sep='\n')
