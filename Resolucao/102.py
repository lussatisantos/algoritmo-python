c = (
    '\033[n', #0 - sem cor
    '\033[0;30;41m', #1 - vermelho
)

def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam =len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'{msg}')
    print('~'*tam)
    print(c[cor], end='')

comando = ''
while True:
    titulo('  SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Funcao ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('  ATE LOGO', 1)