# %%
var_arquivo = 'arquivoteste.txt'
# abrindo o arquivo, e se não houver ele cria um 
# arquivo.
var_conteudo = open(var_arquivo, 'a')
# inserindo um registro
var_linha = var_conteudo.write('\num deste de inserção')
# ira imprimir a quantidade de caracteres.
print(var_linha)
# fechando o arquivo
var_conteudo.close()


# abrindo o arquivo 
var_conteudo = open(var_arquivo, 'r')
# lendo o arquivo
var_linha = var_conteudo.read()
# imprimindo na tela
print(var_linha)
# fechando o arquivo
var_conteudo.close()