while True:
    lista = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezanove', 'vinte')

    num = int(input('Digite um numero: '))

    if num < 0:
        print('Numero invalido, tente novamente entre 0 a 20')
    elif num > 20:
        print('Numero invalido, tente novamente entre 0 a 20')
    else:
        print(f'Numero {num} por extenso e {lista[num]}')
        break