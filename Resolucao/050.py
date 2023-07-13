num = int(input('Digite um numero: '))
s = 0

for i in range(1, num+1):
    if num % i == 0:
      print('\033[33m')
      s += 1
    else:
        print('\033[31m')

if s == 2:
   print('O numero {} e PRIMO' .format(num))
else:
   print('O numero {} nao e PRIMO' .format(num))