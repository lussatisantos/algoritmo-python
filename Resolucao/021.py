num = int(input('Digite um numero: '))

print('Unidade: {}' .format(num // 1 % 10))
print('Dezena: {}' .format(num // 10 % 10))
print('Centena: {}' .format(num // 100 % 10))
print('Milhar: {}' .format(num // 1000 % 10))