total = totmil = 0
while True:
    nome = str(input('Digite o produto: ')).strip()
    preco = float(input('Digite o preco: '))
    total += preco
    if preco > 10000:
        totmil += 1
    s = ' '
    while s not in 'SN':
        s = str(input('Quer continuar? [S/N] ')).strip().upper()

    if s == 'N':
        break
print('{:-^40}' .format(' FIM DO PROGRAMA '))
print(f'O total da compra foi {total:10.2f}')
print(f'Temos {totmil} produtos a custar mais de 10k')