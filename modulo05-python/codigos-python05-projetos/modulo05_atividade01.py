# Atividade 01
# Você recebeu um arquivo vendas_loja.csv com informações de vendas de uma loja.
# O arquivo contém valores nulos e inconsistências em algumas colunas.
# Seu objetivo é:
#
# Ler o arquivo CSV.
#
# Tratar os valores nulos (preencher, remover ou substituir de forma lógica
# (trocar por média ,zero ou string ? você decide ).
#
# Gerar três gráficos usando somente matplotlib:
#
# • O Gráfico de Barras mostrando o total de vendas por categoria.
#
# • O Gráfico de Pizza mostrando a proporção de vendas por região.
#
# • O Gráfico de Linhas mostrando a evolução das vendas ao longo dos meses.
#
# Resultado Esperado:
# • O gráfico de barras mostra quais categorias geram mais receita.
#
# • O gráfico de pizza revela a distribuição de vendas por região.
#
# • O gráfico de linhas mostra tendências mensais, úteis para entender a
# sazonalidade.

# importando bibliotecas
# Importa a biblioteca pandas para manipulação e análise de dados (tabelas, CSVs, etc.)
import pandas as pd

# Importa a biblioteca matplotlib.pyplot para criação de gráficos e visualizações
import matplotlib.pyplot as plt

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# funções
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def separador():
    print('=-'* 36)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# lê um arquivo CSV hospedado no GitHub.
caminho = (r'C:\Users\user\pythonProject\Educ360\codigos-python05aulas/vendas_loja.csv')
df = pd.read_csv(caminho)

# fazendo as Análises básicas.
print('Imprimindo o data frame')
print(df)
# csv já está separado por vírgulas (,) — que é o padrão do formato CSV.
separador()

# Consultas Básicas
# algumas consultas básicas
# Exibe as 5 primeiras linhas do DataFrame (visualização inicial dos dados)
print('Exibe as 5 primeiras linhas do DataFrame (visualização inicial dos dados)')
print(df.head())
separador()

# Exibe as 5 últimas linhas do DataFrame (útil para ver o final da base)
print('Exibe as 5 últimas linhas do DataFrame (útil para ver o final da base)')
print(df.tail())
separador()

# Mostra informações gerais do DataFrame (colunas, tipos de dados e valores nulos)
print('Mostra informações gerais do DataFrame (colunas, tipos de dados e valores nulos)')
print(df.info())
separador()


# Verifica a quantidade de valores nulos (ausentes) em cada coluna do DataFrame
print('Verifica a quantidade de valores nulos (ausentes) em cada coluna do DataFrame')
print(df.isnull().sum())
# colunas a serem tratadas: Regiao e Vendas pois contém valores nulos
separador()

# Tratando dados da coluna Região.

# Preencher valores nulos de texto com 'Indefinida'
# rerirando nulo da coluna Regiao e substituindo por 'Indefinida'
df['Regiao'] = df['Regiao'].fillna('Indefinida')
# fazendo uma verificação na coluna Regiao
print('fazendo uma verificação na coluna Regiao')
print(df.isnull().sum() )
separador()

# Tratando dados da coluna Vendas.
# Preenchendo valores nulos numéricos com a 0 (zeros).
df['Vendas'] = df['Vendas'].fillna(0)
print('fazendo uma verificação')
# fazendo uma verificação
print(df.isnull().sum())
separador()

# Operações de soma e média.
# somando o total de vendas
total_vendas = df['Vendas'].sum()
print(f'O total da venda foi de: R$ '
      f'{total_vendas:,.2f}'.replace(',','X').replace('.',',').replace('X','.') )


# tirando a média de vandas
var_media = df['Vendas'].mean()
print(f'A média da vendas é de: R$ '
      f'{var_media:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))
separador()

# Gráfico de Barras.
# Agrupando e somando vendas por categoria
vendas_categoria = df.groupby('Categoria')['Vendas'].sum()

# Gráfico de Barras
print('Gráfico de Barras')
plt.figure(figsize=(7,4))
plt.bar(vendas_categoria.index, vendas_categoria.values, color='skyblue')
plt.title('Total de Vendas por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Vendas R$')
#plt.xticks(rotation=45) # ou com rotação de 45° neste caso ficou sem rotação
plt.tight_layout()
plt.show()
separador()

# Gráfico de Pizza
print('Gráfico de Pizza')
# Agrupando e somando vendas por região
vendas_regiao = df.groupby('Regiao')['Vendas'].sum()

plt.figure(figsize=(6,6))
plt.pie(vendas_regiao, labels=vendas_regiao.index, autopct='%1.1f%%', startangle=90)
plt.title('Proporção de Vendas por Região')
plt.show()
separador()

# ráfico de Linhas
print('Gráfico de Linhas')

# Agrupando vendas por mes
vendas_mes = df.groupby('Mes')['Vendas'].sum().sort_index()

plt.figure(figsize=(10,5))
plt.plot(vendas_mes.index, vendas_mes.values, marker='o', color='green')
plt.title('Evolução das Vendas ao Longo dos Meses')
plt.xlabel('Mês')
plt.ylabel('Total de Vendas R$')
plt.grid(True)
plt.tight_layout()
plt.show()
separador()







