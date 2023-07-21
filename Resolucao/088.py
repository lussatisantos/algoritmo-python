from datetime import date
hoje  = date.today().year

trabalho = {}

trabalho['nome'] = input('Digite o seu nome: ')
trabalho['ano'] = hoje - int(input('Ano de nascimento: '))
trabalho['carteira'] = int(input('Digite o numero da carteira [0 para encerrar]: '))