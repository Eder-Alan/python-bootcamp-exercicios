# Define o nome do arquivo que contém os dados de vendas
var_arquivo = 'arquivovendas.txt'

# Abre o arquivo em modo leitura ('r') e com codificação UTF-8
# 'with' garante que o arquivo será fechado automaticamente após o bloco
with open(var_arquivo, 'r', encoding='utf-8') as arquivo:
    # Lê todas as linhas do arquivo
    # strip() remove espaços e quebras de linha (\n) do começo e fim
    # split(';') divide a linha em lista, separando pelos ';'
    # O resultado é uma lista de listas: cada linha vira uma lista de valores
    linhas = [linha.strip().split(';') for linha in arquivo]

# Separa o cabeçalho (primeira linha) do restante dos dados
cabecalho = linhas[0]  # Exemplo: ['Nome','Departamento','ValorVendas']
dados = linhas[1:]  # Todas as linhas abaixo do cabeçalho (os registros de vendas)

# Inicializa a variável que vai armazenar o total de vendas
var_total = 0.0

# Texto do título do relatório
titulo = "Relatório de Vendas"
# Largura total do relatório (usada para centralizar o título)
largura_total = 42

# Imprime o título centralizado com '=' preenchendo os lados
print(titulo.center(largura_total, '='))

# Larguras fixas para colunas (ajuste se quiser)
# <10 alinha à esquerda em 10 caracteres, <12 para o departamento, >12 para ValorVendas à direita
print(f'{cabecalho[0]:<10}  {cabecalho[1]:<12}  {cabecalho[2]:>12}')

# Linha de separação usando 42 traços
print('-' * 42)

# Loop para percorrer cada registro nos dados
for nome, dep, valor in dados:
    # Converte o valor da venda de string para float para permitir cálculos
    vendas_float = float(valor)

    # Imprime cada linha do relatório formatada
    # Nome e departamento alinhados à esquerda, valor alinhado à direita
    # :, adiciona separador de milhar e .2f garante duas casas decimais
    print(f'{nome:<10}  {dep:<12} R$ {vendas_float:>12,.2f}')

    # Acumula o valor de vendas na variável total
    var_total += vendas_float

# Linha de separação antes do total
print('-' * 42)

# Imprime o total das vendas
# "Total" alinhado à esquerda em 23 caracteres, valor alinhado à direita com separador de milhar
print(f'{"Total":<23}  R$ {var_total:>12,.2f}')

# Linha final de fechamento do relatório
print('=' * 42,'\n\n')
# ========================================================================
# ================ utilizando a função tabulate
# ========================================================================
# Modo “com bibliotecas” (usando a biblioteca tabulate)
#
# Se você quiser um visual mais elegante, pode usar a biblioteca
# tabulate, que cria tabelas prontas:.

from tabulate import tabulate
# Importa a biblioteca 'tabulate', que permite criar tabelas bonitinhas no terminal.
# Ela formata listas de listas ou listas de dicionários em tabelas com várias opções de estilo.

# Lê o arquivo e transforma em lista de listas
with open(var_arquivo, 'r', encoding='utf-8') as arquivo:
    # 'with' garante que o arquivo será fechado automaticamente após o bloco
    # 'arquivo' é a variável que representa o arquivo aberto
    # List comprehension:
    # - linha.strip() remove espaços extras e quebras de linha (\n)
    # - split(';') separa cada linha em uma lista de valores pelo delimitador ';'
    # O resultado é uma lista de listas, onde cada sublista representa uma linha do arquivo
    linhas = [linha.strip().split(';') for linha in arquivo]

# Separa o cabeçalho (primeira linha) do restante dos dados
cabecalho = linhas[0]  # Contém os nomes das colunas, por exemplo: ['Nome', 'Departamento', 'ValorVendas']
dados = linhas[1:]      # Contém os registros reais (os dados de vendas)

# Calcula o total das vendas
# Percorre cada registro em 'dados', pega a terceira coluna (valor de vendas),
# converte para float e soma todos
var_total = sum(float(valor[2]) for valor in dados)

# Adiciona uma linha extra para o total
# A linha contém:
# - 'Total' na coluna de Nome
# - '' (vazio) na coluna de Departamento
# - var_total na coluna ValorVendas, formatado com 2 casas decimais
dados.append(['Total', '', f'{var_total:.2f}'])

# Texto do título do relatório
titulo = "Relatório de Vendas"
# Largura total usada para centralizar o título
largura_total = 46

# Imprime o título centralizado
# center(largura_total, '=') centraliza o texto e preenche os espaços com '='
print(titulo.center(largura_total, '='))  # Exemplo de saída: ====Relatório de Vendas====

# Imprime a tabela usando tabulate
# - dados: lista de listas com todos os registros e a linha de total
# - headers=cabecalho: usa a primeira linha como cabeçalho da tabela
# - tablefmt='fancy_grid': estilo de tabela com bordas
# - floatfmt=".2f": formata números de ponto flutuante com 2 casas decimais
print(tabulate(dados, headers=cabecalho, tablefmt='fancy_grid', floatfmt=".2f"))

# Linha final de fechamento do relatório usando '=' repetido
print('='*46)  # Cria uma linha visual igual ao título, para deixar o relatório mais organizado

# Observações detalhadas
#
# with open(...) as arquivo: → garante fechamento automático do arquivo;
# evita problemas com arquivos abertos acidentalmente.
#
# linha.strip() → remove espaços e quebras de linha; essencial para
# limpar os dados.
#
# linha.split(';') → transforma cada linha em lista de colunas.
#
# sum(float(valor[2]) for valor in dados) → soma todos os valores da
# terceira coluna (ValorVendas).
#
# dados.append(['Total', '', f'{var_total:.2f}']) → adiciona uma linha
# final de total.
#
# titulo.center(largura_total, '=') → centraliza e cria efeito visual.
#
# tabulate(...) → gera tabela bonita com bordas e alinhamento automático.
#
# floatfmt=".2f" → garante que todos os valores numéricos aparecem com
# duas casas decimais.
# ========================================================================