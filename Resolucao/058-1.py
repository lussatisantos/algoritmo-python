n = int(input('Digite um numero: '))
a = n
f = 1
while a > 0:
    print('{}' .format(a), end='')
    print(' x ' if a > 1 else ' = ', end='')
    f *= a
    a -= 1
print(f)
print('\n')