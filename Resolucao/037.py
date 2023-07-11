from datetime import date
ano_actual = date.today().year

ano_nascimento = int(input('Em que ano voce nasceu? '))

valor = ano_actual - ano_nascimento

if valor < 18:
    print('Voce nao esta idade de se alistar')
    print('Voce tem apenas {} anos de idade' .format(valor))
    idade = 18 - valor
    print('O seu alistamento sera em {}' .format(ano_actual + idade))
elif valor == 18:
    print('Voce tem de se alistar IMEDIATAMENTE')
    print('Voce tem agora {} anos de idade' .format(valor))
