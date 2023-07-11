r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima pode formar triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO')
else:
    print('Os segmentos acima NAO PODEM FORMAR TRIANGULO')