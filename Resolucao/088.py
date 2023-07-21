from datetime import date
hoje  = date.today().year

trabalho = {}

trabalho['nome'] = input('Digite o seu nome: ')
trabalho['ano'] = hoje - int(input('Ano de nascimento: '))
trabalho['carteira'] = int(input('Digite o numero da carteira [0 Nao tem]: '))

if trabalho['carteira'] == 0:
    print('-='*25)

    print(f'O seu nome e {trabalho["nome"]}')
    print(f'Voce tem actualmente {trabalho["ano"]} anos de idade')
    print(f'Nao possui uma Carteira Profissional')
else:
    trabalho['contratacao'] = int(input('Ano de contratacao: '))
    trabalho['salario'] = float(input('Salario (AOA): '))
    trabalho['aposentadoria'] = (trabalho['contratacao'] + 25) - (hoje - trabalho['ano'])

    print('-='*25)

    print(f'O seu nome e {trabalho["nome"]}')
    print(f'Voce tem actualmente {trabalho["ano"]} anos de idade')
    print(f'Foi contratado em {trabalho["contratacao"]}')
    print(f'Tem um salario de {trabalho["salario"]}')

    print(f'Voce se aposentara com {trabalho["aposentadoria"]} anos de idade')