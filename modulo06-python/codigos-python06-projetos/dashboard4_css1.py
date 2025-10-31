# ================================================================
# Importação das bibliotecas
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
opcao_data = st.sidebar.selectbox('🗓️ Selecione a Data:', options=['Todas'] + data_unicas)

unidades = sorted(df['unidade'].unique())
opcao_unidade = st.sidebar.selectbox('🏥 Selecione a Unidade:', options=['Todas'] + unidades)

# Cria uma cópia do DataFrame para aplicar os filtros
df_filtrado = df.copy()

# Filtro de data
if opcao_data != 'Todas':
    df_filtrado = df_filtrado[df_filtrado['dataconsulta'].dt.strftime('%d-%m-%y') == opcao_data]

# Filtro de unidade
if opcao_unidade != 'Todas':
    df_filtrado = df_filtrado[df_filtrado['unidade'] == opcao_unidade]

# ================================================================
# CSS personalizado - Modo Escuro Refinado
# ================================================================
st.markdown("""
<style>
/* ====== CORPO PRINCIPAL ====== */
[data-testid="stAppViewContainer"] {
    background-color: #0E1117;  /* fundo geral */
    color: #FFFFFF;             /* cor padrão do texto */
}

/* ====== SIDEBAR ====== */
[data-testid="stSidebar"] {
    background-color: #111827;  /* fundo lateral mais escuro */
    color: #FFFFFF;
}
[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* ====== CABEÇALHOS ====== */
h1, h2, h3 {
    color: #1E90FF;             /* azul destaque */
    font-weight: 600;
}

/* ====== CARDS ====== */
.card {
    background-color: #1E1E26;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    color: #00FFAA;
    font-size: 18px;
    margin: 5px;
    box-shadow: 0 0 8px rgba(0, 255, 170, 0.2);
    transition: 0.3s;
}
.card:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 12px rgba(0, 255, 170, 0.4);
}

/* ====== TABELA ====== */
[data-testid="stDataFrameContainer"] {
    background-color: #1F2630;
    color: #FFFFFF;
    border-radius: 10px;
    padding: 10px;
}

/* ====== AJUSTE DE BOTÕES ====== */
.stButton button {
    background-color: #00BFFF;
    color: #FFFFFF;
    border-radius: 8px;
    font-weight: bold;
}
.stButton button:hover {
    background-color: #0099CC;
}

/* ====== REMOVER BORDAS EXTERNAS ====== */
[data-testid="stDecoration"] {
    background: none;
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
df_unidade = df_filtrado.groupby('unidade', as_index=False).size().rename(columns={'size': 'consultas'})
df_tipo = df_filtrado.groupby('tipoconsulta', as_index=False).size().rename(columns={'size': 'total'})
df_faturamento = df_filtrado.groupby('unidade', as_index=False)['valor'].sum().rename(columns={'valor': 'faturamento'})

# ================================================================
# Exibição dos gráficos
# ================================================================
st.markdown("### 📅 Análise de Consultas e Faturamento")
col1, col2, col3 = st.columns(3)

# ====== Gráfico 1 ======
fig1 = px.bar(
    df_unidade,
    x='unidade', y='consultas', color='unidade',
    text='consultas',
    title='🩺 Consultas por Unidade',
    color_discrete_sequence=['#00BFFF', '#FF6347', '#32CD32']
)
fig1.update_traces(textposition='outside', textfont=dict(color='white', size=14))
fig1.update_layout(
    plot_bgcolor='#0E1117', paper_bgcolor='#0E1117',
    font_color='white',
    title_font=dict(color='white', size=22),
    xaxis_title='Unidade', yaxis_title='Total de Consultas'
)
col1.plotly_chart(fig1, use_container_width=True)

# ====== Gráfico 2 ======
fig2 = px.pie(
    df_tipo,
    values='total', names='tipoconsulta', hole=0.4,
    title='👨‍⚕️ Consultas por Especialidade',
    color_discrete_sequence=['#FFD700', '#FF69B4', '#8A2BE2', '#00CED1']
)
fig2.update_layout(
    plot_bgcolor='#0E1117', paper_bgcolor='#0E1117',
    font_color='white', title_font=dict(color='white', size=22)
)
col2.plotly_chart(fig2, use_container_width=True)

# ====== Gráfico 3 ======
fig3 = px.bar(
    df_faturamento,
    x='unidade', y='faturamento', color='unidade',
    text=df_faturamento['faturamento'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")),
    title='🥇 Faturamento Total por Unidade',
    color_discrete_sequence=['#00FF7F', '#FF4500', '#1E90FF']
)
fig3.update_traces(textposition='outside', textfont_size=13)
fig3.update_layout(
    plot_bgcolor='#0E1117', paper_bgcolor='#0E1117',
    font_color='white',
    title_font=dict(color='white', size=22),
    xaxis_title='Unidade', yaxis_title='Faturamento (R$)'
)
col3.plotly_chart(fig3, use_container_width=True)

# ================================================================
# Exibição da Tabela Filtrada
# ================================================================
st.markdown("### 📋 Dados Filtrados")
st.dataframe(df_filtrado, use_container_width=True)


# ===============================
# Execução do aplicativo Streamlit
# ===============================
# Para rodar o aplicativo, execute no terminal o comando abaixo:
# local do arquivo:
# cd C:\Users\user\pythonProject\Educ360\codigos-python06aulas
# depois:
# streamlit run dashboard4_css1.py