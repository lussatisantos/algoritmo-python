num = int(input('Digite um numero: '))

print(''' Escolha uma das opcoes para converter:
[1] converta em BINARIO
[2] converta em OCTAL
[3] converta em HEXADECIMAL
''')
      
convert = int(input('Digite a sua opcao: '))

if convert == 1:
    print('{} convertido em BINARIO sera {}' .format(num, bin(num)))
