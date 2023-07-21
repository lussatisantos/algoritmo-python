jogador = dict()
partidas = list()
time = list()

while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ')
    tot = int(input(f'Quantos jogos {jogador["nome"]} fez? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos golos {c+1} fez?: ')))
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
print('-='*23)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*50)
for k, v in enumerate(time):
    print(f'{k:>4} ' ,end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*50)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro, codigo do jogador nao encontrado {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['golos']):
            print(f'     No jogo {i+1} fez {g} golos')
        print('-'*40)
print('<< VOLTE SEMPRE >>')