num = s = tot = 0
num = int(input('Digite um numero qualquer [Digite 999 para parar]: '))
while num != 999:
    s += 1
    tot += num
    num = int(input('Digite um numero qualquer [Digite 999 para parar]: '))
print('Voce digitou {} numeros e soma entre eles e igual a {}' .format(s, tot))