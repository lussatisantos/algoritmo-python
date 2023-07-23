def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam =len(msg)
    print('~'*tam)
    print(msg)
    print('~'*tam)

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Funcao ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)