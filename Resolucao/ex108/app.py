from lib.interface import *
from time import sleep

arq = 'app.txt'

if existe(arq):
    print('Arquivo encontrado')
else:
    print('Arquivo nao encontrado')

while True:
    resp = menu(['ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do sistema'])
    if resp == 1:
        cabecalho('Oopcao 1')
    elif resp == 2:
        cabecalho('Oopcao 2')
    elif resp == 3:
        cabecalho('Saindo do sistema... Ate logo')
        break
    else:
        print('ERRO: digite uma opcao valida.')
    sleep(2)