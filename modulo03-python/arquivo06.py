# %%
# é possível ler arquivos em txt também
#Var_arquivo = 'arquivoteste.txt'
# var_arquivo contem uma imagem
Var_arquivo = 'testedeimagem.jpeg'

# abrindo um arquivo binario para leitura, deve-se
# escrever assim: rb se não não da certo.
Var_conteudo = open(Var_arquivo, 'rb')

# lendo o arquivo
var_linha = Var_conteudo.read()

# imprimindo na tela
print(var_linha)

# e fechanco o arquivo
Var_conteudo.close()

