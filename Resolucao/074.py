valores = list()

for i in range(0, 5):
    valores.append(int(input(f'Digite um valor na posicao {i}: ')))

print(f'Voce digitou os valores {valores}')

print(f'O maior numero digitado e {max(valores)} e esta na posicao {valores.index(max(valores)) + 1}')

print(f'O menor numero digitado e {min(valores)} e esta na posicao {valores.index(min(valores)) + 1}')