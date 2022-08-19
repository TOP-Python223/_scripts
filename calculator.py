def calculator(num1, num2, operation):
    if operation == '+':
        # выражение вычисляется — результат возвращается
        return num1 + num2
    elif operation == '-':
        # возвратов может быть неограниченное количество
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2


while op := input('math sign > '):
    res = calculator(int(input('n1 > ')), int(input('n2 > ')), op)
    print(f"{res = }\t{type(res)}\n")
