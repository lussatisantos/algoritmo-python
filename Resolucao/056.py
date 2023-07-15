import random
adivinha = random.randint(0, 10)
soma = 0

print('=== VAMOS BRINCAR DE ADIVINHA ===')
print('Eu vou pensar um numero de 0 a 10, adivinhe!')
num = int(input('Qual sera o seu palpite: '))



while adivinha != num:
    num = int(input('Voce perdeu, tente novamente: '))
    soma += 1


print('Parabens voce acertou eu pensei em {} e voce em {}' .format(adivinha, num))
print('Voce precisou de {} palpites para acertar' .format(soma))