eng_alphabet = {chr(i): i-96 for i in range(97, 123)}
print(f"{eng_alphabet = }\n")

get_descr = """get(key[, default])
Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.
"""
print(get_descr)

for char in get_descr:
    print(eng_alphabet.get(char, 0), end=' ')
print('\n')

for char in get_descr:
    eng_alphabet.setdefault(char, 0)
print(f"{eng_alphabet = }\n")

