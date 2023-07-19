lista = [[], []]
num = 0

for i in range(1, 8):
    num = (int(input(f'Digite o {i}o valor: ')))

    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print('-'*40)
print(f'Os numeros pares da lista sao {sorted(lista[0])}')
print(f'Os numeros impares da lista sao {sorted(lista[1])}')