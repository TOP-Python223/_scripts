text = "12-ый граф д'Эгильон потратил 12 экю в Париже. Ужасный скряга!"

print(text)
while substr := input('\n > подстрока для поиска: '):
    i = text.find(substr)
    print(f'для {substr=} индекс = {i}')

while substr := input('\n > подстрока для поиска справа: '):
    i = text.lower().rfind(substr)
    print(f'для {substr=} индекс = {i}')


print(f'\n{text.startswith("12") = }')
print(f'\n{text.startswith("#") = }')

print(f'\n{text.endswith("#") = }')
print(f'\n{text.endswith("!") = }\n')


email = 'abcd@ef.gh'
email_wr = 'ab.cd@efgh.'

i_at = email.find('@')
if i_at > 0:
    if email.find('.', i_at+1, -2) > 0:
        print('email is correct')
    else:
        print('email is wrong')
else:
    print('email is wrong')

i_at = email_wr.find('@')
if i_at > 0:
    if email_wr.find('.', i_at+1, -2) > 0:
        print('email is correct')
    else:
        print('email is wrong')
else:
    print('email is wrong')


