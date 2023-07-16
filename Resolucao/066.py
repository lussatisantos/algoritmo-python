m18 = h = muabaixo20 = 0

while True:
    print('-='*20)
    print('ANALISADOR DE GRUPO')
    print('-='*20)

    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if idade > 18:
        m18 += 1
    elif sexo in 'M':
        h += 1
    elif sexo == 'F' and idade < 20:
        muabaixo20 += 1

    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao not in 'Ss':
        break

print(f'No seu grupo existem {m18} maiores de 18 anos, {h} homens registrados e {muabaixo20} mulheres com menos de 20 anos')