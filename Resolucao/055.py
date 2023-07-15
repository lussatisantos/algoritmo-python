sexo = str(input('Digite o seu sexo: ')).strip()

while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos, tente novamente [M/F] : ')).strip().upper()
print('Sexo {} registrado com sucesso!' .format(sexo))