# %%

# desta forma trago todas as funções da biblioteca.
import info
print(info.instrutor)


# %%
# e pode ser feito assim também
# desta forma eu trago apenas uma função da biblibioteca.
from info import empresa

print(empresa)

# %% Modulos Python
import random
numeros = []
par     = 0
impar   = 0

for x in range(20):
    numeros.append(random.randint(1,100))
    if numeros[x] % 2 == 0:
        print(f'Número {numeros[x]} é par')
        par += 1
    else:
        print(f'Número {numeros[x]} é impar')
        impar += 1

print(numeros)
print(f'A quantidade de números pares   é: {par}')
print(f'A quantidade de números impares é: {impar}')
