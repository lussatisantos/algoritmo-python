from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.4)
    print('PRONTOS')

#def somaPar():

numeros = list()
sorteia(numeros)