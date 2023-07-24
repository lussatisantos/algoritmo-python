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
        
def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opcao: ')
    return opc










def existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    