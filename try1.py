print('start')

try:
    # a = b
    a = [1]
    # print(a[1])
    # a += '1'
    print('abc')

except TypeError:
    print('проблема с типами')

except NameError:
    print('проблема с именами')

except:
    print('что-то пошло не так')

else:
    print('всё в порядке')

finally:
    print('выполняется всегда')

print('end')
