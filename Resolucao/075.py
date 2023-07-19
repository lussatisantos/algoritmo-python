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

    while opcao not in 'SN':
        opcao = input('Tente novamente [S/N]: ')
        if opcao == 'N':
            break
