while True:
    num = int(input('Pretendes ver qual tabuada: '))
    for i in range(1, 13):
        print(f'{num} x {i} = {num*i}')
    if num < 0:
        break
print('PROGRAMA ENCERRADO, Volte sempre!')