empresa = 'EscoladeProgramadores'
instrutor = 'Ivan Sanches'     
# %%

# esta biblioteca não é nossa é interna do python
import random

# imprime números aleatórios
print(random.randint(1,100))


# criando uma lista de número aleatórios

numeros   = []
num_par   = 0
num_impar = 0
for x in range(10):
    numeros.append(random.randint(1,100))
    print(numeros)
 
for x in range(10):
    if numeros[x] % 2 == 0:
        print(f'o número {numeros[x]} é par')
        num_par += 1
    else:
        print(f'O número {numeros[x]} é impar') 
        num_impar += 1
print('\n',numeros)

print(f'A quantidade de número pares é: {num_par}')
print(f'A quantidade de número impares é: {num_impar}')