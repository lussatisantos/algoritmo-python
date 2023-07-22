print('-'*30)
print('Contando: ', end='')
for i in range(1, 11, 1):
    print(f'{i} ', end='')
print()
print('-'*30)
print()

print('-'*30)   
print('Contagem regressiva: ', end='')
for i in range(10, 0, -2):
    print(f'{i} ', end='')
print()

def contador(a, b, c):
    for i in range(a, b+c, c):
        print(f'{i} ', end='')
    print()

print('-'*30)
print('Sua vez de contar: ')   
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('Contando: ', end='')
contador(inicio, fim, passo)
print('-'*30)