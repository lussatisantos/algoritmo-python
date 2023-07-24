from moeda import dobro, metade, moedas

n = float(input('Digite um valor em AOA: '))
print(f'O dobro de {moedas(n)}, e igual a {moedas(dobro(n))}')
print(f'A metade de {moedas(n)}, e igual a {moedas(metade(n))}')