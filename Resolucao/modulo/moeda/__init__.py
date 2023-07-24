def aumentar(num, imp):
    tot = num + (num*imp/100)
    return tot

def diminuir(num, imp):
    tot = num - (num*imp/100)
    return tot

def dobro(num):
    return num*2

def metade(num):
    return num/2

def moedas(num=0, moe='AOA '):
    return f'{moe}{num:.2f}'.replace('.', ',')

def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', ',').strip()
        if entrada.isalpha():
            print(f'ERRO: \"{entrada}\" e um numero invalido')
        else:
            valido = True
            return float(entrada)