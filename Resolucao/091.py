jogador = dict()
partidas = list()
time = list()

while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ')
    tot = int(input(f'Quantos jogos {jogador["nome"]} fez? '))
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos golos golos {1} jogo: ')))
    jogador['golos'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = input('Quer continuar? [S/N]: ').upper()[0]
        if resp in 'SN':
            break
        print('Erro, responda somente S ou N')
    if resp == 'N':
        break
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3}' ,end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
print('-'*40)
print('-='*25)
print(f'O jogador {jogador["nome"]} fez {len(jogador["golos"])} jogos')
for i,v in enumerate(jogador['golos']):
    print(f'      => Na partida {i+1}, fez {v} golos')
print(f'Foi um total de {jogador["total"]} golos')