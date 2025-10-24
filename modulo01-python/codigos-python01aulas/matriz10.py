import numpy as np

# é necessário o dtype=object para a versão mais recente do python
var_notas = np.zeros((2,5), dtype=object)
var_media = 0


print('Programa que calcula média')
for x in range(2):
    var_notas[x,0] = input('Digite seu nome: ')
    for y in range(4):
        var_notas[x, y + 1] = input('Digite uma nota: ')

# impressão
print('=============================')
for x in range(2):
    print(f'O nome é: {var_notas[x,0]} e suas notas foram: ')
    var_media = 0
    for y in range(4):
        print(f'{y + 1}ª nota: {var_notas[x, y + 1]}')
        var_media = var_media + float(var_notas[x, y + 1])
    var_media /= 4
    print(f'E a média é: {var_media}')
print(var_notas)