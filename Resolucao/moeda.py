def aumentar(num):
    return num+100

def diminuir(num):
    return num-100

def dobro(num):
    return num*2

def metade(num):
    return num/2

def moedas(num=0, moe='AOA '):
    return f'{moe}{num:.2f}'.replace('.', ',')