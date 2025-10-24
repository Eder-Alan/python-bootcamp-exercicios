# %%

import os

var_arquivo = 'arquivotestes.txt'

if os.path.exists(var_arquivo):

    print('existe')
    var_conteudo = open(var_arquivo, 'a')
    var_adicionar = input('Digite o nome de uma aluno: ')
    var_adicionar = '\n' + var_adicionar

    var_conteudo.write(var_adicionar)
   
    var_conteudo.close()

    var_conteudo = open(var_arquivo, 'r')

    var_linha = var_conteudo.read()
    print(var_linha)
    
    var_conteudo.close()
    
else:
    print('não existe')
    # caso o arquivo não exista será feito tudo abaixo
    # ele será criado e aberto em modo de gravação.
    var_conteudo = open(var_arquivo, 'w')

    # será grava a seguinte informação abaixo.
    var_linha = var_conteudo.write('mais uma linha')
    # o arquivo será fechado 
    var_conteudo.close()

    # agora o arquivo será aberto para leitura.
    var_conteudo = open(var_arquivo, 'r')
    # lendo o conteudo.
    var_linha = var_conteudo.read()
    # impriminto o conteúdo na tela 
    print(var_linha)
    # fechando o conteúdo muito importante.
    var_conteudo.close()