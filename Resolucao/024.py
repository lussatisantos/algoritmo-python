nom = input('Digite algo: ').upper().strip()

print('A letra A aparece {} vezes na frase.' .format(nom.count('A')))
print('A primeira letra A apareceu na posicao {}' .format(nom.find('A')+1))
print('A ultima letra A apareceu na posicao {}' .format(nom.rfind('A')+1))