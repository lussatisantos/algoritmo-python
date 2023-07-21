from datetime import date
hoje  = date.today().year

trabalho = {}

trabalho['nome'] = input('Digite o seu nome: ')
trabalho['ano'] = hoje - int(input('Ano de nascimento: '))
trabalho['carteira'] = int(input('Digite o numero da carteira [0 Nao tem]: '))

print('-='*25)

if trabalho['carteira'] == 0:
    print(f'O seu nome e {trabalho["nome"]}')
    print(f'Voce tem actualmente {trabalho["ano"]} anos de idade')
    print(f'Nao possui uma Carteira Profissional')