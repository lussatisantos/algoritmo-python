velocidade = float(input('Digite a velocidade do carro em Km: '))

if velocidade<=80:
    print('Tenha um bom dia, e dirija com cuidado:')
else:
    multa = velocidade - 80
    print('Voce foi multado por excesso de velocidade')
    print('A sua multa esta avaliada em {} AOA' .format(multa*140))