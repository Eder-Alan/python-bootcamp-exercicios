# Exercício: Fatiamento com Passo (Step) e Inversão
# Utilize a lista numeros = [3,6,9,12,15]
# a) Extraia e imprima todos os números ímpares (começando do índice 0 e pulando de 2 em 2).
# b) Imprima a lista completa em ordem inversa.

numeros = [3,6,9,12,15]

# a) Extraia e imprima todos os números
# ímpares (começando do índice 0 e pulando de 2 em 2).
print(numeros[::2],'\n')

# b) Imprima a lista completa em ordem inversa.
print(numeros[-1::-1],'\n')
print('\n==========================================')


# para melhores prática
print(numeros[::-1],'\n')

# Considere a lista:
lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
#índices: 0    1    2    3    4    5    6
#negativ:-7   -6   -5   -4   -3   -2   -1

# Slice básico [start:stop]
#
# Inclui start, exclui stop.

print(lista[2:5])  # ['C', 'D', 'E']  (índices 2,3,4)
print(lista[:3])   # ['A', 'B', 'C']  (começa do início até índice 2)
print(lista[4:],'\n')   # ['E', 'F', 'G']  (do índice 4 até o fim)

# Slice com passo [start:stop:step]
#
# step>0 → anda para frente.
print(lista[::2])  # ['A', 'C', 'E', 'G']  (cada 2 elementos)
print(lista[1::2],'\n') # ['B', 'D', 'F']       (começando no índice 1)

# Slice inverso (step<0)
#
# step<0 → anda para trás (inverte a lista).
print(lista[::-1])    # ['G', 'F', 'E', 'D', 'C', 'B', 'A']  (toda invertida)
print(lista[-1::-1])  # ['G', 'F', 'E', 'D', 'C', 'B', 'A']  (mesma coisa, começando do último)
print(lista[5:2:-1],'\n')  # ['F', 'E', 'D']  (do índice 5 ao 3, exclusivo)

# Usando índices negativos.
print(lista[-3:])     # ['E', 'F', 'G']   (últimos 3 elementos)
print(lista[:-2])     # ['A', 'B', 'C', 'D', 'E']  (todos menos os 2 últimos)
print(lista[-1::-2])  # ['G', 'E', 'C', 'A']      (inverte e pula de 2 em 2)
