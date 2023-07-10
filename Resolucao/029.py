viagem = float(input('Digite a distancia da viagem: '))

print('Voce esta prestes a comecar uma viagem de {} Km' .format(viagem))

if viagem<=200:
    preco = viagem * 200
    print('Voce pagara {} Kz pela viagem' .format(preco))
else:
    preco = viagem * 175
    print('Voce pagara {} Kz pela viagem' .format(preco))