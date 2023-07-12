peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('O seu IMC e {}' .format(imc))
    print('Voce esta ABAIXO DO PESO')
elif imc <= 25:
    print('O seu IMC e {}' .format(imc))
    print('PARABENS, voce tem o PESO IDEAL')
elif imc <= 30:
    print('O seu IMC e {}' .format(imc))
    print('Voce esta com SOBREPESO, aproveite fazer EXERCICIOS')
elif imc <= 40:
    print('O seu IMC e {}' .format(imc))
    print('Voce tem OBESIDADE, Cuidado!!!')
    print('Contacte um Personal Trainer ou va a um ginasio')
else:
    print('O seu IMC e {}' .format(imc))
    print('Voce tem OBESIDADE MORBIDA, contacte um Medico para uma assistencia')