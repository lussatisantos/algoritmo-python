frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)

inverso = ''

for letra in range(len(junto) -1, -1, -1):
     inverso += junto[letra]
print('O inverso de {} sera {}'.format(junto, inverso))

if inverso == junto:
     print('Temos um PALINDROMO')
else:
     print('A frase digitada nao e um PALINDROMO')