salario = float(input('Digite o seu salario: '))

if salario>100000:
    print('Voce tem 10% de aumento e o teu salario sera {} Kz' .format((salario * 0.1) + salario))
else:
    print('Voce tem 20% de aumento e o salario sera {} Kz' .format((salario * 0.2) + salario))