n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1 > n2 and n2 > n3:
    maior = n1
else:
    menor = n1
if n2 > n3 and n3 > n1:
    maior = n2
else:
    menor = n2
if n3 > n1 and n1 > n2:
    maior = n3
else:
    menor = n3

print('O maior numero digitado e: {}' .format(maior))
print('O menor numero digitado e: {}' .format(menor))