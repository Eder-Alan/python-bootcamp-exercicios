# %%

a = 0
b = 4



try:
    a = 12 / a
# quando houver o erro capture este erro e 
# jogue na variável erro.
except Exception as erro:
    print(f'Erro na primeira tentativa {erro}')

# try e except pode ser utilizado de outra forma
# também.


try:
    a = 12 / a
except:
    a = 12 / b
    print(f'Outro resultado {a}')
try: 
    open ('dados1.txt')
except Exception as erroarqui:
    print(f'Erro na apertura do arquivo {erroarqui}')



