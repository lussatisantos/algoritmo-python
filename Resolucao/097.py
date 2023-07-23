def factorial(a=0):
    cont = 1
    for i in range(a, 0, -1):
        cont *= i
    return cont

print(factorial(5))