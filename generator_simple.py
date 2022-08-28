def gen_strings():
    yield 'abc'
    yield 'def'
    yield 'ghi'
    yield 'jkl'
    yield 'mno'
    yield 'pqr'
    yield 'stu'
    yield 'vwx'
    yield 'yz'


for s in gen_strings():
    print(s)

gen = gen_strings()

print(gen.__next__())
