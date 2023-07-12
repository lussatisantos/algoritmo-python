peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('O seu IMC e {}' .format(imc))
    print('Voce esta abaixo do peso')
elif imc <= 25:
    print('O seu IMC e {}' .format(imc))
    print('PARABENS, voce tem o PESO IDEAL')