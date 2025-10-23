# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# MatPlotlib
# Obter dados do aluno via csv
#
# Fazer o tratamento (nulos, colunas)
#
# Gerar dados para montar gráficos (Barra, Pizza, Linha)
#
# ----------> Numero de Alunos por curso (Barra)
#
# ----------> Distribuição por desempenho (Pizza)
#
# ----------> Frequencia das notas por curos (Linha).
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# importando bibliotecas
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Importa a biblioteca Pandas (pd) para manipulação e análise de dados
# em tabelas (DataFrames)
import pandas as pd

# Importa o módulo pyplot da biblioteca Matplotlib (plt) para criação e
# visualização de gráficos
import matplotlib.pyplot as plt

# - Trabalha com arrays (matrizes) multidimensionais
# - Realiza operações matemáticas e estatísticas complexas
# - É muito mais rápida que listas comuns do Python
# - É base para pandas, matplotlib e outras bibliotecas
import numpy as np
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# funções
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def separador():
    print('=-'* 36)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


# Esta linha lê um arquivo CSV hospedado no GitHub.
# O parâmetro sep=';' indica que o separador usado é ponto e vírgula.
# O resultado é armazenado no DataFrame df.
# importando pelo python
caminho = ('C:\\Users\\user\\pythonProject\\Educ360\\alunos_cursos.csv')
# importante informar o separador ; ao ler o CSV:
df = pd.read_csv(caminho,sep=';')
#df = pd.read_csv('https://raw.githubusercontent.com/profivan-ai/cdb-Python/refs/heads/main/arquivos/alunos_cursos.csv', sep=';')

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
separador()
print(f'{"Inicio da aula 01 - Lendo e tratando dados":^50}')
separador()
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# mostra as primeiras 5 linhas
print('mostra as primeiras 5 linhas')
print(df.head())
separador()

# mostra as ultimas 5 linhas
print('mostra as ultimas 5 linhas')
print(df.tail())
separador()

# verificação as informacoes do df
print('verificação as informacoes do df')
print(df.info())
separador()

# fazendo a verificacao da existencia de nulos
print('fazendo a verificacao da existencia de nulos')
print(df.isnull().sum())
separador()

# o errors='ignore evita que o código quebre caso a coluna não exista.
df.drop('Projetos', axis=1, inplace=True, errors='ignore')
# df.drop(...)	Método do Pandas para remover rótulos (colunas ou linhas) de
# um DataFrame.
# 'Projeto'	O nome da coluna (ou linha, dependendo do axis) que você quer remover.
# axis=1	Define que você quer remover coluna. (axis=0 removeria linha)
# inplace=True	Faz a remoção diretamente no DataFrame original (df), sem
# precisar reatribuir (df = df.drop(...)). Se fosse False, o método retornaria
# uma cópia modificada sem alterar df.
# errors='ignore'	Se a coluna "Projeto" não existir, o Pandas não gera
# erro e apenas ignora. Sem isso, o Python lançaria KeyError.

#df.drop('Projetos', axis=1, inplace=True)

print(df.head())
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
separador()
print(f'{"Inicio da aula 02 - CriandoColunas":^50}')
separador()
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# df['Nota'] >= 7.5
# Cria uma série booleana (True/False) com base na condição:
# True → aluno com nota maior ou igual a 6 e Presença maior ou igual a 7.5
# False → aluno com nota menor que 6 e Presença menor que 7.5
# df['aprovado'] = ...
# Cria uma nova coluna chamada "aprovado" no DataFrame df.
# Cada linha recebe o resultado da condição (True ou False).
print('Criando uma nova coluna Aprovado \n'
      'condição: Nota  >= 7.5 e Presença >= 7.5')
df['Aprovado'] = (df['Nota'] >= 7.5) & (df['Presença'] >= 7.5)
print(df)
separador()

# criando uma nova função
def desempenho(nota):
    if nota >= 8:
        return 'alto'
    elif  nota >= 6:  # Notas entre 6 e 7.99
        return 'medio'
    else:
        return 'baixo'

# df['Desempenho']	Cria uma nova coluna chamada "Desempenho" no DataFrame df.
# df['Nota']	Seleciona a coluna "Nota" do DataFrame, que será usada como
# entrada para a função.
# .apply(desempenho)	Aplica a função desempenho em cada valor da coluna "Nota".
# desempenho	Função definida anteriormente, que retorna um valor
# categórico como "Alto", "Médio" ou "Baixo" com base na nota.
print('Cria uma nova coluna chamada "Desempenho"')
df['Desempenho'] = df['Nota'].apply(desempenho)
print(df)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
separador()
print(f'{"Inicio da aula 03 - Grafico_Barras":^50}')
separador()
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# df.groupby('Curso') Agrupa o DataFrame df pela coluna "Curso",
# criando grupos de linhas com o mesmo valor de curso.
# ['Nota']	Seleciona a coluna "Nota" dentro de cada grupo.
# .mean()	Calcula a média das notas em cada grupo (cada curso).
# media_notas = ...	Armazena o resultado em uma nova variável chamada media_notas.
# O resultado é uma Series do Pandas, onde o índice são os cursos e os valores
# são as médias das notas
# Reseta o índice do DataFrame resultante
# Transforma o índice atual (media_notas) em uma coluna normal
# Cria um novo índice numérico padrão (0,1,2,...).
print('Um filtro por grupo das disciplinas')
media_notas = df.groupby('Curso')['Nota'].mean().sort_values(ascending=False).reset_index()
print(media_notas)
separador()

# df.groupby('Curso')	Agrupa o DataFrame df pela coluna "Curso",
# criando grupos com o mesmo valor de curso.
# ['aprovado']	Seleciona a coluna "aprovado" dentro de cada grupo.
# .sum()	Soma os valores de "aprovado" dentro de cada grupo.
# Reseta o índice do DataFrame resultante
# Transforma o índice atual (aprov_curso) em uma coluna normal
# Cria um novo índice numérico padrão (0,1,2,...).
aprov_curso = df.groupby('Curso')['Aprovado'].sum().reset_index()
print(aprov_curso)


print('Criação de grafico de barras')
# df['Curso']	Seleciona a coluna "Curso" do DataFrame df.
# .value_counts()	Conta quantas vezes cada valor aparece na coluna, ou seja, o número de alunos por curso.
# .plot(...)	Cria um gráfico com base nos valores contados.
# kind='bar'	Define que o gráfico será de barras.
# color='red'	Define a cor das barras como vermelha.
# figsize=(10,5)	Define o tamanho do gráfico: largura 10, altura 5.
# title='Numero de Alunos por Curso'	Define o título do gráfico.
# xlabel='Cursos'	Define o rótulo do eixo X.
# ylabel='Alunos'	Define o rótulo do eixo Y.
# plt.show()	Exibe o gráfico gerado na tela
# plt.tight_layout() Ajusta o layout para que os textos não fiquem sobrepostos.
df['Curso'].value_counts().plot(
    kind='bar',
    color='skyblue',
    figsize=(10,5),
    title='Numero de Alunos por Curso',
    xlabel='Cursos',
    ylabel='Alunos')
plt.tight_layout()
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
separador()
print(f'{"Inicio da aula 04 - Grafico_Pizza":^50}')
separador()
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# df['Desempenho'] - Seleciona a coluna "Desempenho" do DataFrame df
# .value_counts() - Conta quantas vezes cada valor apareça na coluna
#                   (quantos alunos em cada categoria: alto, medio, baixo)
# .plot(...) - Cria um gráfico com base nos valores contados
# kind='pie' - Define que o gráfico será do tipo pizza (pie chart)
# figsize=(8,5) - Define o tamanho do gráfico
#                 8 = largura em polegadas
#                 5 = altura em polegadas
# title='Distribuição por desempenho' - Define o título do gráfico
# ylabel=None - Remove o rótulo do eixo Y (não é necessário em gráfico de pizza)
# autopct='%1.2f%%' - Exibe automaticamente o percentual em cada fatia
#                     %1.2f = número com 2 casas decimais
#                     %% = símbolo de percentual (%)
# plt.tight_layout() - Ajusta automaticamente o layout do gráfico
#                      para que os textos não fiquem sobrepostos ou cortados
# plt.show() - Exibe o gráfico na tela

print('Criação de grafico de Pizza')
df['Desempenho'].value_counts().plot(
    kind='pie',
    figsize=(8,5),
    title='Distribuição por desempenho',
    ylabel=None,
    autopct='%1.2f%%'
    )
plt.tight_layout()
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
separador()
print(f'{"Inicio da aula 05 - Grafico_Linhas":^50}')
separador()
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# df.groupby('Curso') - Agrupa o DataFrame df pela coluna "Curso"
#                        Cria grupos separados para cada curso
# ['Nota'] - Seleciona apenas a coluna "Nota" dentro de cada grupo
# .plot(...) - Cria um gráfico com base nos dados agrupados
# kind='line' - Define que o gráfico será do tipo linhas
#               Mostra a evolução/frequência das notas de cada curso
# legend=True - Exibe a legenda do gráfico
#               Mostra qual linha representa qual curso
# figsize=(8,5) - Define o tamanho do gráfico
#                 8 = largura em polegadas
#                 5 = altura em polegadas
# title='Frequencia das notas por cursos' - Define o título do gráfico
# xlabel='Cursos' - Define o rótulo do eixo X (horizontal)
#                   Identifica que o eixo mostra os cursos
# ylabel='Notas' - Define o rótulo do eixo Y (vertical)
#                  Identifica que o eixo mostra as notas
# plt.tight_layout() - Ajusta automaticamente o layout do gráfico
#                      para que os textos não fiquem sobrepostos ou cortados
# plt.show() - Exibe o gráfico na tela
print('Criando gráfico de linhas')
df.groupby('Curso')['Nota'].plot(
    kind='line',
    legend=True,
    figsize=(8,5),
    title='Frequencia das notas por cursos',
    xlabel='Cursos',
    ylabel='Notas'
)
plt.tight_layout()
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#  fazendo uma separação por curos.
print('fazendo uma separação por curos.')
print('Apenas do curso de Excel')
# fazendo uma separação por curos.
curso = 'Excel'
df[df['Curso'] == 'Excel'].plot(
    kind='line',
    legend=True,
    y='Nota',
    figsize=(8,5),
    title=f'Frequencia das notas do curso: {curso}',
    xlabel='Cursos',
    ylabel='Notas'
)
plt.tight_layout()
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
separador()
print(f'{"Inicio da aula 06 - Variaveis_produzidas":^50}')
separador()
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print('Criando um gráfico com o datafreme média_notas')
media_notas = df.groupby('Curso')['Nota'].mean().sort_values(ascending=False)
media_notas.plot(
    kind='bar',
    color='skyblue',
    figsize=(5,5),
    title='Media de notas por Curso',
    xlabel='Cursos',
    ylabel='Alunos')
plt.tight_layout()
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print('Uma pequena alteração no eixo y')
# Definir y_min e y_max
# Encontra o valor MÍNIMO da coluna "Nota" e armazena em y_min
y_min = df['Nota'].min()

# Encontra o valor MÁXIMO da coluna "Nota" e armazena em y_max
y_max = df['Nota'].max()

# Agrupa as notas por "Curso", calcula a média, ordena em ordem decrescente e transforma em DataFrame
media_notas = df.groupby('Curso')['Nota'].mean().sort_values(ascending=False).reset_index()

# Cria um gráfico de barras com os dados de media_notas e armazena o objeto em "ax"
ax = media_notas.plot(
    kind='bar', # Tipo de gráfico: barras
    color='skyblue',# Cor das barras: azul claro
    figsize=(8, 5),# Título do gráfico
    title='Media de notas por Curso',# Título do gráfico
    xlabel='Cursos',# Rótulo do eixo X
    ylabel='Nota')# Rótulo do eixo Y

# Define os valores que aparecem no eixo Y com intervalo de 0.25
# np.floor(y_min*2)/2: arredonda o mínimo para baixo até o múltiplo de 0.5
# np.ceil(y_max*2)/2 + 0.25: arredonda o máximo para cima até o múltiplo de 0.5 e adiciona 0.25
#ax.set_yticks(np.arange(np.floor(y_min * 2) / 2, np.ceil(y_max * 2) / 2 + 0.25, 0.25))
ax.set_ylim(y_min - 0.5, y_max + 0.5)
# Ajusta o layout do gráfico para evitar sobreposição de textos
plt.tight_layout()

# Exibe o gráfico na tela
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print('Um gráfico de linha')
media_notas = df.groupby('Curso')['Nota'].mean().sort_values(ascending=False).reset_index()
media_notas.plot(
    kind='line',
    color='skyblue',
    figsize=(8, 5),
    title='Media de notas por Curso',
    xlabel='Cursos',
    ylabel='Nota')

plt.tight_layout()
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print('Um grafico de pizza')

# Agrupa os dados por "Curso", soma os valores da coluna "Aprovado" (True/False convertidos em números)
# e transforma o resultado em um DataFrame com colunas "Curso" e "Aprovado"
aprov_curso = df.groupby('Curso')['Aprovado'].sum().reset_index()

# Cria um gráfico de pizza com os dados de aprov_curso
aprov_curso.plot(
    kind='pie',# Tipo de gráfico: pizza (pie chart)
    figsize=(8,5),# Tamanho do gráfico: 8 de largura, 5 de altura
    y='Aprovado',# Coluna que será usada para os valores das fatias
    labels=aprov_curso['Curso'],# Usa os nomes dos cursos como rótulos das fatias
    title='Distribuição por Aprovações',# Título do gráfico
    ylabel='', # Remove o rótulo do eixo Y (não é necessário em gráfico de pizza)
    autopct='%1.2f%%'# Exibe automaticamente o percentual em cada fatia com 2 casas decimais
    )
# Ajusta o layout do gráfico para evitar sobreposição de textos
plt.tight_layout()

# Exibe o gráfico na tela
plt.show()