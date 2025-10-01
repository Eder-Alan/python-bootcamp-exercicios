# Exercício: Inclusão e Inserção de Elementos
# Utilize a lista vendas do exercício anterior. Adicione o valor 500 ao final da
# lista e, em seguida, insira o valor 999
# na segunda posição (índice 1). Imprima a lista após as modificações.
vendas = [1,2,3,6]
print(f'Lista original: {vendas}')
print('\n==========================================')

# incluindo um valor de 500 no final de lista
vendas.append(500)

print(f'Após adicionar 500: {vendas}')
print('\n==========================================')

# inserindo um valor 999 na segunda posição
vendas.insert(1,999)
print(f'Após inserir 999 na posição 1: {vendas}')









