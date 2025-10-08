# %%

var_arquivo = 'arquivostest.txt'

var_conteudo = open(var_arquivo, 'w')
# muito cuidado pois o comando acima grava no arquivo uma
# informação e apaga a informação anterior.
var_linha = var_conteudo.write('nova linha02')
# este programa irá gravar 'nova linha' no arquivo e apagará tudo
# o que estiver anteriormente.

var_conteudo.close()



# abaixo irei abrir o conteúdo novamente e fazer
# a leitura do mesmo.

# abrindo o arquivo
var_conteudo = open(var_arquivo, 'r')

# lendo o arquivo
var_linha = var_conteudo.read()

# fazendo o print na tela 
print(var_linha)

# e fechando o arquivo isso é muito 
# importante não esqueça.
var_conteudo.close()



