# Atividade 01
# Você recebeu um arquivo vendas_loja.csv com informações de vendas de uma loja.
# O arquivo contém valores nulos e inconsistências em algumas colunas. Seu objetivo é:
#
# Ler o arquivo CSV.
#
# Tratar os valores nulos (preencher, remover ou substituir de forma lógica
# (trocar por média ,zero ou string ? você decide ).
#
# Gerar três gráficos usando somente matplotlib:
# • O Gráfico de Barras mostrando o total de vendas por categoria.
# • O Gráfico de Pizza mostrando a proporção de vendas por região.
# • O Gráfico de Linhas mostrando a evolução das vendas ao longo dos meses.
# Resultado Esperado:
# • O gráfico de barras mostra quais categorias geram mais receita.
# • O gráfico de pizza revela a distribuição de vendas por região.
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

caminho = (r'C:\Users\user\pythonProject\Educ360\codigos-python05aulas/vendas_loja.csv')
df1 = pd.read_csv(caminho)

# Verificando os dados.

df1.isnull().sum()

print(df1.isnull().sum())
separador()

print('verificar exatamente onde os registros da coluna Vendas está com nulos')
# posso verificar exatamente onde os registros da coluna Vendas está com nulos
print(df1[df1['Vendas'].isnull()])
separador()

# Tratando dados da coluna Vendas
# Preenchendo os valores nulos numéricos com a média.

# Preenchendo valores nulos numéricos com a média
df1['Vendas'] = df1['Vendas'].fillna(df1['Vendas'].mean())

# fazendo uma verificação
print(df1.isnull().sum())
separador()

# Operações de soma e média
# fazendo a soma dos valores da coluna Vendas
var_soma = df1['Vendas'].sum()
print(f'A soma dos Valores é: R$ {var_soma:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))
separador()

# fazendo a média dos valores da coluna Vendas
var_media = df1['Vendas'].mean()
print(f'A média das vendas é: R$ {var_media:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))
separador()

print('Mostrando extamente todas as linhas que estão com valores nulos na coluna Região')
# mostrando extamente todas as linhas que estão com valores nulos na coluna Região
print(df1[df1['Regiao'].isnull()])
separador()

# Tratando dados da coluna Região.

# retirando todos os nulos da coluna Regiao e substituindo por 'Indefinida'
df1['Regiao'] = df1['Regiao'].fillna('Indefinida')

# fazendo uma verificação na coluna Regiao
print('fazendo uma verificação na coluna Regiao')
print(df1.isnull().sum())
separador()

# mostrando extamente todas as linhas que estavam com valores nulos e foram substituidos por 'Indefinida'
print('Mostrando extamente todas as linhas que estavam com valores nulos e '
      'foram substituidos por Indefinida')
print(df1[df1['Regiao'] == 'Indefinida'])
separador()

# Gráfico de Barras

# Agrupando e somando vendas por categoria
vendas_categoria = df1.groupby('Categoria')['Vendas'].sum()

# Gráfico de Barras
plt.figure(figsize=(7,4))
plt.bar(vendas_categoria.index, vendas_categoria.values, color='skyblue')
plt.title('Total de Vendas por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Vendas R$')
#plt.xticks(rotation=45) # ou com rotação de 45° neste caso ficou sem rotação
plt.tight_layout()
plt.show()
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Gráfico de Pizza
# Agrupando e somando vendas por região
vendas_regiao = df1.groupby('Regiao')['Vendas'].sum()

# Gráfico de Pizza
plt.figure(figsize=(6,6))
plt.pie(vendas_regiao, labels=vendas_regiao.index, autopct='%1.1f%%', startangle=90)
plt.title('Proporção de Vendas por Região')
plt.show()
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Convertendo a coluna 'Mes' para uma ordem lógica (Jan-Dez)
# Gráfico de Linhas.

# Converter a coluna 'Mes' para uma ordem lógica (Jan-Dez)
ordem_meses = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
df1['Mes'] = pd.Categorical(df1['Mes'], categories=ordem_meses, ordered=True)

# Agrupando vendas por mes
vendas_mes = df1.groupby('Mes')['Vendas'].sum().sort_index()

plt.figure(figsize=(10,5))
plt.plot(vendas_mes.index, vendas_mes.values, marker='o', color='green')
plt.title('Evolução das Vendas ao Longo dos Meses')
plt.xlabel('Mês')
plt.ylabel('Total de Vendas R$')
plt.grid(True)
plt.tight_layout()
plt.show()
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-























