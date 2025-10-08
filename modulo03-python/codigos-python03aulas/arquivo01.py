# %%
var_arquivo = 'arquivo.txt'

var_conteudo = open(var_arquivo, 'r')
var_linha = var_conteudo.read()
print(var_linha)

# as linhas de comando acima servem par ler um arquivo.
var_conteudo.close()
