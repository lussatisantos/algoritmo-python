casa = float(input('Quanto custa a casa? AOA '))
salario = float(input('Qual o teu salario mensal? AOA '))
anos = int(input('Em quantos anos de prestacao? '))

valor_a_pagar = casa / (anos * 12)
porc_mensal = salario * 0.3

print('Para comprar uma casa de {} Kz em {} anos a prestacao mensal sera de {:.2f} Kz' .format(casa, anos, valor_a_pagar))

if porc_mensal >= valor_a_pagar:
    print('Emprestimo CONCEDIDO')
else:
    print('Emprestimo NEGADO')