from datetime import date
data = date.today().year

ano = 0
maior = 0
menor = 0

for i in range(0, 7):
    num = int(input('Digite o ano de nascimento: '))
    ano = data - num
    if ano > 17:
        maior += 1
    else:
        menor += 1

print('Os anos digitados {} sao maiores de idade' .format(maior))
print('Os anos digitados {} sao menores de idade' .format(menor))