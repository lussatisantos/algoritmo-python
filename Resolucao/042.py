pago = float(input('Preco das compras: AOA '))

print('''Qual e a forma de pagamento:
[1] Dinheiro/Cheque
[2] Cartao
[3] 2x no Cartao
[4] 3x ou mais no Cartao
''') 

receb = int(input('Qual opcao: '))

if receb == 1:
    valor = pago - (pago * 0.1)
    print('Voce teve 10% de desconto por dinheiro/cheque')
    print('O seu pagamento final sera {} Kz' .format(valor))