# ===============================
# Importação das bibliotecas
# ===============================

import os
import pandas as pd  # Biblioteca para manipulação e análise de dados (DataFrames)
import plotly.express as px  # Biblioteca para criação de gráficos interativos
import streamlit as st  # Biblioteca para criação de aplicativos web
# interativos em Python
# =================================================================

# ================================================================
# uma alternatica caso deseje colocar o projeto no github para
# rodar no site streamlit.
# ================================================================
# Importante: este trecho garante que o app funcione mesmo que
# seja executado em diretórios diferentes

# Garante o caminho completo até o arquivo 'consultas.csv',
# independentemente de onde o app for iniciado.
# __file__ -> caminho completo do arquivo Python atual
# os.path.dirname(__file__) -> diretório onde o script está
# os.path.join(...) -> une o diretório do script com o nome do arquivo CSV
csv_path = os.path.join(os.path.dirname(__file__), "consultas.csv")

# Verifica se o arquivo CSV existe no caminho informado
# Caso não exista, exibe uma mensagem de erro no Streamlit e interrompe a execução
if not os.path.exists(csv_path):
    st.error(f"Arquivo '{csv_path}' não encontrado. "
             f"Verifique se ele está no GitHub e tente recarregar o app.")
    st.stop()  # Interrompe a execução do app para evitar erros ao
    # tentar ler um arquivo inexistente
# =================================================================

# ===============================
# Configuração e exibição no Streamlit
# ===============================

# Define configurações iniciais da página do aplicativo Streamlit:
# - Título da aba do navegador
# - Layout "wide" para ocupar toda a largura da tela
st.set_page_config(page_title='Painel de Consultas Médicas', layout='wide')

# Demandas do cliente:
# 1 - Número de consultas geral e por dadas (selectbox) - gráfico de barras.
# 2 - Por unidades as consultas - especialidades - gráfico de barras.
# 3 -

# Lê o arquivo CSV e armazena os dados em um DataFrame do Pandas
# O parâmetro parse_dates converte automaticamente a coluna 'dataconsulta'
# para o formato de data/hora (datetime)
df = pd.read_csv(csv_path, parse_dates=['dataconsulta'])

# Combo das datas
# Cria uma lista de datas únicas presentes na coluna 'dataconsulta',
# formatando-as no padrão dia-mês-ano (ex.: '25-10-25').
# A função 'sorted()' organiza essas datas em ordem crescente para
# uso em seletores
# (ex.: menus ou filtros de data no Streamlit).
data_unicas = sorted(df['dataconsulta'].dt.strftime('%d-%m-%y').unique())

# Cria um seletor (selectbox) na barra lateral do Streamlit
# permitindo ao usuário escolher uma data ou a opção 'Todas'.
opcao_data = st.sidebar.selectbox('Selecione a Data:',options=['Todas'] + data_unicas)

# Combo das unidades
# Cria uma lista das unidades únicas presentes na coluna 'unidade',
# organizada em ordem alfabética com 'sorted()'.
unidade = sorted(df['unidade'].unique())

# Cria um seletor (selectbox) na barra lateral do Streamlit
# permitindo ao usuário escolher uma unidade específica ou a opção 'Todas'.
opcao_unidade = st.sidebar.selectbox('Selecione a Unidade:', options=['Todas'] + unidade)
# =================================================================

# Faz uma cópia do DataFrame original para aplicar filtros
df_filtrado = df.copy()

# =================================================================
# Aplicando filtro em dataconsulta

# Se o usuário selecionou uma data diferente de 'Todas' no selectbox...
# 1) df_filtrado['dataconsulta'] -> acessa a coluna 'dataconsulta'
# do DataFrame (uma Series de tipo datetime)
# 2) .dt.strftime('%d-%m-%y') -> usa o accessor .dt para aplicar
# strftime a cada valor de data,
# convertendo a data em uma string com o formato 'dia-mês-ano' (ex.: '25-10-25')
# 3) == opcao_data -> compara cada string de data com
# o valor selecionado (opcao_data)
# 4) df_filtrado[ ... ] -> filtra o DataFrame mantendo apenas as
# linhas cuja data, no formato string, é igual a opcao_data
if opcao_data != 'Todas':
    df_filtrado = df_filtrado[df_filtrado['dataconsulta'].dt.strftime('%d-%m-%y') == opcao_data]


# Aplicando filtro em unidades

# Se o usuário selecionou uma unidade específica diferente de 'Todas'
# no selectbox...
# df_filtrado['unidade'] == opcao_unidade -> cria uma Series booleana
# (True/False) indicando quais linhas têm o valor da coluna 'unidade'
# igual ao escolhido
# df_filtrado[ ... ] -> aplica essa máscara booleana ao DataFrame,
# retornando apenas as linhas cujo valor de 'unidade' bate com opcao_unidade
if opcao_unidade != 'Todas':
    df_filtrado = df_filtrado[df_filtrado['unidade'] == opcao_unidade]

# =================================================================
# ===============================
# Composição dos Gráficos
# ===============================
# Define o título principal do dashboard dentro do Streamlit
# Este título aparece no topo da página web.
st.title('📊 Painel de Consultas Medicas')

# ===============================================================
# Criando o filtro - Número de Consultas por Unidade
# ===============================================================

# Agrupa o DataFrame filtrado pela coluna 'unidade' e conta quantas
# linhas há em cada grupo.
# passo a passo:
# 1 df_filtrado.groupby('unidade')→ agrupa as linhas com base na unidade
# (ex.: "Centro", "Vila Nova", etc.)
# 2 .size() → conta o número de ocorrências (linhas) em cada grupo
# 3 .reset_index(name='Total') → transforma o resultado em um novo
# DataFrame com duas colunas:
# - 'unidade' → nome da unidade
# - 'Total'   → número total de consultas naquela unidade

consultas_unidade = df_filtrado.groupby('unidade').size().reset_index(name='Total')

# =================================================================
# criando duas colunas para os gráficos
col1, col2, col3 = st.columns(3)

# ===============================================================
# Criando o Gráfico - Número de Consultas por Unidade
# ===============================================================
# montagem do Gráfico 1 - Número de Consultas por Unidade
fig1 = px.bar(consultas_unidade,
              x='unidade',
              y='Total',
              color='unidade',
              title=f'🩺 Numero de Consultas por Unidades ({opcao_data})',
              text='Total'
              )
# fazendo um update de layout
fig1.update_layout(xaxis_title='Unidade', # trocando o nome do eixo X
                   yaxis_title='Total de Consultas')# trocando o nome do eixo Y

# chamando o gráfico
col1.plotly_chart(fig1, use_container_width=True)

# =========================================================================

# ===============================================================
# Criando o filtro - Número de consultas por especialidade
# ===============================================================

consultas_tipo = df_filtrado.groupby('tipoconsulta').size().reset_index(name='Total')

# =========================================================================
# montagem do gráfico 2 consulta por especialidade
fig2 = px.pie(
    consultas_tipo,
    values='Total',
    names='tipoconsulta',
    title=f'👨‍⚕️ Consultas por Especialidade ',
    color='tipoconsulta',  # mantém a cor por categoria
    hole=0.4,              # se quiser pizza "cheia" use use hole=0
                           # ou hole=0.4 para tipo "rosquinha"
)

# fazendo um update de layout
fig2.update_layout(xaxis_title='Total de consulta', # trocando o nome do eixo X
                   yaxis_title='Tipo da Consulta')  # trocando o nome do eixo Y

# chamando o gráfico
col2.plotly_chart(fig2, use_container_width=True)

# =========================================================================
# ===============================================================
# Criando o filtro - Faturamento por Unidade
# ===============================================================
# Este agrupamento tem como objetivo calcular o total de faturamento
# (soma dos valores) para cada unidade médica, com base nos dados
# já filtrados anteriormente unidade.
#
# Passo a passo:
# 1) df_filtrado.groupby('unidade', as_index=False)
#    → agrupa as linhas do DataFrame pela coluna 'unidade'
#      (ou seja, separa os registros de cada clínica/unidade).
#
# 2) ['valor'].sum()
#    → dentro de cada grupo, soma todos os valores da coluna 'valor',
#      resultando no total faturado por unidade.
#
# 3) as_index=False
#    → mantém 'unidade' como uma coluna normal (e não como índice),
#      o que facilita a criação de gráficos e exibições no Streamlit.
#
# Resultado final:
#    O DataFrame resultante (faturamento_unidade) terá duas colunas:
#    - 'unidade' → nome da unidade médica
#    - 'valor'   → total do faturamento daquela unidade
#
# Exemplo de saída:
#      unidade       valor
#   0  Centro       12000.00
#   1  Vila Nova     8700.00
#   2  Zona Sul     10450.00
#
faturamento_unidade = (df_filtrado.groupby('unidade', as_index=False)['valor'].sum())

# ===============================================================
# Criando o Gráfico - Número de Consultas por Unidade
# ===============================================================
# montagem do Gráfico 1 - Número de Consultas por Unidade
fig3 = px.bar(faturamento_unidade,
              x='unidade',
              y='valor',
              color='unidade',
              title=f'🥇 Faturamento Total por Unidade',
              text='valor'
              )
# fazendo um update de layout
fig3.update_layout(xaxis_title='Unidade', # trocando o nome do eixo X
                   yaxis_title='Total de Faturamento')# trocando o nome do eixo Y

# chamando o gráfico
col3.plotly_chart(fig3, use_container_width=True)

# =========================================================================


# =========================================================================
# Visão dos atendimentos
# criando um cabeçalho
st.subheader(f'📋 Registros: ({opcao_unidade})')
st.dataframe(df_filtrado, use_container_width=True)
# =========================================================================

# ===============================
# Execução do aplicativo Streamlit
# ===============================
# Para rodar o aplicativo, execute no terminal o comando abaixo:
# local do arquivo:
# cd C:\Users\user\pythonProject\Educ360\codigos-python06aulas
# depois:
# streamlit run dashboard2.py