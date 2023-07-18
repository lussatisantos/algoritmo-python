listagem = ('Lapis', 50,
          'Borracha', 50,
          'Caderno', 300,
          'Estojo', 800,
          'Transferidor', 120,
          'Compasso', 150,
          'Mochila', 7400,
          'Canetas', 400,
          'Livros', 17000)
print('=-'*20)
print(f'{"LISTAGEM DE PRECOS":^40}')
print('=-'*20)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'AOA {listagem[pos]:> 3.2f}')
print('=-'*20)