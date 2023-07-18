from random import randint

lista = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print ('Os valores sorteados foram: ' ,end='')

for i in lista:
    print(f'{i} ', end='')
print('\n')
print(f'O maior valor sorteado foi {max(lista)}')
print(f'O menor valor sorteado foi {min(lista)}')