soma = 0
s = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        s += 1
        soma += i
print('A soma de todos os {} valores solicitados sera {}' .format(s, soma))