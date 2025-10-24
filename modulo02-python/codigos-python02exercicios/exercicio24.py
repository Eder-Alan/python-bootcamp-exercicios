# Split
# A função split() é usada para quebrar uma string em uma lista de substrings,
# utilizando um separadorespecífico.
# Exercício: Você recebeu uma linha de dados de um arquivo CSV que lista nomes
# de países. Use a função split() para transformar a string registro_paises em
# uma lista, separando os nomes pela vírgula.
# registro_paises = "Brasil,Argentina,Chile,Uruguai,Paraguai".

registro_paises = "Brasil,Argentina,Chile,Uruguai,Paraguai"

paises = registro_paises.split(',')
print(paises)