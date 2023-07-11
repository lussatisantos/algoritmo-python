from datetime import date
ano_actual = date.today().year

ano = int(input('Ano de nacimento: '))

valor = ano_actual - ano

if valor <= 9:
    print('O atleta tem {} anos' .format(valor))
    print('Classificacao: MIRIM')