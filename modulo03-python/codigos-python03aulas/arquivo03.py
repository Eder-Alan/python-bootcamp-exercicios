# %%
var_arquivo = 'arquivostest.txt'

# abrindo o arquivo, o r+ adiciona dados no inicio
# do arquivo por cima do que já esteja escrito.
var_conteudo = open(var_arquivo,'r+')
# lendo o arquivo
var_linha = var_conteudo.write('baracadabraafafafafa')
 
var_conteudo.close()


var_conteudo = open(var_arquivo,'r')
var_linha = var_conteudo.read()
print(var_linha)



var_conteudo.close()




