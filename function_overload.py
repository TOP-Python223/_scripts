from typing import overload


# перегрузка в python работает только для определения различных типов параметров, но не для определения различного кода для разных сигнатур одной и той же функции
@overload
def test(n: int): ...
@overload
def test(n: float): ...
def test(n):
    print(n)


test(1)
test(2.1)
test('abc')
