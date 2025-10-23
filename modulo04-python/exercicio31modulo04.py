# =============================================================
import pandas as pd
import matplotlib.pyplot as plt
# =============================================================

# =============================================================
# Lendo os dados
# =============================================================
origem = 'C:\\Users\\user\\pythonProject\\Educ360\\basededadosprojeto.csv'
dados = pd.read_csv(origem) # abrindo o arquivo e adicionando o conteudo
                            # dentro da var dados

print('é mostrado os 5 primeiros registros')
print(dados.head(),'\n') # é mostrado os 5 primeiros registros
print('é mostrado os 5 ultimos registros')
print(dados.tail(),'\n') # é mostrado os 5 ultimos registros
print('caso eu queira ver os 15 primeiros basta fazer assim')
print(dados.head(15)) # caso eu queira ver os 15 primeiros elementos
                      # basta fazer assim

# =============================================================
# Tipos de dados
# =============================================================
print('type (dados)',type(dados))

# método que nos informa a composição do nosso arquivo
# nosso arquivo é composto por 100 linhas e 4 colunas.
print(dados.shape)

# identificando quem são estas colunas, posso associar isto a
# uma variável e trabalhar como uma lista
print(dados.columns)

# fazendo um teste.
colunas = dados.columns
# printe na tela da segunda coluna
print(colunas[1])

# printe de todas as colunas, posso utilizar a técnica de fatiamento.
print(colunas[::])

# iremos mostrar as informações de cada coluna
print(dados.info())


# =============================================================
# Explorar os dados
# =============================================================
# como explorar o valor de cada coluna, e muito importante deve-se passar
# o nome da coluna não adianta ficar colocando números vai dar erro.
print('como explorar o valor de cada coluna.')
print(dados['montadora'])

# além disso é totalmente possível passar mais de um campo acompanhe:
print(dados[['montadora', 'modelo']])

# e na ordem que eu desejar:
print(dados[['modelo', 'valor_mercado']])

# =============================================================
# Analise dos dados (EDA)
# =============================================================
# como conseguir a média da base de dados, valor médio de todos os carros
media = dados['valor_mercado'].mean()
# dica de ouro para deixar já no padrão brasileiro real R$
# Passo a passo — exatamente o que acontece com
# Suponha media = 3125.31.
#
# Formatação inicial com f-string:
# s1 = f"R${media:,.2f}"
# :,.2f pede: agrupamento de milhares com vírgula (,) e 2
# casas decimais com ponto (.).
#
# Para 3125.31 → s1 == "R$3,125.31"
#
# Primeiro replace — replace(",", "X"):
# s2 = s1.replace(",", "X")
# Substitui TODAS as vírgulas por "X", criando um placeholder temporário.
#
# s2 == "R$3X125.31"
#
# Por que esse passo? Porque se você trocasse . → , primeiro, ao depois
# trocar , → . você confundiria os separadores (trocas colidem).
# O placeholder impede essa colisão.
#
# Segundo replace — replace(".", ","):
# s3 = s2.replace(".", ",")
# Agora todos os pontos decimais viram vírgulas.
#
# s3 == "R$3X125,31"
#
# Terceiro replace — replace("X", "."):
# s4 = s3.replace("X", ".")
# Por fim, substituímos o placeholder "X" pelos pontos de milhar.
#
# s4 == "R$3.125,31"
#
# E s4 é o que é impresso.
# Exemplo completo mostrando cada etapa
# media = 3125.31
#
# s1 = f"R${media:,.2f}"            # "R$3,125.31"
# s2 = s1.replace(",", "X")        # "R$3X125.31"
# s3 = s2.replace(".", ",")        # "R$3X125,31"
# s4 = s3.replace("X", ".")        # "R$3.125,31"
#
# print(s1)
# print(s2)
# print(s3)
# print(s4).
print(f"R${media:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# somando por grupos de carros
# com o método .mean(numeric_only=True) ele fará a média de todos os
# valores numéricos inclusive os que não interessa que são os anos.
media1 = dados.groupby('montadora').mean(numeric_only=True)
print(media1)

# agora quero apenas os de valores de mercado.
media1 = dados.groupby('montadora')['valor_mercado'].mean(numeric_only=True)
print(media1)

# colocando de forma ordenada.
media1 = dados.groupby('montadora')[['valor_mercado']].mean(numeric_only=True).sort_values('valor_mercado')
print('De forma ascendente')
print(media1)

# e caso eu queira do maior para o menor basta fazer assim:
# colocando de forma ordenada.
media1 = dados.groupby('montadora')[['valor_mercado']].mean(numeric_only=True).sort_values('valor_mercado', ascending=False)
print('De forma descendente')
print(media1)

# posso jogar isso em uma variável e determinar quais são os meus 3 primeiros
# acompanhe:.
tresprimeiros = media1
print(tresprimeiros.head(3))

# iremos gerar um gráfico
print('Com gráficos')
dados_montadora = dados.groupby('montadora')[['valor_mercado']].mean(numeric_only=True).sort_values('valor_mercado', ascending=False)
dados_montadora.plot(kind= 'barh', figsize=(10,5), color='red')

# como gerar graficos no python, é de suma importancia importar a biblioteca
# import matplotlib.pyplot as plt, e não esquecer do álias neste caso
# ficou assim: plt.
plt.title('Valor médio de mercado por montadora')
plt.xlabel('Valor de Mercado (R$)')
plt.ylabel('Montadora')
plt.show()


# para saber o percentual temos de contar os elementos
elementomont = dados.montadora.value_counts()
print(elementomont)

# posso gera um outro gráfico com esta informações
elementomont.plot(kind= 'barh', figsize=(10,5), color='blue')
plt.title('Quantidade por montadora')
plt.xlabel('Valor de Mercado (R$)')
plt.ylabel('Montadora')
plt.show()

# para saber o percentual temos de contar os elementos
elementomont = dados.montadora.value_counts(normalize=True)
print(elementomont)

# =============================================================
# Valores NULOS
# =============================================================
# verificar se existe valores nulos, mas não podemos confiar nesta visualização
print(f'Os valores nulos estão em: \n{dados.isnull().sum()}')

# já verificamos que existem nulos temos agora de tratar
# ao executar não acontecerá nada.
dados =  dados.fillna(0)

# então devemos conferir se os nulos foram substituidos por 0
# aqui temos uma forma mais eficiente de visualizar
dados.isnull().sum()
print(f'Os valores nulos estão em: \n{dados.isnull().sum()}')

# =============================================================
# Aplicar Filtros
# =============================================================
# passar os valores que tenho sem reptição
print(dados.montadora.unique())

# separando por montadoras
filtro = ['Toyota', 'Honda', 'Ford']

# é possivel fazer filtros desta forma, para uma única montadora
print(dados.query('montadora == "Ford"'),'\n')

# abaixo como filtrar em grupo
print('Filtros aplicados com o dados.query(@filtro in montadora)')
print(dados.query('@filtro in montadora'))


# é também possível um filtro dos que não foram selecionados de maneira
# bem simples
print('\nFiltro dos que não foram selecionados: ')
print(dados.query('@filtro not in montadora'))

# aplicando um gráfico
dados_pesq = dados.query('@filtro in montadora')


dados_montadora = dados_pesq.groupby('montadora')[['valor_mercado']].mean(numeric_only=True).sort_values('valor_mercado')
dados_montadora.plot(kind= 'barh', figsize=(10,5), color='red')
plt.title('Quantidade por montadora')
plt.xlabel('Valor de Mercado (R$)')
plt.ylabel('Montadora')
plt.show()

print('Gerando uma estastistica')
elementomont = dados_pesq.montadora.value_counts(normalize=True)
print(elementomont)

# =============================================================
# Filtro1-ANO
# =============================================================
# aplicando filtros por ano
print('\nAplicando filtros por ano')
dados_filtro_ano = dados_pesq['ano_fabricacao'] > 2020
print(dados_pesq[dados_filtro_ano])

# =============================================================
# Filtro2-VALOR
# =============================================================
# aplicando filtros por valor
print('\nAplicando filtros por valor')
dados_filtro_valor = dados_pesq['valor_mercado'] >= 30000
print(dados_pesq[dados_filtro_valor])


# a combinação de dois filtros.
print('\nA junção de dois filtros')
dados_filtro_final = (dados_filtro_ano) & (dados_filtro_valor)
print(dados_pesq[dados_filtro_final])

# uma outra maneira de fazer.
# uma outra forma de fazer.
print('\nUma outra forma de fazer.')
selecao = dados_pesq.query('ano_fabricacao > 2020 and valor_mercado >= 30000')
print(selecao)

# =============================================================
# Salvar os dados
# =============================================================
# como salvar os dados 1ª forma
print('Gravando o arquivo')
selecao.to_csv('pesq_claudio.csv')

# fazendo a leitura do arquivo
print('Fazendo a leitura do arquivo do Claudio')
arquivo_claudio = pd.read_csv('../pesq_claudio.csv')
print(arquivo_claudio)
# =============================

# =============================
# retirando o Unnamed do arquivo gerado
# =============================
# como salvar os dados 2ª forma, retirando o Unnamed do arquivo
print('Gravando o arquivo')
selecao.to_csv('pesq_claudio.csv', index=False)

# fazendo a leitura do arquivo
print('Fazendo a leitura do arquivo do Claudio')
arquivo_claudio = pd.read_csv('../pesq_claudio.csv')
print(arquivo_claudio)
# =============================

# =============================
# mudando o separador para ponto e virgula ;
# retirando o Unnamed
# =============================
# como salvar os dados 3ª forma, mudando o separador para ponto e virgula ;
# e  retirando o Unnamed do arquivo
print('Gravando o arquivo')
selecao.to_csv('pesq_claudio.csv', index=False, sep=';')

# fazendo a leitura do arquivo
print('Fazendo a leitura do arquivo do Claudio')
arquivo_claudio = pd.read_csv('../pesq_claudio.csv', sep=';')
print(arquivo_claudio)
# =============================


# =============================
# arquivo final
# =============================
# retirando o Unnamed do arquivo gerado
print('Gravando o arquivo')
selecao.to_csv('pesq_claudio.csv', index=False)

# fazendo a leitura do arquivo
print('Fazendo a leitura do arquivo do Claudio')
arquivo_claudio = pd.read_csv('../pesq_claudio.csv')
print(arquivo_claudio)