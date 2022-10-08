from string import whitespace, ascii_letters as asl


class EmptyStringError(Exception):
    pass


class TextProcessor:
    def __init__(self, text: str):
        self.text = text

    def clear_non_letters(self) -> str:
        if not self.text:
            raise EmptyStringError

        non_letters = set(self.text) - set(asl) - set(whitespace)
        return self.text.translate(
            {ord(ch): None for ch in non_letters}
        )


exc = None
tp = TextProcessor('')
try:
    tp.clear_non_letters()
except EmptyStringError as e:
    exc = e

print(exc.__class__)
