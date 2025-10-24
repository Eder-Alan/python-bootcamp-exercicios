#=========================================
# for que significa para controlado.

for x in range(8): # range(8) é a quantidade de interções.
    print(x)
    print('segundo print', x + 1)

# range(8) é a quantidade de interções.
# range(8,10) o número 10 segundo número é até a onde deve ir.
print('----------------')
print('segundo for')
for x in range(8,10):
    print(x)


print('----------------')
print('terceiro for')
# range(0,10,2) 0 = a onde começa o loop
# 10 até a onde deve ir
# 2 pula de 2 em 2.
for x in range(0,10,2):
    print(x)


print('----------------')
print('quarto for')
print('Programa que imprime a taboada')
inicio = int(input('Digite o inicio de sua taboada: '))
fim = int(input('Digite o fim de sua taboada: '))
passo = int(input('Digite o passo de sua taboada: '))

for x in range(inicio, fim+1):
    print(f'{passo} * {x} = {passo * x}')

print('----------------')
print('quinto for')
print('Um for ao contrário')
for x in range(10,0,-1):
    print(x)
