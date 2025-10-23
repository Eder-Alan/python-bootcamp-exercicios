# Atividade 02
# Você recebeu um arquivo pacientes_clinica.csv com dados de pacientes
# de uma clínica de saúde. O arquivo contém valores nulos e informações
# de idade, peso, pressão arterial e nível de glicose. Seu objetivo é:
#
# Ler o arquivo CSV.
#
# Tratar os valores nulos de forma adequada.
#
# Gerar os seguintes gráficos usando apenas matplotlib:
#
# • O Barras: média de glicose por faixa etária.
#
# • O Pizza: proporção de pacientes por gênero.
#
# • O Linhas: evolução média da pressão arterial por mês.
#
# Resultado esperado:
# • Faixas etárias mais altas tendem a apresentar glicose média maior.
#
# • A distribuição de gênero é visualizada de forma clara no gráfico de
# pizza.
#
# • O gráfico de linha permite acompanhar possíveis tendências mensais
# na pressão arterial média.

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


# Importa a biblioteca matplotlib.pyplot para criação de gráficos e visualizações
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\user\pythonProject\Educ360\codigos-python_atividades_aulas/pacientes.csv')

# fazendo as Análises básicas.
print('Imprimindo o data frame')
print(df)
separador()
# csv já está separado por vírgulas (,) — que é o padrão do formato CSV.


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

# Verificando os registros exatos da coluna Glicose consta como nulo.
print('Verificando os registros exatos da coluna Glicose consta como nulo.')
print(df[df['Glicose'].isnull()])
separador()

# Verificando a média da coluna Glicose
print('Verificando a média da coluna Glicose')
print(df['Glicose'].mean())
separador()

# Exemplo de uso do método copy().
# fazendo uma cópia do df para demonstração de valores nulos preenchidos com zeros.
df_copy = df.copy()
df_copy['Glicose'] = df_copy['Glicose'].fillna(0)
print('Verificando a média')
print(df_copy['Glicose'].mean())
separador()

# fazendo uma cópia do df para demonstração de valores nulos preenchidos com média.
df_copy1 = df.copy()
df_copy1['Glicose'] = df_copy1['Glicose'].fillna(df_copy1['Glicose'].mean())
print('Verificando a média')
print(df_copy1['Glicose'].mean())
separador()

# Tratando dados da coluna Glicose
# Preenchendo os valores nulos numéricos com a média.
# Preenchendo valores nulos numéricos com a média da coluna Glicose
df['Glicose'] = df['Glicose'].fillna(df['Glicose'].mean())
# fazendo uma verificação
print(df['Glicose'].mean())
separador()

# Verificando dados da coluna pressão.
# Verifica extamente todas as linhas que estão com valores nulos na coluna Pressão
print(df[df['Pressao'].isnull()])
separador()

# Preenchendo os valores nulos numéricos com a média.
df['Pressao'] = df['Pressao'].fillna(df['Pressao'].mean())
# fazendo uma verificação
print('fazendo uma verificação da média da coluna pressão')
print(df['Pressao'].mean())
separador()

# fazendo uma verificação
print('fazendo uma verificação dos dados tratados')
print(df.isnull().sum())
# todos os dados tratatos.
separador()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Função para classificar as idades em faixas etárias
def faixa_etaria(idade):
    """
    Classifica a idade informada em uma das seguintes faixas:
    - Até 30
    - 31 a 40
    - 41 a 50
    - 51 a 60
    - 61 ou mais
    """
    if idade <= 30:          # se a idade for menor ou igual a 30
        return 'Até 30'      # retorna a faixa 'Até 30'
    elif idade <= 40:        # se a idade estiver entre 31 e 40
        return '31 - 40'     # retorna a faixa '31 - 40'
    elif idade <= 50:        # se a idade estiver entre 41 e 50
        return '41 - 50'     # retorna a faixa '41 - 50'
    elif idade <= 60:        # se a idade estiver entre 51 e 60
        return '51 - 60'     # retorna a faixa '51 - 60'
    else:                    # se a idade for maior que 60
        return '61+'         # retorna a faixa '61+'

# Cria uma nova coluna 'faixa_etaria' no DataFrame aplicando a função a cada valor da coluna 'Idade'
df['faixa_etaria'] = df['Idade'].apply(faixa_etaria)

# Exibe as primeiras linhas do DataFrame atualizado para verificar a nova coluna
print(df.head())
separador()

# Gráfico de Barras.
# Calcula a média de glicose para cada faixa etária
media_clicose = df.groupby('faixa_etaria')['Glicose'].mean().sort_values()
media_clicose  # exibe o resultado da média por faixa etária

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print('Gráfico de Barras')
# Cria o gráfico de barras da média de glicose por faixa etária
plt.figure(figsize=(7,4))  # define o tamanho da figura
plt.bar(
    media_clicose.index,    # categorias no eixo X (faixas etárias)
    media_clicose.values,   # valores no eixo Y (média de glicose)
    color='lightgreen',     # cor de preenchimento das barras
    edgecolor='black',      # cor da borda das barras
    linewidth=0.5           # espessura da borda
)

plt.title('Média de Glicose por Faixa Etária')  # título do gráfico
plt.xlabel('Faixa Etária')                      # rótulo do eixo X
plt.ylabel('Glicose (mg/dl)')                   # rótulo do eixo Y

# Adiciona linhas de grade horizontais finas para facilitar a leitura
plt.grid(True, axis='y', linestyle='--', linewidth=0.4, color='gray', alpha=0.6)

#plt.xticks(rotation=45)  # opcional: rotaciona os rótulos do eixo X
plt.tight_layout()        # ajusta o layout para evitar cortes
plt.show()                # exibe o gráfico
separador()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Gráfico de pizza mostrando a proporção de pacientes por gênero
print('Gráfico de pizza ')
df['Genero'].value_counts().plot(
    kind='pie',                      # tipo de gráfico: pizza
    figsize=(5,5),                   # define o tamanho da figura
    title='Proporção de Pacientes por Gênero',  # título interno do gráfico
    ylabel='',                        # remove o rótulo do eixo Y
    autopct='%1.1f%%',               # exibe porcentagem com 1 casa decimal
    startangle=90                     # inicia o gráfico girado a 90° para melhor visualização
)

plt.title('Distribuição de Pacientes Por Gênero')  # título externo do gráfico
plt.show()  # exibe o gráfico
separador()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Gráfico de Linha
print('Gráfico de Linha')
# Definir a ordem correta dos meses
ordem_meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
               'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
df['Mes'] = pd.Categorical(df['Mes'], categories=ordem_meses, ordered=True)  # converte para categoria ordenada

# Agrupando por mês e calculando a média da pressão arterial
pressao_media_mes = df.groupby('Mes', observed=False)['Pressao'].mean().reset_index()
  # média de pressão por mês

# Gráfico de linha da evolução da pressão arterial
plt.figure(figsize=(10,5))  # define o tamanho da figura
plt.plot(
    pressao_media_mes['Mes'],      # eixo X (meses)
    pressao_media_mes['Pressao'],  # eixo Y (pressão média)
    color='green',                 # cor da linha
    marker='o',                    # marcador nos pontos
    linewidth=2                    # espessura da linha
)

plt.title('Evolução Média da Pressão Arterial por Mês')  # título do gráfico
plt.xlabel('Mês')                                        # rótulo do eixo X
plt.ylabel('Pressão Arterial (mmHg)')                    # rótulo do eixo Y

plt.grid(True, axis='y', linestyle='--', linewidth=0.4, color='gray', alpha=0.6)  # linhas de grade horizontais finas
plt.tight_layout()  # ajusta layout para não cortar elementos
plt.show()          # exibe o gráfico
separador()

