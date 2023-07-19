numeros = []

while True:
    n = int(input('Digite um numero: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Nao foi possivel adicionar este numero')
    
    opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if opcao == 'N':
        break

print(f'A lista contem {len(numeros)} elementos')
numeros.sort(reverse = True)
print(f'A lista de ordem descrescente sera {numeros}')