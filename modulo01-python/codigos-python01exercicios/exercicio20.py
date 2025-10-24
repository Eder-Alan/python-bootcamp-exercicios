# Listas
# Listas em Python são coleções ordenadas e mutáveis, definidas por colchetes []
# Exercício: Crie uma lista chamada vendas contendo alguns valores.
# Calcule e imprima:
# a) A soma total dos valores.
# b) O maior e o menor valor.
# c) O número total de itens na lista.
# vendas=[1,2,3,6].


vendas = [1,2,3,6]
print(vendas)

print(f'A soma total das vendas foi de     : R${sum(vendas)}')
print(f'A maior venda foi a de             : R${max(vendas)}')
print(f'A quantidade total de vendas foi de: {len(vendas)}\n')
print('\n==========================================')


# exercitando um pouco mais.
vendas1 = [2.500, 3.500, 1.555, 7.521, 2.546, 9.451, 2.654, 5.987]
print(f"A soma total das vendas foi de     : R${sum(vendas1):.3f}")
print(f'A maior venda foi de               : R${max(vendas1):.3f}')
print(f'A menor venda foi de               : R${min(vendas1):.3f}')
media = sum(vendas1) / len(vendas1)
print(f"A média das vendas foi de          : R${media:.3f}")
print(f'A quantidade total de vendas foi de: {len(vendas1)}')