total = totmil = menor = cont = 0
barato = ''
while True:
    nome = str(input('Digite o produto: ')).strip()
    preco = float(input('Digite o preco: '))
    cont += 1
    total += preco
    if preco > 10000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    s = ' '
    while s not in 'SN':
        s = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if s == 'N':
        break
print('{:-^40}' .format(' FIM DO PROGRAMA '))
print(f'O total da compra foi {total:10.2f}')
print(f'Temos {totmil} produtos a custar mais de 10k')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')