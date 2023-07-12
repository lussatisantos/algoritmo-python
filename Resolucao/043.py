from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')

print(''' Suas opcoes:
[0] Pedra
[1] Papel
[2] Tesoura
''')
jogador = int(input('Qual sera a sua jogada: '))
computador = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 11)
print('O computador escolheu {}' .format(itens[computador]))
print('Voce escolheste {}' .format(itens[jogador]))
print('-=' * 11)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCE VENCEU')
    elif jogador == 2:
        print('EU VENCE')
    else:
        print('Jogada invalida!')
elif computador == 1:
    if jogador == 0:
        print('EU VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCE VENCEU')
    else:
        print('Jogada invalida!')
elif computador == 2:
    if jogador == 0:
        print('VOCE VENCEU')
    elif jogador == 1:
        print('EU VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada invalida!')