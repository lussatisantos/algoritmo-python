s = tot = maior = menor = 0
leitura = 'S'

while leitura in 'Ss' and leitura not in 'Nn':
    num = int(input('Digite um numero: '))
    menor = num
    leitura = str(input('Quer continuar? [S/N] '))
    s += 1
    tot += num

    if menor > maior:
        maior = menor
    else:
        menor = num
media = tot / s
print('Voce digitou {} numeros e a media foi {}' .format(s, media))
print('O maior valor foi {} e o menor valor foi {}' .format(maior, menor))