algo = input('Digite algo: ')
print('O tipo primitivo desse valor e: ', type(algo))
print('E numerico ', algo.isnumeric())
print('So tem espacos espaco? ', algo.isspace())
print('E alfabetico ', algo.isalpha())
print('E alfanumerico ', algo.isalnum())
print('Esta em maisculas ', algo.isupper())
print('Esta em minusculas ', algo.islower())
print('Esta com inicial maiscula ou capitalizado ', algo.istitle())