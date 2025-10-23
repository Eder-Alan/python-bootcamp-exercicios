# %%
# ---------------- listas
linha = ['Ivan', 'Fábio', 'Zeca']
#imprime o primeiro elemento 'Ivan'
print(linha[0]) 
# imprime e lista toda.
print(linha)

# ------------uma lista dentro da outra
linha = ['Ivan', [1970, 1994, 2002], 'Fábio', 'Zeca']

# como acessar os novos elementos?
print(linha[1])

# acessando o ano de 1994
print(linha[1][1])

# pode ser feito assim:
copas = linha[1]
print(copas)
print(type(copas))

# para pegar de linha o ultimo valor
print(linha[-1])

# alterando a lista para outros exercicios
linha = ['Ivan', [1970, 1994, 2002], 'Fábio', 'Zeca', [2001, 2002, 2004]]
# pegando o ultimo elemento da lista
print(linha[-1])

# agora pegando o ultimo elemento da lista e o primeiro elemento
# da sublista.
print(linha[-1][0])

# um teste o que acontecerá???
# imprime uma letra do primeiro indice, o primeiro indice
# é Ivan e a litra -2 é o penultimo caracter logo a letra 'a'.
print(linha[0][-2])

# e agora??
print(linha[0][1])
# imprime a letra v, o primeiro elemento da lista e a segunda
# letra do nome Ivan.


# ================conceito de inclusões
# e as inclusões ficam no final da lista.
# dados = [10]
# entrada = input('Digite um valor: ')
# dados.append(entrada)
# print(dados)

# ========== outra forma de fazer.
dados = [10, 20]
# inclui um dado no ultimo elemento
dados.append(int(input('Digite um número: ')))
print(dados)

# ================ agora inserção
# na posição 0 será inserido um número 50 
dados.insert(0,50)
print(dados)

# na posição 1 será inserido o número 45
dados.insert(1,45)
print(dados)

