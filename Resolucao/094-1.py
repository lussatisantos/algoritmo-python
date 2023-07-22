def contador(a, b, c):
    for i in range(a, b+c, c):
        print(f'{i} ', end='')
def linha():
    print('-='*20)


print()
linha()
print('Contagem crescente: ', end='')
contador(1, 10, 1)
print()
linha()
print('Contagem decrescente: ', end='')
contador(10, 0, -2)
print()
linha()

print('Chegou a sua vez de contar')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('Fazendo a sua contagem: ', end='')
contador(inicio, fim, passo)
print()
linha()
print('     << FINAL DO ALGORITMO >>')