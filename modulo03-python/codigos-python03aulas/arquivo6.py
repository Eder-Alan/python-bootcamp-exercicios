# %%
var_arquivo = 'arquivo.txt'


# é necessário uma variavel para conter o arquivo
# ou seja é um apontamento para o arquivo.
var_conteudo = open(var_arquivo,'r')
# aqui faz a impressão do conteúdo do arquivo
# com a função read().
#print(var_conteudo.read())

# o que pode ser feito, criar uma variável para
# receber o conteúdo e servir de parametro para a 
# função print, ao inves de fazer assim:
# print(var_conteudo.read()).
linhas = var_conteudo.read()
print(linhas)



 



# tipos de abertura de arquvi
# r  = read  -> apenas leitura
# w  = write -> faz a gravação e é utilizado para criar
#              o arquivo caso ele não exista.
# r+ = read + write -> ele lê e grava no arquivo ele
#                      adiciona no inicio do arquivo.
# 
# 
# 
# var_conteudo = open(var_arquivo,'w')
# muito cuidado com o comando acima se houver conteúdo no
# aquivo ele simplesmente será apagado!!!.