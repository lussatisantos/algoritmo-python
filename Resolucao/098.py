def voto(ano):
    from datetime import date
    h = date.today().year
    idade = h - ano

    if idade < 16:
        return 'VOTO NEGADO'
    elif idade >= 16 and idade < 18:
        return 'VOTO OPCIONAL'
    elif idade > 18 and idade < 60:
        return 'VOTO OBRIGATORIO'

a = int(input('Digite o seu ano: '))
print(voto(a))
