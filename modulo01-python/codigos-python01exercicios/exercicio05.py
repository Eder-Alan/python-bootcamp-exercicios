# Assunto: Variaveis e Input
# - Declare uma variável chamada nome_cidade com o valor "São Paulo" e uma variável
# chamada temperatura com o valor 23.5. Em seguida, exiba o tipo de cada variável
# usando a função type().

nome_cidade = "São Paulo"
temperatura = 23.5

print(type(nome_cidade)) # do tipo str
print(type(temperatura)) # do tipo float

# ========= melhorias

nome_cidade = "São Paulo"
temperatura = 23.5

print(f"O tipo da variável nome_cidade é: {type(nome_cidade)}")  # str
print(f"O tipo da variável temperatura é: {type(temperatura)}")  # float
