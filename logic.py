s = 'line'
# s = 12
# s = 'square'

if type(s) is str and s == 'line':
    print('––––––––––')
else:
    print('errorr')

if s == 'line' or s == 'square':
    print('figure')


a = False
b = True
c = True

print(not a or b and c)
print(not (a or b) and c)
