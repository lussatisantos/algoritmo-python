metro = float(input('Digite a quantidade de metros: '))

print('{}metros equivale a: ')
print('{:.0f}km' .format(metro/1000))
print('{:.0f}hm' .format(metro/100))
print('{:.0f}dm' .format(metro/10))
print('{:.0f}dc '.format(metro*10))
print('{:.0f}cm '.format(metro*100))
print('{:.0f}mm '.format(metro*1000))