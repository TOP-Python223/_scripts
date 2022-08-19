t = True
f = False

print(type(t))

print('bool to...')
print('...int:', int(t), int(f))
print('...float:', float(t), float(f))
print('...complex:', complex(t), complex(f))
print('...str:', str(t), str(f))
print()

print('...to bool:')
print('int...:', bool(-12), bool(0))
print('float...:', bool(0.00001), bool(0.0))
print('complex...:', bool(1j), bool(0j))
print('str...:', bool(' '), bool(''))
print('list...:', bool(['']), bool([]))
print('tuple...:', bool(([],)), bool(tuple()))
print()
 