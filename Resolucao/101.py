def notas(*n, sit=False):
    """
    -> Funcao para analisar notas e situacoes de varios alunos
    :params n: uma ou mais notas dos alunos (aceita varios)
    :params sit: Valor opcional, inidicando se deve ou nao adicionar a situacao
    :return: dicionario com varias informacoes sobre a situacao da turma 
    """
    c = dict()
    c['total'] = len(n)
    c['maior'] = max(n)
    c['menor'] = min(n)
    c['media'] = sum(n)/len(n)

    if sit:
        if c['media'] >= 7:
            c['situacao'] = 'BOA'
        elif c['media'] >= 5:
            c['situacao'] = 'RAZOAVEL'
        else:
            c['situacao'] = 'RUIM'
 
    return c

resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)