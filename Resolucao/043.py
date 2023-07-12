from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')

print(''' Suas opcoes:
[0] Pedra
[1] Papel
[2] Tesoura
''')
jogador = int(input('Qual sera a sua jogada: '))
computador = randint(0, 2)

print('O computador escolheu {}' .format(itens[computador]))
print('Voce escolheste {}' .format(itens[jogador]))