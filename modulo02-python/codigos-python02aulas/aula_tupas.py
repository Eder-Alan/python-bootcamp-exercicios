# %%
# ============== tuplas

dados_lista = [50, 'Ivan', 'SP'] # Esta é uma lista

dados_tupla = (50, 'Ivan', 'SP') # Esta é uma tupla



print(type(dados_lista))
print(type(dados_tupla))

# uma tupla é imutavel não é possivel adicionar elementos
# abaixo dará erro pois não é possível altera-los
# dados_tupla[0] = 49

# mas se um dos itens da tupla for uma lista por exemplo:

# Esta é uma tupla mas com uma lista dentro dela ai já da para 
# inserir elementos dentro desta lista.
dados_tupla = (50, 'Ivan', 'SP',['Rj','BA']) 

print(dados_tupla[3])
dados_tupla[3].append('PE')
print(dados_tupla)
