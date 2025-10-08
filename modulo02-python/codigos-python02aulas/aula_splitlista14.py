# ============split
# %%
linha = 'Olá, Ivan'

# split separa a variavel em uma lista o resultado
# ficará abaixo ['Olá', ' Ivan'].
lista = linha.split(',')
print(lista)

# 0 posição código
# 1 posição nome
# 2 posição saldo
# 3 posição endereço.

# não importa o tamanho do registro o que importa é estar 
# separado por ; .
registro = '0001; Silvio Santos; 1250.00; Lapa'
lista = registro.split(';')
print(lista)

# podemos fazer perguntas.
if float(lista[2]) >= 1000:
    print('Saldo suficiente')
else:
    print('Saldo não é suficiente')


