num = int(input('Digite um numero: '))

print(''' Escolha uma das opcoes para converter:
[1] converta em BINARIO
[2] converta em OCTAL
[3] converta em HEXADECIMAL
''')
      
convert = int(input('Digite a sua opcao: '))

if convert == 1:
    print('{} convertido em BINARIO sera {}' .format(num, bin(num)))
elif convert == 2:
    print('{} convertido em OCTAL sera {}' .format(num, oct(num)))
elif convert == 3:
    print('{} convertido em HEXADECIMAL sera {}' .format(num, hex(num)))