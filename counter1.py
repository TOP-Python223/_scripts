from collections import Counter
from words_from_text import words

c1 = Counter('helloworld')
print(f"\n{c1 = }")

words_rate = Counter(words)
# print(f"\n{words_rate = }")

print(f"\n{words_rate.most_common(5) = }")
