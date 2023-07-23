def ficha(nome='<desconhecido>', gol=0):
   print(f'O jogador {nome} fez {gol} golos no campeonato')

nom = str(input('Nome do jogador: ')).strip()
golo = str(input('Numero de golos: '))
if golo.isnumeric():
    golo = int(golo)
else:
    golo = 0
if nom.strip() == '':
    ficha(gol=golo)
else:
    ficha(nom, golo)