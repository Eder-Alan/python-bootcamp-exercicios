# %%
# ---------------- listas
dados = [10,40,20,25]
type(dados)
print(type(dados))
print(dados)
dados
print(dados[0])

for x in range(4):
    print(dados[x], end='  ')

print('\n')
print(dados[-1]) # buscando o ultimo elemento
   
# ---------------- Funções
# sum, max, min

print(f'A soma                é: {sum(dados)}')
print(f'O maior valor         é: {max(dados)}')
print(f'O menor valor         é: {min(dados)}')
print(f'A média dos valores   é: {sum(dados) / len(dados)}')
print(f'O tamanho da lista    é: {len(dados)} elementos')
print(f'A ordem dos elementos é: {sorted(dados)}')
# %%
