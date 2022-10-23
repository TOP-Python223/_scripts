class TOKENS:
    @property
    def value(self):
        return 'X', 'O'

TOKENS = TOKENS()

print(TOKENS.value)



def TOKENS():
    return 'X', 'O'

print(TOKENS())
