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
elif receb == 2:
        valor = pago - (pago * 0.05)
        print('Voce teve 5% de desconto por Cartao')
        print('O seu pagamento final sera {} Kz' .format(valor))
elif receb == 3:
      print('O seu pagamento final sera {} Kz' .format(pago))
elif receb == 4:
      parcelas = int(input('Quantas parcelas: '))
      if parcelas >= 3:
            valor = (pago / parcelas) + ((pago + 0.2) / parcelas)
            total = pago + (pago * 0.2)

            print('Voce tera juro de 20% por {} parcelas' .format(parcelas))
            print('O seu pagamento por parcela sera {} Kz e o pagamento final de {} Kz' .format(valor, total))
      else:
            print('Parcela invalida, apenas valido pra 3 ou mais parcela')
            