def factorial(a=0, show=False):
    """
    -> Calcular o Factorial de um numero:
    :params a: O numero a ser calculado
    :params show: (Opcional) mostrar ou :nao a conta
    :return: O valor do factorial de um :numero a
    """
    cont = 1
    for i in range(a, 0, -1):
        if show:
            print(i, end='')
            if i>1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        cont *= i
    return cont

print(factorial(5, show=True))
help(factorial)