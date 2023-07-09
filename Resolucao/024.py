nom = input('Digite algo: ').upper()

print('A letra A aparece {} vezes na frase.' .format(nom.count('A')))
print('A primeira letra A apareceu na posicao {}' .format(nom.find('A')+1))