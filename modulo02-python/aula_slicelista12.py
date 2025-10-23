# %%
# ---------------- listas
linha = ['Ivan', 'Fábio', 'Zeca']
#imprime o primeiro elemento 'Ivan'
print(linha[0]) 
# imprime e lista toda.
print(linha)

# ------------uma lista dentro da outra
linha = ['Ivan', 
        [1970, 1994, 2002], 
        'Fábio', 
        'Zeca',
        [2001, 2002, 2004, 2005, 2010],
        [1,2,3,4,5,6,7,8,9]]

# assim retornará apena o nome Ivan
print(linha[0:1])

# assim retornará o nome e todos os anos
print(linha[2:5])

# linha[0:3] o zero significa o primeiro elemento e o segundo
# número significa o stop.

# um teste
print(linha[0:-4])

# criando uma lista de uma lista
anos = linha[4]
print(anos) 

copa = linha[1]
print(copa)

# o primeiro número é o star e o ultimo número
# é o stop.
print(anos[1:5])

# existe também o step ou o passo
numeros = linha[5]
# imprime todos os números da lista números
print(numeros[0:9:1])

# imprime só os números impares.
print(numeros[0:9:2])

# imprime só os números pares
print(numeros[1:9:2])

# imprime os números ao contrário
print(numeros[::-1])

# imprime os números ao contrário mas faltando
# um número por que??.
print(numeros[9:0:-1])

