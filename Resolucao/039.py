nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('A sua media foi {} valores' .format(media))
    print('Infelizmente voce esta REPROVADO')
elif media <= 6.9:
    print('A sua media foi de {} valores' .format(media))
    print('Voce foi ao RECURSO')
elif media>= 7 and media < 10.1:
    print('A sua media foi de {} valores' .format(media))
    print('PARABENS, voce esta APROVADO')
else:
    print('ERRO, tente novamente!!')