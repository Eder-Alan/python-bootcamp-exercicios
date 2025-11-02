# ================================================================
# importação das biblioteca
# ================================================================
import os
import streamlit as st
import pandas as pd
import plotly.express as px

# ================================================================
# Garantindo o caminho correto do arquivo CSV
# ================================================================
csv_path = os.path.join(os.path.dirname(__file__), "consultas.csv")

# Verifica se o arquivo existe
if not os.path.exists(csv_path):
    st.error(f"Arquivo '{csv_path}' não encontrado. "
             f"Verifique se ele está no GitHub e tente recarregar o app.")
    st.stop()

# ================================================================
# Configuração inicial do app
# ================================================================
st.set_page_config(page_title='Painel de Consultas Médicas', layout='wide')

# ================================================================
# Leitura dos dados
# ================================================================
df = pd.read_csv(csv_path, parse_dates=['dataconsulta'])

# ================================================================
# Filtros - Data e Unidade
# ================================================================
data_unicas = sorted(df['dataconsulta'].dt.strftime('%d-%m-%y').unique())
opcao_data = st.sidebar.selectbox('Selecione a Data:', options=['Todas'] + data_unicas)

unidades = sorted(df['unidade'].unique())
opcao_unidade = st.sidebar.selectbox('Selecione a Unidade:', options=['Todas'] + unidades)

# Cria uma cópia do DataFrame para aplicar os filtros
df_filtrado = df.copy()

# Filtro de data
if opcao_data != 'Todas':
    df_filtrado = df_filtrado[df_filtrado['dataconsulta'].dt.strftime('%d-%m-%y') == opcao_data]

# Filtro de unidade
if opcao_unidade != 'Todas':
    df_filtrado = df_filtrado[df_filtrado['unidade'] == opcao_unidade]

# ================================================================
# CSS personalizado para modo escuro
# ================================================================
st.markdown("""
<style>

/* 🎨 ====== CONTAINER GERAL DO APLICATIVO ====== */
/* Este seletor pega o "corpo" principal da página do Streamlit */
[data-testid="stAppViewContainer"] {
    background-color: #0e1117;  /* Cor de fundo principal do app (preto-azulado escuro) */
    color: white;               /* Cor padrão do texto em toda a tela (branco) */
}

/* 💳 ====== ESTILO DOS CARDS DE RESUMO ====== */
/* Tudo que tiver class="card" (como seus resumos de total de consultas) 
   vai receber este estilo visual */
.card {
    background-color: #1f2630;  /* Cor de fundo do card (cinza escuro suave) */
    padding: 20px;              /* Espaçamento interno do conteúdo do card */
    border-radius: 10px;        /* Bordas arredondadas para deixar o card mais moderno */
    text-align: center;         /* Centraliza o texto dentro do card */
    color: #00ff99;             /* Cor do texto dentro dos cards (verde neon) */
    font-size: 20px;            /* Tamanho da fonte do conteúdo dos cards */
    margin: 5px;                /* Espaçamento entre os cards (externo) */
}

/* 🩵 ====== TÍTULOS PRINCIPAIS (h1, h2, h3) ====== */
/* Define a cor dos títulos usados em markdown ou HTML */
h1, h2, h3 {
    color: #00bfff;             /* Azul-ciano vibrante (destaque para títulos) */
}

/* 📋 ====== CONTAINER DAS TABELAS (DATAFRAMES) ====== */
/* Este seletor estiliza o fundo e o texto das tabelas mostradas com st.dataframe() */
[data-testid="stDataFrameContainer"] {
    background-color: #1f2630;  /* Fundo escuro igual ao dos cards (mantém harmonia) */
    color: white;               /* Texto das tabelas em branco para contraste */
}

</style>
""", unsafe_allow_html=True)

# ================================================================
# Cálculos e Resumos
# ================================================================
consultas_unidade = df_filtrado.groupby('unidade').size().reset_index(name='Total')

total_consultas = consultas_unidade['Total'].sum()
total_unidades = consultas_unidade['unidade'].nunique()
total_faturamento = df_filtrado['valor'].sum()

# ================================================================
# Cards de resumo
# ================================================================
st.title('📊 Painel de Consultas Médicas')

col1, col2, col3 = st.columns(3)
col1.markdown(f"<div class='card'>Total de Consultas<br><b>{total_consultas}</b></div>", unsafe_allow_html=True)
col2.markdown(f"<div class='card'>Unidades Ativas<br><b>{total_unidades}</b></div>", unsafe_allow_html=True)
col3.markdown(f"<div class='card'>Faturamento Total<br><b>R$ {total_faturamento:,.2f}</b></div>", unsafe_allow_html=True)

# ================================================================
# Preparação dos dados para os gráficos
# ================================================================
# Consultas por unidade
df_unidade = df_filtrado.groupby('unidade', as_index=False).size().rename(columns={'size': 'consultas'})

# Consultas por tipo de consulta (ex-"especialidade")
df_tipo = df_filtrado.groupby('tipoconsulta', as_index=False).size().rename(columns={'size': 'total'})

# Faturamento por unidade
df_faturamento = df_filtrado.groupby('unidade', as_index=False)['valor'].sum().rename(columns={'valor': 'faturamento'})

# ================================================================
# 📊 Exibição dos gráficos
# ================================================================
st.markdown("### 📅 Análise de Consultas e Faturamento")

col1, col2, col3 = st.columns(3)

# 1 Gráfico de barras - Consultas por unidade
fig1 = px.bar(df_unidade,
              x='unidade',
              y='consultas',
              color='unidade',
              text='consultas',
              title='🩺 Consultas por Unidade',
              color_discrete_sequence=['#00bfff', '#ff6347', '#32cd32']
              )

# fazendo um update de layout
fig1.update_layout(xaxis_title='Unidade', # trocando o nome do eixo X
                   yaxis_title='Total de Consultas')# trocando o nome do eixo Y

fig1.update_layout(plot_bgcolor='#0e1117', paper_bgcolor='#0e1117', font_color='white')
col1.plotly_chart(fig1, use_container_width=True)

# 2 Gráfico de pizza - Consultas por tipo de consulta
fig2 = px.pie(df_tipo,
              values='total',
              names='tipoconsulta',
              hole=0.4,
              title=f'👨‍⚕️ Consultas por Especialidade ',
              color_discrete_sequence=['#FFD700', '#FF69B4', '#8A2BE2', '#00CED1']
              )
# fazendo um update de layout


fig2.update_layout(plot_bgcolor='#0e1117', paper_bgcolor='#0e1117', font_color='white')
col2.plotly_chart(fig2, use_container_width=True)

# 3 Gráfico de barras - Faturamento por unidade
fig3 = px.bar(df_faturamento,
              x='unidade',
              y='faturamento',
              color='unidade',
              text=df_faturamento['faturamento'].apply(
                  lambda x: f"R${x:,.2f}"
                  .replace(",", "X").replace(".", ",").replace("X", ".")),
              title=f'🥇 Faturamento Total por Unidade',
              color_discrete_sequence=['#00FF7F', '#FF4500', '#1E90FF'] # Cores das barras
              )


# fazendo um update de layout
fig3.update_layout(xaxis_title='Unidade', # trocando o nome do eixo X
                   yaxis_title='Faturamento  (R$)')# trocando o nome do eixo Y

# Texto em R$ na horizontal
fig3.update_traces(
    textposition='outside',  # Texto acima das barras
    textangle=0,             # Mantém os textos na horizontal
    textfont_size=13
)

fig3.update_layout(plot_bgcolor='#0e1117', paper_bgcolor='#0e1117', font_color='white')
col3.plotly_chart(fig3, use_container_width=True)

# ================================================================
# Exibição da Tabela Filtrada
# ================================================================
st.markdown("### 📋 Dados Filtrados")
st.dataframe(df_filtrado)
# ================================================================


# ===============================
# Execução do aplicativo Streamlit
# ===============================
# Para rodar o aplicativo, execute no terminal o comando abaixo:
# local do arquivo:
# cd C:\Users\user\pythonProject\Educ360\codigos-python06aulas
# depois:
# streamlit run dashboard4_css.py