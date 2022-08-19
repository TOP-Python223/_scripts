from itertools import dropwhile


email1 = 'ab.cd@ef.gh'
email2 = 'ab.cd@efgh'
email3 = 'abcd@ef.gh'
email4 = 'abc@def'


def is_not_at(char: str) -> bool:
    """Предикат проверки на '@'."""
    return True if char != '@' else False


for email in (email1, email2, email3, email4):
    part = ''.join(dropwhile(is_not_at, email))
    print(part, end='\t')
    print(True if '.' in part else False)
