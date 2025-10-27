# ===============================
# Importação das bibliotecas
# ===============================

import pandas as pd                # Biblioteca para manipulação e análise de dados (DataFrames)
import plotly.express as px        # Biblioteca para criação de gráficos interativos
import streamlit as st             # Biblioteca para criação de aplicativos web interativos em Python


# ===============================
# Leitura do arquivo CSV
# ===============================

# Define o caminho completo do arquivo CSV que será lido
# O "r" antes da string indica que é uma *raw string* (sem necessidade de escapar as barras invertidas)
caminho = r'E:\não copiada\cursos\Curso Bootcamp Company.e e Educ360\módulo 03 Tilha Dados\vídeos\03 Phyton\Linguagem Python - Semana 6/consultas.csv'

# Lê o arquivo CSV e converte automaticamente a coluna 'dataconsulta' para o formato datetime.
# Isso permite realizar operações baseadas em data (como filtros, ordenação e gráficos de 
# série temporal).
df = pd.read_csv(caminho, parse_dates=['dataconsulta'])

# Combo das datas
# Cria uma lista de datas únicas presentes na coluna 'dataconsulta',
# formatando-as no padrão dia-mês-ano (ex.: '25-10-25').
# A função 'sorted()' organiza essas datas em ordem crescente para uso em seletores 
# (ex.: menus ou filtros de data no Streamlit).
datas_unicas = sorted(df['dataconsulta'].dt.strftime('%d-%m-%y').unique())
opcao_data = st.sidebar.selectbox('Selecione a data: ', options=['Todas'] + datas_unicas)


# Combo das unidades
unidades = sorted(df['unidade'].unique())
opcao_unidade = st.sidebar.selectbox('Selecione uma unidade: ', options=['Todas'] + unidades)


# fazendo uma cópia do dataframe
df_filtrado = df.copy()

# Aplicando filtros
if opcao_data != 'Todas':
    df_filtrado = df_filtrado[df_filtrado['dataconsulta'].dt.strftime('%d-%m-%y') == opcao_data]

if opcao_unidade != 'Todas':
    df_filtrado = df_filtrado[df_filtrado['unidade'] == opcao_unidade]


# composição dos gráficos
st.title('📊 Painel de Consultas Medicas')

# Gráfico 1 - Número de Consultas por Unidade
consultas_unidade = df_filtrado.groupby('unidade').size().reset_index(name='Total')

consultas_unidade








# ===============================
# Configuração e exibição no Streamlit
# ===============================

# Define configurações iniciais da página do aplicativo Streamlit:
# - Título da aba do navegador
# - Layout "wide" para ocupar toda a largura da tela
st.set_page_config(page_title='Painel de Consultas Médicas', layout='wide')

# Define o título que aparecerá no topo do dashboard


# Exibe o DataFrame (tabela) na página web do Streamlit
df


# Demandas do cliente
# 1 - Número de consultas geral e por datas (selectbox) - Barras
# 2 - Por unidade as consultas - dados -Especialidades
 

# ===============================
# Execução do aplicativo Streamlit
# ===============================
# Para rodar o aplicativo, execute no terminal o comando abaixo:
# streamlit run Dashboard.py
