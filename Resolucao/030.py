ano = int(input('Qual ano queres analisar? '))

if ano % 4 == 0:
    print('O ano {} e BISSEXTO' .format(ano))
else:
    print('O ano {} nao e bissexto' .format(ano))