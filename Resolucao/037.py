from datetime import date
ano_actual = date.today().year

ano_nascimento = int(input('Em que ano voce nasceu? '))

valor = ano_actual - ano_nascimento

if valor < 18:
    print('Voce nao esta idade de se alistar')
    idade = 18 - valor
    print('O seu alistamento sera em {}' .format(ano_actual + idade))