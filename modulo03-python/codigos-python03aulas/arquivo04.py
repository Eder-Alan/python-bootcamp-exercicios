# %%
var_arquivo = 'arquivoteste.txt'

# abrindo a arquivo
var_conteudo = open(var_arquivo, 'w+')
# escrevendo no arquivo, ele apaga tudo o arquivo para
# fazer uma unica escrita faça os testes.
var_linha = var_conteudo.write('mais uma linha de teste')
# fechando o arquivo é muito importante.
var_conteudo.close()

# abrindo o arquivo novamente agora apenas para leitura.
var_conteudo = open(var_arquivo, 'r')
# fazendo a leitura da linha do arquivo
var_linha = var_conteudo.read()
#imprimindo o conteúdo do arquivo
print(var_linha)

# fechando o arquivo muito importante não esquecer.
var_conteudo.close()