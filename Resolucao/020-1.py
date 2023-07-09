nome = input('Digite o seu nome: ').strip()

print('O seu nome em maisculas sera {}' .format(nome.upper()))
print('O seu nome em minusculas sera {}' .format(nome.lower()))
print ('O seu nome tem {} letras' .format(len(nome) - nome.count(' ')))

new = nome.split()
print('O seu primeiro nome e {} e tem {} letras' .format(new[0], len(new[0])))