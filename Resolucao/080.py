temp = []
princ = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Pesos: ')))
    princ.append(temp[:])
    temp.clear()

    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print(f'Os dados foram {princ}')