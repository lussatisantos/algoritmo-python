valores = list()
num = 0

while True:
    num = int(input('Digite um numero: '))

    if num not in valores:
        valores.append(num)
        print('Numero adicionado com sucesso!!!')
    else:
        print('Numero NAO adicionado, valor ja se encontra no banco de dados')
    opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'S':
        print('=-'*20)
    else:
        break
print(f'Voce digitou os seguintes valores {sorted(valores)}')