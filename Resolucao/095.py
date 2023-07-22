from time import sleep

def maior(*num):
    cont = maior = 0
    print('-='*25)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.4)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados ao todo {cont} valores')
    print(f'O maior valor informado foi {maior}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 8)
maior(1, 2)
maior(6)
maior()