maior = 0
menor = 0
for i in range(1,6):
    n = float(input('Quanto pesa a {} pessoa: ' .format(i)))
    if i == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print('O maior peso foi de {} kg' .format(maior))
print('O menor peso foi de {} kg' .format(menor))