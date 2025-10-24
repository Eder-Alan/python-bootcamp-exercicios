# Peça ao usuário para digitar números continuamente. O loop deve parar
# quando a soma dos números digitados ultrapassar 100 ou usuário digitar 0.

print('Programa que faz soma de números até 100')

var_valores = 0
var_total   = 0

while True:
    var_valores = float(input('Digite um número para somar ou (0) zero para parar: '))
    print(f'{var_valores} + {var_total} = ',end='')
    var_total += var_valores
    print(f'{var_total}')
    if(var_total > 100 or var_valores == 0):
        break
print(f'O total dos valores é: {var_total}')


# ======================= melhorias
print('Programa que faz soma de números até 100')

total = 0

while True:
    numero = float(input('Digite um número para somar (0 para parar): '))

    # Verifica antes de somar
    if numero == 0:
        break

    total += numero
    print(f'Soma parcial: {total}')

    if total > 100:
        print('A soma ultrapassou 100!')
        break

print(f'\nO total dos valores é: {total}')
