jogador = dict()
partidas = list()
jogador['nome'] = input('Nome do jogador: ')
tot = int(input(f'Quantos jogos {jogador["nome"]} fez? '))

for c in range(0, tot):
    partidas.append(int(input(f'Quantos golos {c} jfez: ')))
jogador['golos'] = partidas[:]
jogador['total'] = sum(partidas)

print('-='*25)
print(jogador)
print('-='*25)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*25)
print(f'O jogador {jogador["nome"]} fez {len(jogador["golos"])} jogos')
for i,v in enumerate(jogador['golos']):
    print(f'      => Na partida {i+1}, fez {v} golos')
print(f'Foi um total de {jogador["total"]} golos')