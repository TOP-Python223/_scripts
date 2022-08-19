phrase = input('enter a phrase: ')

unique_chars = tuple()
for char in phrase:
    if char not in unique_chars:
        unique_chars += (char,)

print(unique_chars)
print(f'{len(phrase) = }\t{len(unique_chars) = }')
