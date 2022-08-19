text = "12-ый граф д'Эгильон потратил 12 экю в Париже. Ужасный скряга!"

# метод возвращает новый объект – список
words = text.split()
print(words)
sents = text.split('.')
print(sents)
elems = text.split(' 12 ')
print(elems, end='\n\n')

# исходный объект не изменяется
print(text, end='\n\n')

text_join1 = ''.join(words)
print(text_join1)
text_join2 = '_'.join(words)
print(text_join2)
text_join3 = ' | '.join(words)
print(text_join3)
