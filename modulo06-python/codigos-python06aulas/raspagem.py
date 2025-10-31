# ===============================
# Importação das bibliotecas
# ===============================

import requests  # Biblioteca usada para fazer requisições HTTP (baixar o conteúdo da página)
from bs4 import BeautifulSoup  # Biblioteca usada para analisar e extrair dados de páginas HTML
import streamlit as st  # Biblioteca para criar interfaces web interativas
import pandas as pd  # Biblioteca para manipulação e exibição de dados em formato de tabela (DataFrame)

# ===============================
# Configuração da página no Streamlit
# ===============================

st.set_page_config(page_title='Raspagem Aula', layout='wide')  # Define título e layout da página
st.title('Raspagem de Dados')  # Exibe o título no topo do app

# ===============================
# Definição da URL alvo
# ===============================

url = 'https://rhplay.com.br/'  # Site de onde serão extraídos os dados (alvo da raspagem)

# Cabeçalho (User-Agent) simula o acesso de um navegador real,
# para evitar bloqueios por parte do servidor do site.
cabecalho = {
    'User-Agente':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'
}

# Faz a requisição HTTP ao site
r = requests.get(url, headers=cabecalho)

# ===============================
# Tratamento do conteúdo HTML
# ===============================

# Cria um objeto BeautifulSoup a partir do HTML baixado,
# permitindo navegar e extrair partes específicas da página.
site = BeautifulSoup(r.content, 'html.parser')

# Mostra todo o código HTML da página no terminal (útil para testes)
print(site)

# ===============================
# Extração dos links
# ===============================

links = []  # Lista que armazenará os dicionários com "Texto do link" e "URL"

# Percorre todas as tags <a> (links) que possuem o atributo href
for a in site.find_all('a', href=True):
    texto = a.get_text(strip=True)  # Extrai o texto visível do link (remove espaços extras)
    link = a['href']  # Extrai o endereço (href)

    # Ignora links vazios, âncoras internas (#) ou apenas "/"
    if texto and link not in ('#', '/', ''):

        # Se o link for relativo (começa com "/"), completa com a URL base
        if link.startswith('/'):
            link = url.rstrip('/') + link

        # Transforma o link em HTML clicável para exibição no Streamlit
        link = f"<a href='{link}'> {link} </a>"

        # Adiciona o texto e o link formatado à lista
        links.append({'Texto do link': texto, 'URL': link})

# ===============================
# Conversão em tabela (DataFrame)
# ===============================

df = pd.DataFrame(links)  # Converte a lista de dicionários em tabela (DataFrame)

# Exibe a tabela no Streamlit, permitindo clicar nos links.
# O parâmetro escape=False permite renderizar o HTML e deixar os links clicáveis.
st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)

# ===============================
# Observações finais
# ===============================

# Vídeo de referência: Web Scraping (2º momento - 3:40)

# Para executar este script no terminal:
# 1. Acesse o diretório do projeto:
#    cd C:\Users\user\pythonProject\Educ360\codigos-python06aulas
# 2. Execute o servidor Streamlit:
#    streamlit run raspagem.py

# Este script faz uma raspagem simples de dados do site rhplay.com.br,
# extraindo todos os links da página.
# Depois ele organiza os dados em uma tabela usando o pandas e exibe
# tudo em uma interface web interativa criada com Streamlit.
# Assim é possível ver e clicar nos links diretamente na aplicação.