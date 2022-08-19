# объявление функции
def firstfunc():
    # тело функции
    print("It's a func!")

# вызов функции
a = firstfunc()
# возвращаемый функцией объект — None
print(f"{a = }\t{type(a) = }")



def adder():
    num = 5 + 10
    # возврат функцией значения
    return num

b = adder()
print(f"{b = }\t{type(b) = }")
