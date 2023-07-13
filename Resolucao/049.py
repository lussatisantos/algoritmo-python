primeiro = int(input('Primeiro termo: '))
razao = int(int(input('Razao: ')))
decimo = primeiro + (10 - 1) * razao

for i in range(primeiro, decimo + razao, razao):
    print('{}'.format(i), end=' -> ')
print('ACABOU')