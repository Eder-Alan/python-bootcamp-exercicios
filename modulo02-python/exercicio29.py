# Tuplas (Tuples)
# Tuplas são coleções ordenadas definidas por parênteses (). A principal
# característica é que elas são imutáveis, ou seja, não podem ser alteradas
# (você não pode usar .append(), por exemplo). Exercício: Acessando Elementos e
# Manipulando uma Lista Dentro da Tupla Crie uma tupla que contenha uma string,
# um número inteiro e, no terceiro elemento, uma lista de nomes.
# Acesse o primeiro nome dentro dessa lista.
# Acrescente o nome Felipe ao final da lista dos nomes.
# dados_empresa = ("Matriz 01", 2023, ["Alice", "Roberto", "Carla"]).

# Tupla com lista interna            # Lista interna é mutável
dados_empresa = ("Matriz 01", 2023, ["Alice", "Roberto", "Carla"])

# identificando o tipo da variável
print(type(dados_empresa))

# imprimindo os dados da tupla
print(dados_empresa)

# acessando o primerio nome da lista
print(dados_empresa[2][0])

# acrescentando o nome Felipe ao final da lista que está
# dentro de uma tupla.
dados_empresa[2].append('Felipe')

# acessando os nomes
print(dados_empresa[2])

# ============ exercicios adicionais para praticar e testar
# acessando os nomes
print(dados_empresa[2])

# utilizando o insert para inserir um nome em um local especifico
dados_empresa[2].insert(2,'Junior')

# acessando os nomes
print(dados_empresa[2])

# removendo dados de dentro de uma lista, no caso o primerio nome
# Alice.
dados_empresa[2].pop(0)

# acessando os nomes
print(dados_empresa[2])