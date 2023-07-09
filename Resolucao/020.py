nome = input('Digite o seu nome: ').strip()

print('O seu nome em maisculas sera {}' .format(nome.upper()))
print('O seu nome em minusculas sera {}' .format(nome.lower()))
print ('O seu nome tem {} letras' .format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem {} letras' .format(nome.find(' ')))