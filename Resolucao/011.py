preco = float(input('Digite o preco de um produto: '))

print('O produto tem o preco original de {}, como estamos em promocao, voce teras 5% de desconto e pagaras somente {:.2f} AOA' .format(preco, (preco*0.05)- preco))