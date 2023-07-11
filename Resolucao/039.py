nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Infelizmente voce esta REPROVADO')
elif media <= 6.9:
    print('Voce foi ao RECURSO')
elif media>= 7 and media < 10.1:
    print('PARABENS, voce esta APROVADO')
else:
    print('ERRO, tente novamente!!')