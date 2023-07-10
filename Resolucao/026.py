import random

print('=== VAMOS BRINCAR DE ADIVINHA ===')
num = int(input('Eu vou pensar um numero de 0 a 5, adivinhe: '))

adivinha = random.randint(0, 5)

if num>5:
    print('Numero invalido, tente de 0 a 5')
else:
    if adivinha == num:
        print('PARABENS, voce ganhou o jogo, eu pensei em!!!!')
    else:
        print('Voce perdeu, tente novamente!!!')