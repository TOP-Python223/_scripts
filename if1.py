a = 1

# одна условная инструкция
if a == 1:
    print('a == 1')
    a = 10
elif a > 0:
    print('a > 0')
    a = -a
else:
    print('else')

# print('end of if...elif...else statement')

# две условных инструкции
if a == 10:
    print('a == 10')
    a = 100
if a < 0:
    print('a > 0')
    a = -a
else:
    print('else')
