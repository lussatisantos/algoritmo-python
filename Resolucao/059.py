primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao de PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')