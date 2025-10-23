# %%


var_arquivo = 'teste.txt'

# abro o arquivo em modo de adicionar um elemento
conteudo = open(var_arquivo, 'a')

# adiciono o elemento que quero 
linha = conteudo.write('\nlinha adicional')

# fecho o arquivo
conteudo.close

# abro novamente o arquivo 
conteudo = open(var_arquivo, 'r')

# depois de aberto printo o conteúdo na tela
print(conteudo.read())

# fecho o arquivo novamente.
conteudo.close