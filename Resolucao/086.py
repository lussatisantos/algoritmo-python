lista = dict ()

lista['nome'] = str(input('Digite o seu nome: ')) 
lista['media'] = float(input('Digite a sua media: '))

print(f'O seu nome e {lista["nome"]}')
print(f'A sua media e de {lista["media"]} valores')

if lista['media'] < 5:
    print('Voce esta Reprovado')
elif lista['media'] < 7:
    print('Voce esta em Recuperacao')
else:
    print('Voce esta Aprovado')