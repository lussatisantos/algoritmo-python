num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo numero: ')))

print(f'Voce digitou: {num}')

print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 apareceu na {num.index(3) + 1} posicao')
else:
    print('O numero 3 nao foi digitadi em nenhuma posicao')
print('Os numeros pares digitados foram ', end='')

for i in num:
    if i % 2 == 0:
        print(i, end='')