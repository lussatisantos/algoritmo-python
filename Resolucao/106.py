def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um numero inteiro valido')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuario')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um numero inteiro valido')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuario')
            return 0
        else:
            return n
        
num = leiaInt('Digite um valor inteiro: ')
nume = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitao foi {num} e o real digitado foi {nume}')