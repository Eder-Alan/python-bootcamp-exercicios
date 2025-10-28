# ============================================
# 🩺 LEITURA DO ARQUIVO CSV DE FORMA SEGURA NO STREAMLIT
# ============================================

# Importamos os módulos necessários:
# - os → para manipular caminhos de arquivos e pastas
# - pandas → para ler o CSV e criar o DataFrame
# - streamlit → para mostrar mensagens na tela e interromper o app se necessário
import os
import pandas as pd
import streamlit as st

# ============================================
# 🔍 CONSTRUÇÃO DO CAMINHO CORRETO PARA O CSV
# ============================================

# __file__ → representa o caminho completo deste arquivo Python (Dashboard.py)
# os.path.dirname(__file__) → pega apenas a pasta onde este arquivo está salvo
# os.path.join() → junta o caminho da pasta + o nome do arquivo 'consultas.csv'
# 
# Exemplo prático:
# Se o arquivo estiver em:
#   /app/python-bootcamp-exercicios/modulo06-python/codigos-python06aulas/Dashboard.py
# Então o caminho final do CSV será:
#   /app/python-bootcamp-exercicios/modulo06-python/codigos-python06aulas/consultas.csv
csv_path = os.path.join(os.path.dirname(__file__), "consultas.csv")

# ============================================
# ⚠️ VERIFICA SE O ARQUIVO EXISTE
# ============================================

# Antes de tentar ler, checamos se o arquivo realmente existe.
# Isso evita o erro "FileNotFoundError" e mostra uma mensagem amigável no app.
if not os.path.exists(csv_path):
    # Mostra o erro na interface do Streamlit
    st.error(f"Arquivo '{csv_path}' não encontrado. "
             "Verifique se ele está no GitHub e tente recarregar o app.")
    
    # Interrompe a execução do aplicativo para evitar falhas adiante
    st.stop()

# ============================================
# 📖 LEITURA DO ARQUIVO CSV
# ============================================

# Se o arquivo foi encontrado, fazemos a leitura normalmente.
# O parâmetro 'parse_dates' converte automaticamente a coluna 'dataconsulta'
# em formato de data (datetime) — ideal para gráficos e filtros.
df = pd.read_csv(csv_path, parse_dates=['dataconsulta'])

# ============================================
# ✅ PRONTO! O DataFrame 'df' agora está carregado com segurança
# ============================================

# A partir daqui, você pode continuar o código do seu dashboard normalmente:
# Exemplo:
st.success("✅ Arquivo 'consultas.csv' carregado com sucesso!")
st.dataframe(df.head())  # Mostra as primeiras linhas do CSV no Streamlit

# ============================================
# 📘 RESUMO DO QUE ESSE TRECHO FAZ
# ============================================
# 1️⃣ Garante que o app sempre encontre o CSV mesmo em subpastas;
# 2️⃣ Funciona no GitHub, no Streamlit Cloud e no seu computador local;
# 3️⃣ Evita travar o app com FileNotFoundError;
# 4️⃣ Mostra mensagens claras para o usuário.



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


# ===============================
# Composição dos Gráficos
# ===============================

# Define o título principal do dashboard dentro do Streamlit
# Este título aparece no topo da página web.
st.title('📊 Painel de Consultas Médicas')

# ===============================================================
# Gráfico 1 - Número de Consultas por Unidade
# ===============================================================

# Agrupa o DataFrame filtrado pela coluna 'unidade' e conta quantas linhas há em cada grupo.
# Explicação passo a passo:
# 1 df_filtrado.groupby('unidade')   → agrupa as linhas com base na unidade (ex.: "Centro", "Vila Nova", etc.)
# 2 .size()                          → conta o número de ocorrências (linhas) em cada grupo
# 3 .reset_index(name='Total')       → transforma o resultado em um novo DataFrame com duas colunas:
#                                         - 'unidade' → nome da unidade
#                                         - 'Total'   → número total de consultas naquela unidade
consultas_unidade = df_filtrado.groupby('unidade').size().reset_index(name='Total')

# Agora 'consultas_unidade' é um novo DataFrame que pode ser usado para gerar o gráfico.
# Exemplo de estrutura:
#   unidade        Total
#   -----------    -----
#   Centro          120
#   Vila Nova        85
#   Jardim Santos    47

# criando duas colunas para o gráfico
col1, col2 = st.columns(2)

# =========================================================================
# montagem do Gráfico 1 - Número de Consultas por Unidade
fig1 = px.bar(consultas_unidade,
              x='unidade',
              y='Total',
              color='unidade',
              title=f'Numero de Consultas por Unidades ({opcao_data})',
              text='Total'

              )


# fazendo um update de layout
fig1.update_layout(xaxis_title='Unidade', # trocando o nome do eixo X
                   yaxis_title='Total de Consultas')# trocando o nome do eixo Y

# chamando o gráfico
col1.plotly_chart(fig1, use_container_width=True)
# =========================================================================


consultas_tipo = df_filtrado.groupby('tipoconsulta').size().reset_index(name='Total')

# =========================================================================
# montagem do gráfico 2 consulta por especialidade
fig2 = px.bar(consultas_tipo,
              x='Total',
              y='tipoconsulta',
              color='tipoconsulta',
              title=f'Consultas por Especialidade ({opcao_data})',
              text='Total'

              )


# fazendo um update de layout
fig2.update_layout(xaxis_title='Total de consulta', # trocando o nome do eixo X
                   yaxis_title='Tipo da Consulta')# trocando o nome do eixo Y

# chamando o gráfico
col2.plotly_chart(fig2, use_container_width=True)
# =========================================================================

# Visão dos atendimentos

# criando um cabeçalho
st.subheader(f'📋 Registros: ({opcao_unidade})')
st.dataframe(df_filtrado, use_container_width=True)




# ===============================
# Configuração e exibição no Streamlit
# ===============================

# Define configurações iniciais da página do aplicativo Streamlit:
# - Título da aba do navegador
# - Layout "wide" para ocupar toda a largura da tela
st.set_page_config(page_title='Painel de Consultas Médicas', layout='wide')

# Define o título que aparecerá no topo do dashboard
st.title('Meu primeiro Dashboard')




# Exibe o DataFrame (tabela) na página web do Streamlit
df

# Exibe o DataFrame (tabela) na página web do Streamlit
print(df)

# Demandas do cliente
# 1 - Número de consultas geral e por datas (selectbox) - Barras
# 2 - Por unidade as consultas - dados -Especialidades


# ===============================
# Execução do aplicativo Streamlit
# ===============================
# Para rodar o aplicativo, execute no terminal o comando abaixo:
# streamlit run dashboard_streamlit.py


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
