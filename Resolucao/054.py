soma_idade = 0
media = 0
maior_homem = 0
velho = 0
mulher = 0

for grupo in range (1, 5):
    print('------ {} PESSOA ------' .format(grupo))

    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade

    if grupo ==1 and sexo in 'Mm':
        maior_homem = idade
        velho = nome

    if sexo in 'Mm' and idade > maior_homem:
        maior_homem = idade
        velho = nome
    if sexo in 'Ff' and idade > 20:
        mulher += 1

media = soma_idade / 4

print('A media de idade do grupo e de {} anos' .format(media))
print('O homem mais velho tem {} anos de nome {}' .format(maior_homem, velho))
print('Ao todo sao {} mulheres com menos de 20 anos' .format(mulher))