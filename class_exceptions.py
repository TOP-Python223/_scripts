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


test_text = """A Current Directory for each drive?
Originally in MS-DOS, each drive had its own current directory, for complex historical reasons.

Now in Win32, there is one global current directory, but at the command line the appearance is still maintained that each drive has its own current directory, this is a fake-out by cmd.exe.
The location for each drive is stored using the undocumented environment variables =A:, =B:, =C: etc.

The only reason you need to be aware of this is that GUI Windows applications may have a different current directory than the command prompt. Similarly two CMD sessions can each have a different current directory."""

exc = None
tp = TextProcessor(test_text)
try:
    print(tp.clear_non_letters(), end='\n'*3)
except EmptyStringError as e:
    exc = e

print(exc.__class__)
