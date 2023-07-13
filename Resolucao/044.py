from time import sleep

fogo = int(input('[0] para comecar a contagem do fogo de artificio: '))

if fogo == 0:
    for i in range(10, 0, -1):
        print(i)
        sleep(1)
    print('BOOOOMMMMM!!!!!!!')
else:
    print('Contagem cancelada')