galera = []
pessoa = {}
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo [M/F]: ').upper()[0]
        if pessoa['sexo'] in 'SM':
            break
        else:
            print('Erro, digite somente M ou F')
    pessoa['idade'] = int(input('Idade: '))
    galera = pessoa[:]
    while True:
        resp = input('Quer continuar? [S/N]: ').upper()[0]
        if resp in 'SN':
            break
        else:
            print('Erro, responda somente S ou N')
    if resp == 'N':
        break
print('-='*25)
print(galera)