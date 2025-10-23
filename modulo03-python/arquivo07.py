# %%

import os
var_contador = 0
var_arquivo = 'arquivotestes.txt'

if os.path.exists(var_arquivo):
    with open(var_arquivo, 'r') as var_conteudo:
        for linha in var_conteudo:
            linha = linha.rstrip()

            if (linha == 'anderson'):
                print(f'O nome {linha} existe')
            print(linha)
            var_contador += 1
            

else: 
    with open(var_arquivo,'w') as var_conteudo:
         pass  # aqui o Python precisa de um bloco, 
               # mas não faremos nada

print(f'A quantidade de linha é de: {var_contador}')


# podemos transforma em uma tupla

var_tupla = tuple(open(var_arquivo, 'r'))
print(var_tupla)

with open(var_arquivo, 'r') as var_conteudo:
    linha_Tupla = tuple(linha.strip() for linha in var_conteudo)
    
print(linha_Tupla)
  
  

