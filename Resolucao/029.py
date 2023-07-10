viagem = float(input('Digite a distancia da viagem: '))

if viagem<=200:
    preco = viagem * 0.50
    print('Voce pagara {} pela viagem' .format(preco))
else:
    preco = viagem * 0.45
    print('Voce pagara {} pela viagem' .format(preco))