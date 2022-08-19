text = "12-ый граф д'Эгильон потратил 12 экю в Париже. Ужасный скряга!"
web = ['www.google.com', 'https://10.0.0.1/index.htm', 'yandex.ru', 'ss64.org']

sq = '\''
print(f"{text.replace('12', '18') = }\n")
print(f"{text.replace('а', '') = }\n")
print(f"{text.replace('а', '', 2) = }\n")
print(f"{text.replace(sq, '`') = }\n")
print(r"text.replace(' ', '\n') =", text.replace(' ', '\n'), end='\n\n')


for addr in web:
    print(f"{addr.strip('.:/cghmoprstuw') = }")
