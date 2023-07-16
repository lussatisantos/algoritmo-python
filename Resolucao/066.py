from random import randint

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ''
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? [P/I] '))
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total}')