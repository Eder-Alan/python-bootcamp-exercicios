import pandas as pd
import plotly.express as px
import streamlit as st


# ============================
# CONFIGURAÇÕES INICIAIS
# ============================

st.set_page_config(page_title="Atlântico Digital Streamlit", layout="wide")

# cor de fundo
st.markdown("""
    <style>
        .stApp {
            background-color: #e0e0e0 !important;
        }
    </style>
""", unsafe_allow_html=True)

# ===========================================
# SIDEBAR – UPLOAD DO ARQUIVO
# ===========================================

st.sidebar.header("📂 Carregar Arquivo")
uploaded_file = st.sidebar.file_uploader("⬅️ Envie um Arquivo Excel", type=["xlsx", "xls"])

# ===========================================
# SE NÃO HOUVER ARQUIVO → MOSTRA O LOGO
# ===========================================

if not uploaded_file:
    st.markdown("""
        <div style='display: flex; justify-content: center;'>
    """, unsafe_allow_html=True)

    st.image("log_da_Atlantico_digital.png", width=800)


    st.markdown("</div>", unsafe_allow_html=True)

    st.stop()

# ==== DAQUI PARA BAIXO SÓ EXECUTA SE O ARQUIVO EXISTE ====

st.markdown("""
<style>
h1 {
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Atlântico Digital")

# camada bronze
df = pd.read_excel(uploaded_file)
df_copy = df.copy()

# camada prata: renomear colunas
df_copy.columns = [f"col{i}" for i in range(1, len(df.columns)+1)]

mapa_colunas = {
    "col2": "cliente",
    "col4": "projeto",
    "col7": "tipo_de_tarefa",
    "col8": "equipe",
    "col10": "responsavel",
    "col13": "urgente",
    "col15": "aberta_por",
    "col16": "criada_em",
    "col17": "entrega_desejada",
    "col19": "fechada_em",
    "col20": "esforco_estimado",
    "col22": "ja_registrada_h",
    "col24": "porcentagem_tarefa_concluida",
    "col25": "etapa",
    "col26": "fase",
    "col27": "reaberta",
}
df_copy = df_copy.rename(columns=mapa_colunas)

# dropando as linas das datas que não foram preenchidas
df_copy = df_copy.dropna(subset=["criada_em", "entrega_desejada", "fechada_em"])

# camada ouro - cards e pré-processamento
total_registros = df_copy["tipo_de_tarefa"].count()
total_clientes = df_copy["cliente"].nunique()

# converter datas
df_copy["criada_em"] = pd.to_datetime(df_copy["criada_em"], errors="coerce")
df_copy["fechada_em"] = pd.to_datetime(df_copy["fechada_em"], errors="coerce")
df_copy["entrega_desejada"] = pd.to_datetime(df_copy["entrega_desejada"], errors="coerce")

df_copy["duracao_dias"] = (df_copy["fechada_em"] - df_copy["criada_em"]).dt.days
tempo_medio = df_copy["duracao_dias"].mean()

menor_data = df_copy["criada_em"].dt.date.min()
maior_data = df_copy["criada_em"].dt.date.max()

def metric_card(titulo, valor):
    tema = st.get_option("theme.base")
    if tema == "light":
        bg_color = "#FFFFFF"
        text_color = "#000000"
        label_color = "#555555"
    else:
        bg_color = "#e0e0e0"
        text_color = "#050404"
        label_color = "#0D0A0A"

    st.markdown(f"""
        <div style="
            padding:15px;
            border:3px solid #007BFF;
            border-radius:20px;
            text-align:center;
            width:100%;
            background-color:{bg_color};
        ">
            <div style="font-size:16px; color:{label_color};">{titulo}</div>
            <div style="font-size:32px; font-weight:bold; color:{text_color};">{valor}</div>
        </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
st.markdown("<br>", unsafe_allow_html=True)
with col1: metric_card("📋 Total de Ocorrências", total_registros)
with col2: metric_card("⬇️📅 Menor Data", menor_data.strftime("%d/%m/%Y") if pd.notnull(menor_data) else "-")
with col3: metric_card("⬆️📅 Maior Data", maior_data.strftime("%d/%m/%Y") if pd.notnull(maior_data) else "-")

st.markdown("""
    <style>
        /* Força a cor do label dos inputs (inclui selectbox) */
        .st-emotion-cache-0 h3, 
        .st-emotion-cache-0 label, 
        label[data-baseweb="select"] {
            color: #000000 !important;
            font-weight: bold !important;
            opacity: 1 !important;
        }
        div[role="radiogroup"] > label,
        div[class*="stSelectbox"] label {
            color: #000000 !important;
            font-weight: bold !important;
        }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown("### 📊 Selecione a Análise")
opcao = st.sidebar.radio(
    "Escolha:",
    [
        "Sem Visualização",
        "Tarefas Reabertas",
        "Tempo Médio por Tarefas Realizadas",
        "Esforço Tarefas Concluidas <= 100%",
        "Esforço Tarefas Concluidas >= 100%",
        "Tempo Total por Tarefas Realizadas"
    ]
)

# =========================
# Bloco: Tarefas Reabertas
# =========================
percentual_reabertas = round((df_copy["reaberta"] == "Sim").mean() * 100, 2)
contagem = df_copy["reaberta"].value_counts().reset_index()
contagem.columns = ["reaberta", "quantidade"]

fig0 = px.pie(
    contagem,
    names="reaberta",
    values="quantidade",
    title="Tarefas Reabertas",
    hole=0.5
)

# Preparar df_reabertas (split/explode responsáveis)
df_reabertas = df_copy[df_copy["reaberta"].astype(str).str.upper() == "SIM"].copy()
df_reabertas["responsavel"] = df_reabertas["responsavel"].astype(str).str.split(",")
df_reabertas = df_reabertas.explode("responsavel")
df_reabertas["responsavel"] = df_reabertas["responsavel"].str.strip()
df_reabertas["tipo_de_tarefa"] = df_reabertas["tipo_de_tarefa"].astype(str).str.strip()

df_responsavel = (
    df_reabertas
    .groupby(["responsavel", "tipo_de_tarefa"])
    .size()
    .reset_index(name="tarefas_reabertas")
    .sort_values(by=["responsavel", "tarefas_reabertas"], ascending=[True, False])
)

fig1 = px.bar(
    df_responsavel.groupby("responsavel", as_index=False)["tarefas_reabertas"].sum().sort_values("tarefas_reabertas", ascending=False),
    x="tarefas_reabertas",
    y="responsavel",
    title="Quantidade de Tarefas Reabertas por Responsável",
    color="responsavel",
    text="tarefas_reabertas"
)
fig1.update_traces(textposition="outside")
fig1.update_layout(xaxis_title="Qtde de Tarefas Reabertas", yaxis_title="Responsável", showlegend=False)

# =========================
# Bloco: Tempo Médio por Tipo de Tarefa
# =========================
# calcular tempo em dias entre fechada_em e entrega_desejada
df_copy["tempo_entrega_dias"] = (df_copy["fechada_em"] - df_copy["entrega_desejada"]).dt.days
df_valid = df_copy.dropna(subset=["tempo_entrega_dias", "tipo_de_tarefa", "entrega_desejada"]).copy()

df_tipo_tarefa = (
    df_valid.groupby("tipo_de_tarefa")["tempo_entrega_dias"]
    .mean()
    .reset_index()
    .sort_values("tempo_entrega_dias", ascending=False)
)

tipos_medio = df_tipo_tarefa["tipo_de_tarefa"].unique()

fig2 = px.bar(
    df_tipo_tarefa,
    x="tempo_entrega_dias",
    y="tipo_de_tarefa",
    title="Tempo Médio de Entrega por Tipo de Tarefa",
    color="tipo_de_tarefa",
    text="tempo_entrega_dias"
)
fig2.update_traces(
    textposition="outside",
    textfont_size=12,
    marker_line_width=1.2,
    marker_line_color="black"
)
fig2.update_layout(
    xaxis_title="Tempo Médio (dias)",
    yaxis_title="Tipo de Tarefa",
    showlegend=False,
    height=600,
    xaxis_tickfont_size=12,
    yaxis_tickfont_size=12,
    bargap=0.25
)

# preparar uma versão de exibição (strings) do df_valid para o dataframe visual
df_valid_display = df_valid.copy()
df_valid_display["entrega_desejada"] = df_valid_display["entrega_desejada"].dt.strftime("%d/%m/%Y %H:%M")
df_valid_display["fechada_em"] = df_valid_display["fechada_em"].dt.strftime("%d/%m/%Y %H:%M")

# =========================
# Bloco: Tempo Total por Tipo de Tarefa (soma)
# =========================
df_tipo_tarefa_total = (
    df_valid.groupby("tipo_de_tarefa")["tempo_entrega_dias"]
    .sum()
    .reset_index()
    .sort_values("tempo_entrega_dias", ascending=False)
)

tipos_total = df_tipo_tarefa_total["tipo_de_tarefa"].unique()

fig_tempo_total = px.bar(
    df_tipo_tarefa_total,
    x="tempo_entrega_dias",
    y="tipo_de_tarefa",
    title="Tempo Total de Entrega por Tipo de Tarefa",
    color="tipo_de_tarefa",
    text="tempo_entrega_dias"
)
fig_tempo_total.update_traces(textposition="outside", textfont_size=12, marker_line_width=1.2, marker_line_color="black")
fig_tempo_total.update_layout(xaxis_title="Tempo Total (dias)", yaxis_title="Tipo de Tarefa", showlegend=False, height=600, bargap=0.25)

# =========================
# Exibição conforme opção escolhida
# =========================
if opcao == "Tarefas Reabertas":
    fig0.update_traces(textinfo="value")
    st.plotly_chart(fig0, use_container_width=True)
    st.plotly_chart(fig1, use_container_width=True)

    st.dataframe(
        df_responsavel.rename(columns={
            "responsavel": "Responsável",
            "tipo_de_tarefa": "Tipo de Tarefa",
            "tarefas_reabertas": "Qtde de Tarefas Reabertas"
        }),
        use_container_width=True,
        hide_index=True
    )

elif opcao == "Tempo Médio por Tarefas Realizadas":
    st.plotly_chart(fig2, use_container_width=True)

    # construir tabela detalhada e permitir filtro por tipo (média)
    df_tipo_tarefa_detalhe = df_valid_display[
        ["tipo_de_tarefa", "responsavel", "entrega_desejada", "fechada_em", "tempo_entrega_dias"]
    ].reset_index(drop=True).sort_values("tipo_de_tarefa", ascending=True)

    tipo_selecionado = st.selectbox("Selecione o tipo de tarefa para exibição no dataframe:", tipos_medio)
    df_filtrado = df_tipo_tarefa_detalhe[df_tipo_tarefa_detalhe["tipo_de_tarefa"] == tipo_selecionado]

    st.dataframe(
        df_filtrado.rename(columns={
            "tipo_de_tarefa": "Tipo de Tarefa",
            "responsavel": "Responsável",
            "entrega_desejada": "Entrega Desejada",
            "fechada_em": "Fechada Em",
            "tempo_entrega_dias": "Tempo de Entrega (dias)"
        }),
        use_container_width=True,
        hide_index=True
    )

elif opcao == "Esforço Tarefas Concluidas <= 100%":
    limite = st.slider("Escolha o limite máximo (%)", 0, 100)
    # garantir que a coluna esteja em formato numérico (0..1)
    df_valid["porcentagem_tarefa_concluida"] = pd.to_numeric(df_valid["porcentagem_tarefa_concluida"], errors="coerce")
    df_menor = df_valid[df_valid["porcentagem_tarefa_concluida"] * 100 <= limite]

    df_menor = df_menor[["cliente", "projeto", "tipo_de_tarefa", "equipe", "responsavel",
                         "urgente", "aberta_por", "criada_em", "entrega_desejada", "fechada_em",
                         "esforco_estimado", "porcentagem_tarefa_concluida", "reaberta"]]

    df_menor["criada_em"] = df_menor["criada_em"].dt.strftime("%d/%m/%Y %H:%M")

    df_menor["entrega_desejada"] = df_menor["entrega_desejada"].dt.strftime("%d/%m/%Y %H:%M")

    df_menor["fechada_em"] = df_menor["fechada_em"].dt.strftime("%d/%m/%Y %H:%M")


    st.subheader("Valores com % <= 100")
    df_menor = df_menor.sort_values(by="porcentagem_tarefa_concluida", ascending=False)

    st.dataframe(df_menor.rename(columns={
        "cliente": "Cliente",
        "projeto": "Projeto",
        "tipo_de_tarefa": "Tipo de Tarefa",
        "equipe": "Equipe",
        "responsavel": "Responsável",
        "urgente": "Urgente",
        "aberta_por": "Aberta Por",
        "criada_em": "Criada Em",
        "entrega_desejada": "Entrega Desejada",
        "fechada_em": "Fechada Em",
        "esforco_estimado": "Esforço Estimado",
        "porcentagem_tarefa_concluida": "Porcentagem Esforço Tarefa Concluida",
        "reaberta": "Reaberta"
    }), use_container_width=True, hide_index=True)

elif opcao == "Esforço Tarefas Concluidas >= 100%":
    df_valid["porcentagem_tarefa_concluida"] = pd.to_numeric(df_valid["porcentagem_tarefa_concluida"], errors="coerce")
    df_maior = df_valid[df_valid["porcentagem_tarefa_concluida"] * 100 >= 100]

    df_maior = df_maior[["cliente", "projeto", "tipo_de_tarefa", "equipe", "responsavel",
                         "urgente", "aberta_por", "criada_em", "entrega_desejada", "fechada_em",
                         "esforco_estimado", "porcentagem_tarefa_concluida", "reaberta"]]
    df_maior["criada_em"] = df_maior["criada_em"].dt.strftime("%d/%m/%Y %H:%M")

    df_maior["entrega_desejada"] = df_maior["entrega_desejada"].dt.strftime("%d/%m/%Y %H:%M")

    df_maior["fechada_em"] = df_maior["fechada_em"].dt.strftime("%d/%m/%Y %H:%M")


    df_maior = df_maior.sort_values(by="porcentagem_tarefa_concluida", ascending=False)
    st.subheader("Valores com % >= 100")
    
    st.dataframe(df_maior.rename(columns={
        "cliente": "Cliente",
        "projeto": "Projeto",
        "tipo_de_tarefa": "Tipo de Tarefa",
        "equipe": "Equipe",
        "responsavel": "Responsável",
        "urgente": "Urgente",
        "aberta_por": "Aberta Por",
        "criada_em": "Criada Em",
        "entrega_desejada": "Entrega Desejada",
        "fechada_em": "Fechada Em",
        "esforco_estimado": "Esforço Estimado",
        "porcentagem_tarefa_concluida": "Porcentagem Esforço Tarefa Concluida",
        "reaberta": "Reaberta"
    }), use_container_width=True, hide_index=True)

elif opcao == "Tempo Total por Tarefas Realizadas":
    st.plotly_chart(fig_tempo_total, use_container_width=True)

    tipo_selecionado = st.selectbox("Selecione o tipo de tarefa para exibição no dataframe:", tipos_total)

    df_tipo_tarefa_total = df_copy[["cliente","projeto","tipo_de_tarefa","equipe","responsavel"
    ,"entrega_desejada","fechada_em","tempo_entrega_dias"]].reset_index(drop=True)

    # mudar posicão das datas dia mes ano
    df_tipo_tarefa_total["entrega_desejada"] = df_tipo_tarefa_total["entrega_desejada"].dt.strftime("%d/%m/%Y %H:%M")
    df_tipo_tarefa_total["fechada_em"] = df_tipo_tarefa_total["fechada_em"].dt.strftime("%d/%m/%Y %H:%M")

    # filtra o dataframe agrupado por tipo de tarefa
    df_filtrado = df_tipo_tarefa_total[df_tipo_tarefa_total["tipo_de_tarefa"] == tipo_selecionado]

    st.dataframe(
        df_filtrado.rename(columns={
            "cliente": "Cliente",
            "projeto": "Projeto",
            "tipo_de_tarefa": "Tipo de Tarefa",
            "equipe": "Equipe",
            "responsavel": "Responsável",
            "entrega_desejada": "Entrega Desejada",
            "fechada_em": "Fechada Em",
            "tempo_entrega_dias": "Tempo de Entrega (dias)"
        }),
        use_container_width=True,
        hide_index=True
    )

# fim do script
# cd  "E:\não copiada\cursos\Curso Bootcamp Company.e e Educ360\planilha do projeto"
# streamlit run Projeto_Atlantico.py