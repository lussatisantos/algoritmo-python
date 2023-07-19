todos = []
pares = []
impares = []

while True:
    num = int(input('Digite um numero: '))

    if num not in todos:
        todos.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    opcao = str(input('Quer continuar? [S/N]: '))

    if opcao in 'Nn':
        break
print(f'A sua lista sera {todos}')
print(f'Os valores pares da sua lista sao {pares}')
print(f'Os valores impares da sua lista sao {impares}')