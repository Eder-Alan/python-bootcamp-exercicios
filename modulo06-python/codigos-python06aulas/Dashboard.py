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
import plotly.express as px  # Adicionando a importação do Plotly Express

# Garante o caminho completo, independente de onde o app for iniciado
csv_path = os.path.join(os.path.dirname(__file__), "consultas.csv")

if not os.path.exists(csv_path):
    st.error(f"Arquivo '{csv_path}' não encontrado. Verifique se ele está no GitHub e tente recarregar o app.")
    st.stop()

df = pd.read_csv(csv_path, parse_dates=['dataconsulta'])

# Combo das datas
datas_unicas = sorted(df['dataconsulta'].dt.strftime('%d-%m-%y').unique())
opcao_data = st.sidebar.selectbox('Selecione a data: ', options=['Todas'] + datas_unicas)

# Combo das unidades
unidades = sorted(df['unidade'].unique())
opcao_unidade = st.sidebar.selectbox('Selecione uma unidade: ', options=['Todas'] + unidades)

# Fazendo uma cópia do dataframe
df_filtrado = df.copy()

# Aplicando filtros
if opcao_data != 'Todas':
    df_filtrado = df_filtrado[df_filtrado['dataconsulta'].dt.strftime('%d-%m-%y') == opcao_data]

if opcao_unidade != 'Todas':
    df_filtrado = df_filtrado[df_filtrado['unidade'] == opcao_unidade]

# ===============================
# Composição dos Gráficos
# ===============================

st.title('📊 Painel de Consultas Médicas')

# ===============================================================
# Gráfico 1 - Número de Consultas por Unidade
# ===============================================================

consultas_unidade = df_filtrado.groupby('unidade').size().reset_index(name='Total')

col1, col2 = st.columns(2)

# Gráfico 1
fig1 = px.bar(consultas_unidade,
              x='unidade',
              y='Total',
              color='unidade',
              title=f'Número de Consultas por Unidade ({opcao_data})',
              text='Total')

fig1.update_layout(xaxis_title='Unidade',
                   yaxis_title='Total de Consultas')

col1.plotly_chart(fig1, use_container_width=True)

# Gráfico 2 - Consultas por Especialidade
consultas_tipo = df_filtrado.groupby('tipoconsulta').size().reset_index(name='Total')

fig2 = px.bar(consultas_tipo,
              x='Total',
              y='tipoconsulta',
              color='tipoconsulta',
              title=f'Consultas por Especialidade ({opcao_data})',
              text='Total')

fig2.update_layout(xaxis_title='Total de Consultas',
                   yaxis_title='Tipo de Consulta')

col2.plotly_chart(fig2, use_container_width=True)

# Visão dos atendimentos
st.subheader(f'📋 Registros: ({opcao_unidade})')
st.dataframe(df_filtrado, use_container_width=True)

# ===============================
# Configuração e exibição no Streamlit
# ===============================

st.set_page_config(page_title='Painel de Consultas Médicas', layout='wide')
st.title('Meu primeiro Dashboard')

df  # Exibe o DataFrame na página web
