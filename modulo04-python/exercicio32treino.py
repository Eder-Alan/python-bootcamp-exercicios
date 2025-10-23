# =========================================================
# bibliotecas utilizadas
# =========================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# =========================================================
pd.set_option('display.max_columns', 20)
# Define o número máximo de colunas que o Pandas vai exibir ao imprimir um DataFrame
# Se o DataFrame tiver mais colunas do que esse valor, o Pandas abrevia a exibição
# (mostra as primeiras e últimas colunas e coloca ... no meio).
# Valor padrão: depende da versão do Pandas, mas normalmente é algo pequeno
# (por ex. 20 ou menos).
# Útil quando você quer ver muitas colunas durante a inspeção sem que o Pandas
# esconda colunas no meio.
# =========================================================

pd.set_option('display.max_rows', 50)
# Define o número máximo de linhas que o Pandas vai mostrar ao imprimir um DataFrame.
# Se o DataFrame tiver mais linhas do que esse valor, o Pandas trunca a saída
# (mostra as primeiras e as últimas linhas, com ... entre elas).
# Valor padrão costuma ser 60 ou similar; aqui você está forçando a exibição
# até 50 linhas antes do truncamento.
# Útil para evitar que grandes tabelas “poluam” a tela ou para garantir que você
# veja um bloco maior de linhas durante a depuração.

# =========================================================
# 2) Carregar a base "suja"
# =========================================================
# Se estiver no Colab: faça upload do arquivo ou use o caminho do Drive
# Exemplo local (substitua pelo seu caminho) ou use upload no Colab:
# from google.colab import files
# uploaded = files.upload()
# origem = 'base_locadora_suja.csv'

origem = 'base_locadora_suja.csv'  # variável que guarda o nome/caminho
                                   # do arquivo CSV de origem dos dados

df = pd.read_csv(origem)  # df é um DataFrame que armazena os dados do
                          # arquivo CSV de forma estruturada (linhas e colunas)
print(f'Dimensões: {df.shape}')  # exibe o número de linhas e colunas do
                               # DataFrame (formato da estrutura de dados)

print('\nEstrutura do arquivo ')
df.info() # me informa a estrutura do arquivo.

print(df.head(10))  # Exibe as 10 primeiras linhas do DataFrame para
                    # inspeção inicial
print(df.tail(10))  # Exibe as 10 últimas linhas do DataFrame para ver o
                    # final dos dados
# =========================================================

# =========================================================
# 3) Inspeção inicial — ver colunas, tipos, nulos, duplicados
# =========================================================
print(df.columns) # exibe o cabeçalho das colunas existentes
print(df.info())  # me informa a estrutura do arquivo.
print("\nContagem nulos por coluna:\n", df.isnull().sum())
# df.isnull() detecta nulos, sum() conta quantos há.

print("\nDuplicados:", df.duplicated().sum()) # informa se existem registros
                                              # duplicados e .sum conta quanta
                                              # existem.
print(df.sample(8))  # Seleciona aleatoriamente 8 linhas do DataFrame
# Útil para visualizar uma amostra dos dados sem precisar ver o DataFrame inteiro.
# Cada vez que você roda, normalmente as linhas escolhidas mudam,
# porque é aleatório.
# =========================================================


# =========================================================
# 4) Padronizar nomes de colunas (se necessário)
# =========================================================
# Renomeia colunas para padrão snake_case (se não estiverem assim)
# para cada coluna c no DataFrame, ele:
#
# Remove espaços extras (strip())
#
# Converte para minúsculas (lower())
#
# Substitui espaços por underscore (replace(' ', '_'))
#
# O for sempre vem depois da expressão na sintaxe de list comprehension..
df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]

print('\nExibindo as primeiras 2 linhas')
print(df.head(2)) # exibe as primeira 2 linhas
# =========================================================


# =========================================================
# 5) Limpar e converter a coluna valor_mercado para numérico
# =========================================================
# Explicação breve: remover R$, remover pontos de milhar, trocar vírgula
# decimal por ponto. Lidar com valores escritos por extenso como "cinco mil".
# # Função de limpeza robusta para "valor_mercado"
import re

def limpar_valor(v):
    if pd.isna(v):
        return np.nan
    s = str(v).strip()
    # tratar valores escritos (ex: "cinco mil")
    # mapeamento simples para palavras-chave comuns
    palavras = {
        r'cinco\s*mil': '5000',
        r'zero': '0'
    }
    for pat, rep in palavras.items():
        if re.search(pat, s, flags=re.IGNORECASE):
            s = re.sub(pat, rep, s, flags=re.IGNORECASE)
            break

    # remover "R$" e espaços
    s = re.sub(r'[Rr]\$\s*', '', s)
    # remover qualquer caractere que não seja dígito, vírgula ou ponto
    s = re.sub(r'[^\d\.,-]', '', s)

    # se conter mais de uma vírgula/ponto, tentar identificar separador decimal
    # estratégia: substituir pontos por vazio e vírgula por ponto (padrão BR)
    # mas primeiro identificar se o formato já tem vírgura decimal
    if s.count(',') == 1 and s.count('.') >= 1:
        # assume formato BR como "12.345,67"
        s = s.replace('.', '').replace(',', '.')
    else:
        # remove pontos que são milhares e troca vírgula por ponto
        s = s.replace('.', '').replace(',', '.')
    # se estiver vazio após limpeza, retornar NaN
    if s == '':
        return np.nan
    try:
        return float(s)
    except:
        return np.nan

# aplicar função
df['valor_mercado_limpo'] = df['valor_mercado'].apply(limpar_valor)
print("Antes/Depois exemplos:")
print(df[['valor_mercado','valor_mercado_limpo']].head(10))
# =========================================================

# ABAIXO LIMPEZA UTILIZADA EM CASOS ESPECIFICOS.
# =========================================================
# 6) Limpar e padronizar montadora e modelo
# =========================================================
# tirar espaços extras e padronizar case
df['montadora'] = df['montadora'].astype(str).str.strip().str.title().replace({'nan': np.nan})
# explicações:
# 1) df['montadora']
#
# Seleciona a coluna chamada "montadora" do DataFrame — o alvo das transformações.
# 2) .astype(str)
#
# Converte todos os valores da coluna para strings Python ('abc', '123', etc.). Importante:
#
# Valores np.nan ou None são convertidos para a string literal 'nan' (ou 'None' em alguns casos), não permanecem como valor nulo.
#
# Essa conversão permite usar os métodos de string .str.* em toda a série sem erro.
# 3) .str.strip()
#
# Aplica a função strip() a cada string: remove espaços em branco no início e no fim.
# Exemplo: ' ford ' → 'ford'.
#
# 4) .str.title()
#
# Aplica title() a cada string: coloca em Title Case, ou seja, primeira letra de cada palavra em maiúscula e o restante em minúscula.
# Exemplos:
#
# 'ford' → 'Ford'
#
# 'volkswagen do brasil' → 'Volkswagen Do Brasil'
#
# Observação: title() trata hífens e apóstrofos de forma específica e nem
# sempre é desejável (por exemplo, McDonald vira Mcdonald).
# Para regras específicas pode ser necessário um tratamento customizado.
# 5) .replace({'nan': np.nan})
#
# Substitui ocorrências da string exata 'nan' por np.nan (valor nulo do NumPy / do pandas).
# Por que provavelmente foi colocado aqui: depois de .astype(str)
# os NaN originais viraram a string 'nan', então essa substituição tenta
# restaurar esses valores como nulos reais.

# abaixo basicamente a mesma explicação da anterior
df['modelo'] = df['modelo'].astype(str).str.strip().str.title().replace({'Nan': np.nan, 'None': np.nan})

# corrigir alguns erros conhecidos (ex: WRV -> WR-V, WRV sem hífen)
df['modelo'] = df['modelo'].replace({'Wrv': 'Wr-V'})
df[['montadora','modelo']].head(10)
# =========================================================


# =========================================================
# 7) Converter ano_fabricacao para inteiro (lidar com nulos e strings)
# =========================================================
df['ano_fabricacao'] = pd.to_numeric(df['ano_fabricacao'], errors='coerce').astype('Int64')  # Int64 mantém NA
print("Tipos:\n", df.dtypes)
print(df[['ano_fabricacao']].head(10))
# =========================================================


# =========================================================
# 8) Tratar duplicados e nulos
# =========================================================
# Ver duplicados exatos
print("Duplicados exatos:", df.duplicated().sum())

# Mostrar duplicados exatos
print(df[df.duplicated(keep=False)].sort_values(['montadora','modelo','ano_fabricacao']))

# Remover duplicados exatos mantendo a primeira ocorrência
df = df.drop_duplicates().reset_index(drop=True)
print("Nova dimensão:", df.shape)

# Estratégias para nulos:
# - Se modelo ou montadora estiverem nulos: marcar como "Desconhecido"
df['montadora'] = df['montadora'].fillna('Desconhecida')
df['modelo'] = df['modelo'].fillna('Desconhecido')

# - Se ano_fabricacao for nulo, manter NA (ou imputar com média/moda se desejar)
# - Se valor_mercado_limpo for nulo, podemos preencher com 0 ou com a mediana da montadora
print("Nulos após primeira limpeza:\n", df[['ano_fabricacao','valor_mercado_limpo']].isnull().sum())

# Imputa (preenche) valores ausentes em 'valor_mercado_limpo' com a mediana
# por montadora.
# Para cada grupo de 'montadora', calcula a mediana apenas se existir pelo
# menos um valor válido
# (condição evita warnings em grupos totalmente nulos). Mantém consistência
# interna entre veículos da mesma marca.

df['valor_mercado_limpo'] = (
    df.groupby('montadora')['valor_mercado_limpo']
      .transform(lambda x: x.fillna(x.median()) if x.notna().any() else x)
)

# ainda que sobrem nulos (se toda a montadora não tiver valores), preencher com 0 ou global median
df['valor_mercado_limpo'] = df['valor_mercado_limpo'].fillna(df['valor_mercado_limpo'].median())
# =========================================================


# =========================================================
# 9) Coluna final formatada para exibir em BRL (opcional)
# =========================================================
def format_brl(x):
    if pd.isna(x):
        return ''
    s = f"R${x:,.2f}"
    return s.replace(',','X').replace('.',',').replace('X','.')

df['valor_mercado_formatado'] = df['valor_mercado_limpo'].apply(format_brl)
print(df[['valor_mercado','valor_mercado_limpo','valor_mercado_formatado']].head(8))
# =========================================================


# =========================================================
# 10) Análises rápidas (médias, contagens, gráficos)
# =========================================================
# média por montadora
media_por_mont = df.groupby('montadora')['valor_mercado_limpo'].mean().sort_values(ascending=False)
print(media_por_mont.head(10))

# contagem por montadora
contagem = df['montadora'].value_counts()
print(contagem)

# gráfico valor médio por montadora (barra horizontal)
ax = media_por_mont.plot(kind='barh', figsize=(10,6))
ax.set_xlabel('Valor médio (R$)')
ax.set_title('Valor médio por montadora')
plt.show()

# filtrar montadora e ano como você fazia
filtro = ['Toyota','Honda','Ford']
df_filtro = df[df['montadora'].isin(filtro)]
print(df_filtro.head())
# =========================================================


# =========================================================
# 11) Exportar arquivo limpo
# =========================================================
df_clean = df.copy()
# selecionar colunas finais que deseja salvar
df_clean = df_clean[['montadora','modelo','ano_fabricacao','valor_mercado_limpo','valor_mercado_formatado']]
df_clean.to_csv('base_locadora_limpa.csv', index=False, sep=';')
print("Salvo: base_locadora_limpa.csv")
# =========================================================


# =========================================================
# 12) Exercícios práticos para você (faça um por vez)
# =========================================================
# Antes de preencher nulos com mediana, experimente df.dropna() e observe
# quantas linhas são perdidas. Compare resultados.
# Experimente df['valor_mercado_limpo'].fillna(0) e veja como isso altera
# as médias por montadora.
# Crie uma coluna idade_veiculo = 2025 - ano_fabricacao (ou use o ano
# corrente automaticamente) e calcule a média por montadora.
# Encontre os top 5 modelos mais valiosos (por média) — e mostre
# também quantas unidades existem de cada modelo.
# também quantas unidades existem de cada modelo.
# Identifique outliers em valor_mercado_limpo (usar IQR ou z-score)
# e mostre as linhas.
# Crie um dashboard simples no Excel: exporte df_clean e use
# Tabelas/Pivôs/Gráficos no Excel para praticar visualização..


