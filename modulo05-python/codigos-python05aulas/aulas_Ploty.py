# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# importando bibliotecas
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# importa a biblioteca Plotly Express,
# usada para criar gráficos interativos de forma simples
import plotly.express as px

# módulo para controlar como os gráficos são exibidos
import plotly.io as pio

# Importa o módulo graph_objs do Plotly como 'go'
# graph_objs contém classes para criar gráficos de BAIXO NÍVEL (mais controle e customização)
# Diferente do plotly.express (px) que é alto nível e mais simples
# Usado para criar objetos gráficos personalizados como: go.Bar(), go.Scatter(), go.Pie(), etc.
import plotly.graph_objs as go

# Importa a biblioteca Pandas (pd) para manipulação e análise de dados
# em tabelas (DataFrames)
import pandas as pd

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# funções
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def separador():
    print('=-'* 36)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
separador()
print(f'{"Inicio da aula 01 - Ploty-Grafico_linhas":^50}')
separador()
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
pio.renderers.default = 'browser'  # define o navegador como destino de exibição (necessário fora do Colab)

# cria o gráfico
fig = px.line(x=[1,2,3,4],
              y=[10,20,12,40],
              title = 'Exemplo de gráfico de linha com Plotly'
              )         # título exibido no topo

#fig.show()  # exibe o gráfico em uma janela interativa (no navegador padrão)

#fig.show()  # exibe o gráfico (obrigatório no PyCharm)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
separador()
print(f'{"Inicio da aula 02 - Ploty-Grafico_linhas_CSV-Gapminder":^50}')
separador()
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

df = pd.read_csv(r'/gapminder2007.csv')

print('Imprimindo dados na tela')
print(df)
separador()

print('Imprimindo os primeiros 05 dados na tela')
print(df.head())
separador()

print('Imprimindo os ultimos 05 dados na tela')
print(df.tail())
separador()

print('Imprimindo as informações dos dados na tela')
print(df.info())
separador()


print('Imprimindo os primeiros 05 dados na tela')
# mostra estatísticas descritivas (média, min, max, quartis, etc.)
# das colunas numéricas do DataFrame
print(df.describe())
separador()

fig2 = px.line(df, x='country', y='lifeExp',title='Expectativa de vida')
#fig2.show() # exibe o gráfico (obrigatório no PyCharm)
fig2.show()


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
input('Pressione ENTER para continuar...')
# ------------------------------------------------------------
# 1 Carrega o conjunto de dados "gapminder" incluído no Plotly
#    Esse dataset contém informações históricas de países
#    como: população, expectativa de vida e PIB per capita.
# ------------------------------------------------------------
df = px.data.gapminder()

# ------------------------------------------------------------
# 2 Filtra o DataFrame para incluir apenas:
#     - países do continente "Americas"
#     - anos a partir de 2000
#     - países com população maior que 38 milhões
#    O método .query() permite aplicar filtros com sintaxe tipo SQL.
# ------------------------------------------------------------
df = df.query("continent == 'Americas' and year >= 2000 and pop > 38000000")

# ------------------------------------------------------------
# 3 Cria um gráfico de LINHA (line chart) com as seguintes configurações:
#     - x='year' → eixo X representa o ano
#     - y='lifeExp' → eixo Y representa a expectativa de vida
#     - title='Expectativa de vida' → título do gráfico
#     - color='country' → uma cor diferente para cada país
#     - text='pop' → exibe o valor da população próximo dos pontos no gráfico
#     - hover_name='pop' → mostra o valor da população ao passar o mouse (tooltip)
# ------------------------------------------------------------
fig3 = px.line(
    df,
    x='year',
    y='lifeExp',
    title='Expectativa de vida',
    color='country',
    text='pop',
    hover_name='pop'
)

# ------------------------------------------------------------
# 4 Exibe o gráfico interativo no navegador padrão
#    (abre em http://127.0.0.1:xxxx se estiver no PyCharm ou VSCode)
# ------------------------------------------------------------
fig3.show()


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
input('Pressione ENTER para continuar...')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
separador()
print(f'{"Inicio da aula 03 - Ploty-Grafico_linhas_CSV_ivan":^50}')
separador()
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

df = pd.read_csv(r'/viagens.csv', sep=';')
print(df)
separador()

print('Imprimindo os primeiros 05 dados na tela')
print(df.head())
separador()

print('Imprimindo os ultimos 05 dados na tela')
print(df.tail())
separador()

print('Imprimindo as informações dos dados na tela')
print(df.info())
separador()

# Agrupa por 'mes', calcula a média das colunas numéricas e
# redefine o índice para que 'mes' volte a ser coluna
df_meses = df.groupby(['mes'], sort=False).mean().reset_index()

# Exibe o DataFrame resultante com as médias por mês
print(df_meses)
separador()

print('Imprimindo um grafico de linhas')
separador()
# Cria um gráfico de linha (line chart) usando Plotly Express:
# - 'x' define o eixo horizontal como a coluna 'mes'
# - 'y' define o eixo vertical como a coluna 'viagens'
# - 'title' adiciona o título do gráfico: 'Média de Viagens por Mes'
# - 'color' diferencia as linhas por 'ano', atribuindo cores diferentes para cada ano
# - 'text' mostra os valores de 'viagens' diretamente sobre os pontos da linha
# Em seguida, exibe o gráfico com fig4.show()

fig4 =  px.line(df, x='mes', y='viagens', title='Média de Viagens por Mes', color='ano', text='viagens')
fig4.show()


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
input('Pressione ENTER para continuar...')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
separador()
print(f'{"Inicio da aula 04 - Ploty-Grafico_barras":^50}')
separador()
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

df = pd.read_csv(r'/compras.csv', sep=';')
print(df)

print('Imprimindo os primeiros 05 dados na tela')
print(df.head())
separador()

print('Imprimindo os ultimos 05 dados na tela')
print(df.tail())
separador()


print('Imprimindo as informações dos dados na tela')
print(df.info())
separador()


# Verifica a presença de valores nulos (missing values) no DataFrame 'df':
# - 'df.isnull()' retorna um DataFrame do mesmo tamanho, com True nos locais onde há valores nulos e False onde há dados preenchidos
# - '.sum()' soma os valores True em cada coluna (True é interpretado como 1), fornecendo a quantidade total de valores nulos por coluna
# - 'print()' exibe na tela o resultado, mostrando quantos valores faltantes existem em cada coluna do DataFrame
print('Verificando a presença de valores nulos')
print(df.isnull().sum())
separador()


print('Agrupando e contando o número de ocorrencias')
# Agrupa o DataFrame 'df' pela coluna 'dia' sem ordenar os grupos
df_dia = df.groupby('dia', sort=False)
# Conta o número de ocorrências em cada coluna para cada grupo de 'dia'
# - Cada valor representa quantas linhas têm dados não nulos naquela coluna para cada dia
# - Colunas com valores nulos são desconsideradas na contagem
print(df_dia.count())
separador()

print('Agrupando e somando a coluna de valores de cada dia')
# Agrupa o DataFrame 'df' pela coluna 'dia' sem ordenar os grupos
# Em seguida, aplica a função de agregação 'sum' apenas na coluna 'valor',
# somando todos os valores de cada dia
# Redefine o índice do DataFrame resultante para que 'dia' volte a ser
# uma coluna comum,
# em vez de permanecer como índice após o agrupamento
df_dia = df.groupby('dia', sort=False).agg({'valor': 'sum'}).reset_index()
# Exibe o DataFrame resultante, mostrando a soma de 'valor' para cada dia
print(df_dia)
separador()


print('Criando um gráfico de barras')
# Cria um gráfico de barras (bar chart) usando Plotly Express:
# - 'x' define o eixo horizontal como a coluna 'dia' (cada dia da semana)
# - 'y' define o eixo vertical como a coluna 'valor' (total de gastos por dia)
# - 'title' adiciona o título do gráfico: 'Gastos por dia da Semana'
# - 'color' aplica cores diferentes para cada dia, facilitando a distinção visual entre as barras
# Em seguida, exibe o gráfico com fig5.show()
fig5 = px.bar(df_dia, x='dia', y='valor', title=' Gastos por dia da Semana', color='dia')
fig5.show()


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
input('Pressione ENTER para continuar...')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
separador()
print(f'{"Inicio da aula 05 - Ploty-Grafico_barras_2":^50}')
separador()
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

print('Criando um gráfico de barras com dias da semana e por sexo')
# ===== PREPARAÇÃO DOS DADOS =====

# Garantir que a coluna 'sexo' seja do tipo string (texto)
# O .astype(str) converte qualquer valor para string
# O .str.strip() remove espaços em branco no início e fim dos valores
# Isso evita problemas como "M" ser diferente de "M " (com espaço)
df['sexo'] = df['sexo'].astype(str).str.strip()

# Garantir que a coluna 'valor' contenha apenas números
# pd.to_numeric() converte os valores para numérico
# errors='coerce' transforma valores inválidos em NaN (not a number) ao invés de dar erro
# Isso previne erros caso existam valores não numéricos na coluna
df['valor'] = pd.to_numeric(df['valor'], errors='coerce')


# ===== AGRUPAMENTO DOS DADOS =====

# Agrupar os dados por 'dia' e 'sexo' e somar os valores
# groupby(['dia', 'sexo']) - agrupa linhas que tenham o mesmo dia E mesmo sexo
# sort=False - mantém a ordem original dos dados (não ordena alfabeticamente)
# as_index=False - mantém 'dia' e 'sexo' como colunas normais (não como índice)
# ['valor'].sum() - soma todos os valores do grupo
# Resultado: uma linha para cada combinação única de dia + sexo, com o total de gastos
df_dia = df.groupby(['dia', 'sexo'], sort=False, as_index=False)['valor'].sum()


# ===== VERIFICAÇÃO DOS DADOS =====

# Exibe o DataFrame resultante no console para verificar se o agrupamento está correto
# Útil para debug e conferência dos dados antes de gerar o gráfico
print(df_dia)


# ===== CRIAÇÃO DO GRÁFICO =====

# Criar gráfico de barras usando Plotly Express
fig6 = px.bar(
    df_dia,                                      # DataFrame com os dados agrupados
    x='valor',                                     # Eixo X: dias da semana
    y='dia',                                   # Eixo Y: valores somados dos gastos
    title='Gastos por dia da Semana X (M/F)',   # Título do gráfico
    color='sexo',                                # Cor das barras baseada no sexo (M/F)
    barmode='group',                             # Barras agrupadas lado a lado (não empilhadas)
    text='valor'                                 # Exibe o valor numérico em cima de cada barra
)

# Exibir o gráfico interativo na tela
fig6.show()


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
input('Pressione ENTER para continuar...')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# fazer o desafio do professor momento: 5:20
# utilize esta base:
# df = pd.read_csv(r'C:\Users\user\pythonProject\Educ360\compras2.csv',sep=';')
# print(df) fazer isso no código abaixo.
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print('Criando um gráfico de barras com dias da semana e por sexo')
# ===== PREPARAÇÃO DOS DADOS =====

# Garantir que a coluna 'sexo' seja do tipo string (texto)
# O .astype(str) converte qualquer valor para string
# O .str.strip() remove espaços em branco no início e fim dos valores
# Isso evita problemas como "M" ser diferente de "M " (com espaço)
df['sexo'] = df['sexo'].astype(str).str.strip()

# Garantir que a coluna 'valor' contenha apenas números
# pd.to_numeric() converte os valores para numérico
# errors='coerce' transforma valores inválidos em NaN (not a number) ao invés de dar erro
# Isso previne erros caso existam valores não numéricos na coluna
df['valor'] = pd.to_numeric(df['valor'], errors='coerce')


# ===== AGRUPAMENTO DOS DADOS =====

# Agrupar os dados por 'dia' e 'sexo' e somar os valores
# groupby(['dia', 'sexo']) - agrupa linhas que tenham o mesmo dia E mesmo sexo
# sort=False - mantém a ordem original dos dados (não ordena alfabeticamente)
# as_index=False - mantém 'dia' e 'sexo' como colunas normais (não como índice)
# ['valor'].sum() - soma todos os valores do grupo
# Resultado: uma linha para cada combinação única de dia + sexo, com o total de gastos
df_dia = df.groupby(['dia', 'sexo'], sort=False, as_index=False)['valor'].sum()


# ===== VERIFICAÇÃO DOS DADOS =====

# Exibe o DataFrame resultante no console para verificar se o agrupamento está correto
# Útil para debug e conferência dos dados antes de gerar o gráfico
print(df_dia)


# ===== CRIAÇÃO DO GRÁFICO =====

# Criar gráfico de barras usando Plotly Express
fig6 = px.bar(
    df_dia,                                      # DataFrame com os dados agrupados
    y='dia',                                     # Eixo X: dias da semana
    x='valor',                                   # Eixo Y: valores somados dos gastos
    title='Gastos por dia da Semana X (M/F)',    # Título do gráfico
    color='sexo',                                # Cor das barras baseada no sexo (M/F)
    barmode='group',                             # Barras agrupadas lado a lado (não empilhadas)
    text='valor',                                # Exibe o valor numérico em cima de cada barra
    orientation='h', # Define a orientação do gráfico como HORIZONTAL
# 'h' = horizontal: as barras ficam deitadas (da esquerda para direita)
# 'v' = vertical (padrão): as barras ficam em pé (de baixo para cima)
# Útil quando os rótulos do eixo são longos ou quando você quer facilitar a leitura
    hover_name='valor'                           # Define qual informação aparece em DESTAQUE no tooltip (caixa de informações)
# Quando você passa o mouse sobre a barra, o valor aparece como título principal
# O hover (passar o mouse) mostra informações adicionais de forma interativa
# Neste caso, mostra o valor dos gastos em destaque ao passar o mouse
)

# Exibir o gráfico interativo na tela
fig6.show()


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
input('Pressione ENTER para continuar...')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
separador()
print(f'{"Inicio da aula 06 - Ploty-Grafico_Pizza":^50}')
separador()
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print('Criando um gráfico de Pizza')
# Agrupa dados por 'dia' e soma os valores, mantendo ordem original
df_agrupando_dia = df.groupby('dia', sort=False)['valor'].sum().reset_index()

# Cria gráfico de pizza (pie chart)
fig7 = px.pie(
    df_agrupando_dia,        # DataFrame com dados agrupados
    values='valor',          # Tamanho de cada fatia (proporção baseada no valor)
    names='dia',             # Rótulo de cada fatia (nome do dia)
    title='Gastos por Dia da Semana',  # Título do gráfico
    hover_name='valor',      # Destaca o valor ao passar o mouse
    opacity=0.8              # Transparência das fatias (0=invisível, 1=opaco)
)

# Exibe o gráfico
fig7.show()


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
input('Pressione ENTER para continuar...')
separador()

print('Criando um gráfico de Pizza com outros comandos')
# Agrupa dados por 'dia' e soma os valores, mantendo ordem original
df_agrupando_dia = df.groupby('dia', sort=False)['valor'].sum().reset_index()

# Cria gráfico de pizza (pie chart)
fig7 = px.pie(
    df_agrupando_dia,        # DataFrame com dados agrupados
    values='valor',          # Tamanho de cada fatia (proporção baseada no valor)
    names='dia',             # Rótulo de cada fatia (nome do dia)
    title='Gastos por Dia da Semana',  # Título do gráfico
    hover_name='valor',      # Destaca o valor ao passar o mouse
    color_discrete_sequence=px.colors.sequential.RdBu  # Paleta de cores sequencial (vermelho para azul)
)

# Exibe o gráfico
fig7.show()


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
input('Pressione ENTER para continuar...')
separador()


print('Um outro gráfico de Pizza bem bacana')
# Define os rótulos (nomes) de cada fatia do gráfico de pizza
labels = ['Oxygen', 'Hidrogen', 'Carbon_Dioxide', 'Nitrogen']

# Define os valores numéricos correspondentes a cada rótulo
# Determina o tamanho/proporção de cada fatia
values = [4500, 2500, 1053, 500]

# Cria figura usando Graph Objects (go) para maior controle
fig8 = go.Figure(
    data=[
        go.Pie(
            labels=labels,           # Nomes das fatias
            values=values,           # Valores de cada fatia
            pull=[0, 0, 0.2, 0]     # "Puxa" fatias para fora do centro
                                     # [0, 0, 0.2, 0] = apenas a 3ª fatia (Carbon_Dioxide) é destacada
                                     # 0 = fatia normal, 0.2 = fatia puxada 20% para fora
        )
    ]
)

# Exibe o gráfico
fig8.show()


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
input('Pressione ENTER para continuar...')
separador()

print('Um gráfico de Pizza muito diferente')
from ast import pattern  # Esta importação não é necessária, pode remover
import plotly.graph_objects as go

labels = ['Oxygen', 'Hidrogen', 'Carbon_Dioxide', 'Nitrogen']
values = [4500, 2500, 1053, 500]
colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']  # ❌ Era 'darkorang'

# Cria figura do gráfico de pizza
fig = go.Figure(  # ❌ Estava sem parênteses na mesma linha
    data=[
        go.Pie(
            labels=labels,           # Rótulos das fatias
            values=values,           # Valores de cada fatia
            textfont_size=20,        # Tamanho da fonte do texto nas fatias
            marker=dict(             # ❌ Era 'Mark' (maiúsculo errado)
                colors=colors,       # Cores personalizadas para cada fatia
                pattern=dict(        # Padrões de preenchimento (texturas)
                    shape=['.', 'x', '+', '-']  # ❌ Era shape[...] sem =
                )
            )
        )
    ]
)

# Exibe o gráfico
fig.show()


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
input('Pressione ENTER para continuar...')