from moeda import dobro, metade, moedas, aumentar, diminuir

def prints(n):
    print(f'O dobro de {moedas(n)}, e igual a {moedas(dobro(n))}')
    print(f'A metade de {moedas(n)}, e igual a {moedas(metade(n))}')
    print(f'Aumentando 10% sera {moedas(aumentar(n, 10))}')
    print(f'Dminuindo 10% sera {moedas(diminuir(n, 10))}')
    