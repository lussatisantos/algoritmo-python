from random import randint

def sorteia(lista):
    for cont in range(0,5):
        lista.append(randint(1, 10))

#def somaPar():

numeros = list()
sorteia(numeros)
print(numeros)