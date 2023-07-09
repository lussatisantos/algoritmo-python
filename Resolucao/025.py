nome = str(input('Digite o seu nome completo: ')).strip().split()

print('O seu primeiro nome: {}' .format(nome[0]))
print('O seu ultimo nome: {}' .format(nome[len(nome)-1]))