from time import sleep
opcao = 0

numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))

while opcao != 5:
    print ('''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 [ 1 ] Somar
 [ 2 ] Multiplicar
 [ 3 ] Maior
 [ 4 ] Novos numeros
 [ 5 ] Terminar o programa
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        ''')
    opcao = int(input('O que desejas: '))

    if opcao == 1:
        soma = numero1 + numero2
        sleep(1)
        print ('A soma de {} e {} e igual a {}' .format(numero1, numero2, soma))
        