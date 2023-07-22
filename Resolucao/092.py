def area(a, b):
    s = a * b
    print(f'A area do terreno {larg}x{comp} sera {s}m**2')

print('  Controle de Terrenos')
print('-'*25)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)