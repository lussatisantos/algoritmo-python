s = tot = 0
leitura = 'S'

while leitura in 'Ss' and leitura not in 'Nn':
    num = int(input('Digite um numero: '))
    leitura = str(input('Quer continuar? [S/N] '))
    s += 1
    tot += num
media = tot / s
print('Voce digitou {} numeros e a media foi {}' .format(s, media))