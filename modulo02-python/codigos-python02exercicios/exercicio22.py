# Slices
# O fatiamento (slice) permite trabalhar com trechos ou subconjuntos da lista.
# A sintaxe é [start:stop:step]. Exercício:
# Dada a lista alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G'], utilize o
# fatiamento para extrair e imprimir uma sublista contendo apenas os elementos
# a partir do índice 2 até o índice 5 (exclusivo).
# alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G'].

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

letra = alfabeto
print(letra[2:5])
print('\n==========================================')

# ontra forma, pode ser direta
print(alfabeto[2:5])
print('\n==========================================')

# Relembrando a regra do slice
#
# lista[start:stop:step]
# start → índice inicial (inclusivo)
# stop → índice final (exclusivo)
# step → passo (de quantos em quantos anda).

# ========= exercitando um pouco
# utilizando o step também
# começando no 1 elemento
# indo até o ultimo
# e pulando de 2 em 2.
print(letra[1:7:2])

# forma simplificada
# utilizando o step também
# começando no 1 elemento
# indo até o ultimo
# e pulando de 2 em 2.
print(letra[1::2])

# desta forma irá mostrar tudo
print(letra[::])

# começa do primeiro elemento ou seja b
# vai até o ultimo e não existe o passo.
print(letra[1::])

# começa do 3 elemento ou seja o D
# vai até o 6 no caso o F
# não tem passo.
print(letra[3:6:])

# começa no elemento 0
# vai até o final
# o passo 3 em 3.
print(letra[::3])
