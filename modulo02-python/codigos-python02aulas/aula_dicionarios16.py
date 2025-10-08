# =============dicionários
# %%
lista = ['Ivan', 'Denise', 12] # uma lista
dicio = {'Nome': 'Ivan',
         'Idade': 50,
         'Cidade': 'SP',
         'Linguagem':['Python', 'Cobol', 'PHP','Java'],
         'Cargos': [
             {'empresa:':'xpto', 
              'funcao'  :'programador'},
              {'empresa:':'abcd', 
              'funcao'  :'analista'},
              {'empresa:':'gpti', 
              'funcao'  :'gerente'}
         ]} # um dicionário


print(type(lista))
print(type(dicio))

# mostra tudo o que tem dentro de
#  dicionário
print(dicio) 

# mostra apenas o que tem na chave
# nome do dicionário.
print(dicio['Nome'])

# como substituir algo no dicionário
dicio['Nome'] = 'Silva'

# para percorrer a chave do
# dicionário.
for chave in dicio.keys():
    print(chave)
print('\n')

# para percorre os valores
for valores in dicio.values():
    print(valores)
print('\n')

# como procurar valores
if 'SP' in dicio.values():
    print('Encontrado')
else:
    print('Não encontrado')

# aqui é mostrado todas as linguagens
print(dicio['Linguagem'])

# aqui é mostrado a linguagem que eu
# quero
# [Python', 'Cobol', 'PHP', 'Java']
#    0         1       2       3.
print(dicio['Linguagem'][1])

# aqui estou acessando um dicionário
# que se econtra dentro da listas cargos.
print(dicio['Cargos'][-1]['funcao'])