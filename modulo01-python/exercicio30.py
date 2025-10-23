# O objetivo desse exercicio é gerar um relatório (imagem exemplo abaixo) a
# partir da leitura do arquivo vendas.txt. Quando terminar insira o codigo no
# formulário e envie ao instrutor.
#
# O que você precisar usar : abertura de arquivo, strip, split, loops...e formatacao
# Dica: Para posicionar o texto use print(f"{nome:20} {depto:15}
# R$ {vendas_float:12,.2f}") # (.2f para milhar)
#
# Link para baixar o arquivo vendas.txt : O objetivo desse exercicio é gerar
# um relatório (imagem exemplo abaixo) a partir da leitura do arquivo vendas.txt.
# Quando terminar insira o codigo no formulário e envie ao instrutor.

# Define o nome do arquivo que contém os dados de vendas
var_arquivo = 'arquivovendas.txt'
# atribuindo um apelido para var_arquivo.
with open(var_arquivo, 'r', encoding='utf-8') as arquivo:

    linhas = [linha.strip().split(';') for linha in arquivo]

# Separando o cabeçalho (primeira linha) do restante dos dados
cabecalho = linhas[0]
dados = linhas[1:]  # Todas as linhas abaixo do cabeçalho (os registros de vendas)

var_total = 0.0

titulo = "Relatório de Vendas"

largura_total = 42

# Imprime o título centralizado com '=' preenchendo os lados
print(titulo.center(largura_total, '='))

# Larguras fixas para colunas
print(f'{cabecalho[0]:<10}  {cabecalho[1]:<12}  {cabecalho[2]:>12}')

# Linha de separação usando 42 traços
print('-' * 42)


for nome, dep, valor in dados:
    # Convertendo o valor da venda de string para float para permitir cálculos
    vendas_float = float(valor)

    print(f'{nome:<10}  {dep:<12} R${vendas_float:>12,.2f}')

    # Acumula o valor de vendas na variável total
    var_total += vendas_float


print('-' * 42)

print(f'{"Total":<23}  R$ {var_total:>12,.2f}')
print('=' * 42)
