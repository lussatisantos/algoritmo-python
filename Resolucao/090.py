galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo [M/F]: ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('Erro, digite somente M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())  
    
    while True:
        resp = input('Quer continuar? [S/N]: ').upper()[0]
        if resp in 'SN':
            break
        else:
            print('Erro, responda somente S ou N')
    if resp == 'N':
        break
print('-='*25)
print(f'A) Ao todo temos {len(galera)} pessoas caadastradas')
media = soma / len(galera)
print(f'B) A media de idade e de {media:5.2f} anos')
print('C) As mulheres cadastradas foram ',end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estao acima da media: ')
for p in galera:
    if p['idade'] >= media:
        print('  ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
            print()
print('<< TERMINADO >>')