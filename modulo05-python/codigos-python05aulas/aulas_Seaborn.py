# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# importando bibliotecas
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# biblioteca para visualização de dados baseada no Matplotlib,
# com gráficos estatísticos mais elaborados e esteticamente aprimorados
import seaborn as sns

# módulo do Matplotlib usado para criar e personalizar gráficos em Python
import matplotlib.pyplot as plt

# biblioteca Pandas, que é amplamente usada em Python para manipulação e
# análise de dados, especialmente dados tabulares
# (como planilhas ou arquivos CSV).
#
# as pd → cria um apelido (pd) para a biblioteca, permitindo que você
# use funções do Pandas de forma mais curta.
import pandas as pd
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# funções
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def separador():
    print('=-'* 36)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
separador()
print(f'{"Inicio da aula 1 - Seaborn - Parte1":^50}')
separador()
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

dados = sns.load_dataset('tips')  # carrega um conjunto de dados
                                  # exemplo do Seaborn (gorjetas em um
                                  # restaurante)
dados.head()  # exibe as primeiras linhas do DataFrame
dados.tail()  # exibe as últimas linhas do DataFrame
dados.info()  # mostra informações sobre as colunas, tipos de dados e valores nulos
print(dados.describe(include='all'))  # exibe estatísticas descritivas de todas as colunas, incluindo categóricas

# Cria um gráfico de dispersão (scatter plot) usando o Seaborn
# Mostra a relação entre o valor total da conta (total_bill) e o valor da gorjeta (tip)
sns.scatterplot(x='total_bill', y='tip', data=dados)

# Define o título do gráfico
plt.title('Relação entre Total da Conta e Gorjeta')

# Exibe o gráfico na tela
plt.show()


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Cria um gráfico de dispersão com uma linha de regressão linear
# x='total_bill' → eixo X mostra o valor total da conta
# y='tip' → eixo Y mostra o valor da gorjeta
# data=dados → usa o DataFrame 'dados' como fonte de dados
sns.regplot(x='total_bill', y='tip', data=dados)

# Define o título do gráfico
plt.title('Relação entre Total da Conta e Gorjeta')

# Exibe o gráfico
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Cria um gráfico de barras com o Seaborn
# x='day' → eixo X representa os dias da semana
# y='tip' → eixo Y mostra o valor médio das gorjetas por dia
# data=dados → usa o DataFrame 'dados' como fonte de dados
sns.barplot(x='day', y='tip', data=dados)

# Define o título do gráfico
plt.title('Relação entre Total da Conta e Gorjeta')

# Exibe o gráfico na tela
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Cria um gráfico de barras com o Seaborn
# x='day' → eixo X representa os dias da semana
# y='tip' → eixo Y mostra o total de gorjetas por dia
# data=dados → usa o DataFrame 'dados' como fonte de dados
# estimator=sum → soma os valores de 'tip' para cada categoria em 'day'
sns.barplot(x='day', y='tip', data=dados, estimator=sum)

# Define o título do gráfico
plt.title('Relação entre Total da Conta e Gorjeta')

# Exibe o gráfico
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Cria um gráfico de barras usando a biblioteca Seaborn
# x='day' → define o eixo X com os dias da semana presentes na coluna 'day' do DataFrame
# y='tip' → define o eixo Y com os valores da coluna 'tip', que representa as gorjetas
# data=dados → especifica o DataFrame que contém os dados a serem plotados
# estimator='mean' → calcula a média das gorjetas para cada dia da semana (poderia ser sum, median, etc.)
sns.barplot(x='day', y='tip', data=dados, estimator='mean')

# Define o título do gráfico
plt.title('Relação entre Total da Conta e Gorjeta')

# Exibe o gráfico na tela
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Cria um gráfico de barras usando a biblioteca Seaborn
# x='day' → define o eixo X com os dias da semana presentes na coluna 'day' do DataFrame
# y='tip' → define o eixo Y com os valores da coluna 'tip', que representa as gorjetas
# data=dados → especifica o DataFrame que contém os dados a serem plotados
# estimator='mean' → calcula a média das gorjetas para cada dia da semana
# hue='day' → adiciona uma camada de cor baseada nos dias, necessário para usar palette sem warning
# palette='pastel' → aplica uma paleta de cores suaves (tons pastéis) para as barras
# dodge=False → mantém as barras juntas, sem separação por hue
# legend=False → remove a legenda extra gerada pelo hue
sns.barplot(
    x='day',
    y='tip',
    data=dados,
    estimator='mean',
    hue='day',
    palette='pastel',
    dodge=False,
    legend=False
)

# Define o título do gráfico
plt.title('Relação entre Total da Conta e Gorjeta')

# Exibe o gráfico na tela
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
separador()
print(f'{"Inicio da aula 2 - Seaborn - Parte2":^50}')
separador()
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Cria um gráfico do tipo boxplot (diagrama de caixa) usando Seaborn
# x='day' → define o eixo X com os dias da semana presentes na coluna 'day' do DataFrame
# y='total_bill' → define o eixo Y com os valores da coluna 'total_bill', que representa o valor total da conta
# data=dados → especifica o DataFrame que contém os dados a serem plotados
# O boxplot mostra a distribuição dos valores:
#   - A caixa representa o 1º e 3º quartil (Q1 e Q3)
#   - A linha dentro da caixa representa a mediana
#   - Os "bigodes" (whiskers) mostram o intervalo dos dados, excluindo outliers
#   - Pontos fora dos bigodes são considerados outliers
sns.boxplot(x='day', y='total_bill', data=dados)

# Define o título do gráfico
plt.title('Distribuição de valor das Contas por Dia')

# Exibe o gráfico na tela
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Cria um gráfico do tipo boxplot (diagrama de caixa) usando Seaborn
# x='day' → define o eixo X com os dias da semana presentes na coluna 'day' do DataFrame
# y='tip' → define o eixo Y com os valores da coluna 'tip', que representa as gorjetas
# data=dados → especifica o DataFrame que contém os dados a serem plotados
# O boxplot mostra a distribuição dos valores:
#   - A caixa (box) representa o intervalo interquartil (Q1 a Q3)
#   - A linha dentro da caixa representa a mediana (Q2)
#   - Os "bigodes" (whiskers) representam a extensão dos dados sem considerar outliers
#   - Pontos fora dos bigodes são considerados outliers (valores atípicos)
sns.boxplot(x='day', y='tip', data=dados)

# Define o título do gráfico
plt.title('Distribuição de valor das Gorjetas por Dia')

# Exibe o gráfico na tela
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Cria um histograma usando Seaborn para visualizar a distribuição dos dados
# data=dados → DataFrame que contém os dados
# x='total_bill' → coluna do DataFrame que será usada no eixo X (valores das contas)
# bins=25 → define em quantos intervalos (barras) o histograma será dividido
# kde=True → adiciona uma curva de densidade (Kernel Density Estimate) para mostrar a forma da distribuição
# color='orange' → define a cor das barras do histograma
sns.histplot(data=dados, x='total_bill', bins=25, kde=True, color='orange')

# Define o título do gráfico
plt.title('Histogramas das Contas')

# Exibe o gráfico na tela
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Cria um histograma usando Seaborn para visualizar a distribuição dos valores
# data=dados → DataFrame que contém os dados
# x='total_bill' → coluna do DataFrame que será usada no eixo X (valores das contas)
# bins=10 → define o número de intervalos (barras) do histograma, neste caso 10
# kde=False → não adiciona a curva de densidade, mostrando apenas as barras
# color='orange' → define a cor das barras do histograma
sns.histplot(data=dados, x='total_bill', bins=10, kde=False, color='orange')

# Define o título do gráfico
plt.title('Histogramas das Contas')

# Exibe o gráfico na tela
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Cria um histograma usando Seaborn para visualizar a distribuição das gorjetas
# data=dados → DataFrame que contém os dados
# x='tip' → coluna do DataFrame que será usada no eixo X (valores das gorjetas)
# bins=25 → define o número de intervalos (barras) do histograma
# kde=True → adiciona uma curva de densidade (Kernel Density Estimate) para mostrar a forma da distribuição
# color='orange' → define a cor das barras do histograma
sns.histplot(data=dados, x='tip', bins=25, kde=True, color='orange')

# Define o título do gráfico
plt.title('Histogramas das Gorjetas')

# Exibe o gráfico na tela
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# violino consigo visualizar a média e a mediana neste gráfico.
# Cria um gráfico do tipo violin plot usando Seaborn
# x='day' → define o eixo X com os dias da semana presentes na coluna 'day' do DataFrame
# y='tip' → define o eixo Y com os valores da coluna 'tip', que representa as gorjetas
# data=dados → especifica o DataFrame que contém os dados a serem plotados
# O violin plot mostra a distribuição dos dados combinando:
#   - A forma do "violino" representa a densidade dos dados (similar a um KDE)
#   - A linha branca no centro representa a mediana
#   - A linha preta dentro do violino representa o intervalo interquartil (Q1 a Q3)
#   - É possível observar a simetria e a concentração dos valores (picos)
sns.violinplot(x='day', y='tip', data=dados)

# Define o título do gráfico
plt.title('Distribuição de valor das Gorjetas por Dia')

# Exibe o gráfico na tela
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Cria um gráfico de linha usando Seaborn
# x='total_bill' → define o eixo X com os valores totais das contas
# y='tip' → define o eixo Y com os valores das gorjetas
# data=dados → especifica o DataFrame que contém os dados a serem plotados
# marker='o' → adiciona um marcador circular em cada ponto da linha para destacar os valores individuais
# O gráfico de linha ajuda a visualizar a relação entre o total da conta e o valor da gorjeta
sns.lineplot(x='total_bill', y='tip', data=dados, marker='o')

# Define o título do gráfico
plt.title('Relação entre Total da Conta e Gorjeta')

# Exibe o gráfico na tela
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Define a opção de filtro para o sexo
opc = 'Male'  # Pode ser 'Male' ou 'Female'

# Cria uma máscara booleana para filtrar apenas os dados do sexo escolhido
# dados.sex == opc → retorna True para linhas onde a coluna 'sex' é igual a opc
dadosf = dados.sex == opc

# Cria um gráfico de linha usando Seaborn apenas com os dados filtrados
# x='total_bill' → eixo X com os valores totais das contas
# y='tip' → eixo Y com os valores das gorjetas
# data=dados[dadosf] → aplica o filtro, usando apenas as linhas onde dadosf é True
# marker='o' → adiciona marcadores circulares em cada ponto da linha
sns.lineplot(x='total_bill', y='tip', data=dados[dadosf], marker='o')

# Define o título do gráfico, incluindo o sexo filtrado dinamicamente
plt.title(f'Relação entre Total da Conta e Gorjeta - Sexo {opc}')

# Exibe o gráfico na tela
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# caso eu queira dos dois sexos
# hue é semalhante a um groupby
# Cria um gráfico de linha usando Seaborn
# x='total_bill' → define o eixo X com os valores totais das contas
# y='tip' → define o eixo Y com os valores das gorjetas
# data=dados → DataFrame que contém todos os dados
# marker='o' → adiciona um marcador circular em cada ponto da linha
# hue='sex' → separa as linhas por sexo, desenhando uma linha para 'Male' e outra para 'Female'
#            cada linha terá uma cor diferente automaticamente
sns.lineplot(x='total_bill', y='tip', data=dados, marker='o', hue='sex')

# Define o título do gráfico
# f-string mantém o título dinâmico, mas aqui opc não influencia o gráfico, é apenas texto
plt.title(f'Relação entre Total da Conta e Gorjeta - Sexo {opc}')

# Exibe o gráfico na tela
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
separador()
print(f'{"Inicio da aula 3 - Seaborn - Parte3":^50}')
separador()
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Lê um arquivo CSV diretamente de uma URL usando Pandas
# sep=';' → define que o separador de colunas no arquivo é ponto e vírgula
df = pd.read_csv(
    'https://raw.githubusercontent.com/profivan-ai/cdb-Python/refs/heads/main/arquivos/alunos_cursos.csv',
    sep=';'
)

# Cria um gráfico de contagem (count plot) usando Seaborn
# x='Curso' → eixo X com os nomes dos cursos presentes na coluna 'Curso'
# data=df → DataFrame que contém os dados
# O countplot conta automaticamente quantas ocorrências existem para cada curso
sns.countplot(x='Curso', data=df)

# Define o título do gráfico
plt.title('Alunos por curso')

# Adiciona uma grade no gráfico (opcional)
# plt.grid(True) → se descomentado, adiciona linhas de grade no fundo do gráfico para facilitar leitura
# Você pode usar ou não, depende se quer visualizar melhor os valores
# plt.grid(True)

# Exibe o gráfico na tela
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Cria um gráfico de linha usando Seaborn
# x='Curso' → eixo X com os nomes dos cursos presentes na coluna 'Curso'
# y='Nota' → eixo Y com os valores da coluna 'Nota'
# data=df → DataFrame que contém os dados
# marker='o' → adiciona marcadores circulares em cada ponto da linha para destacar os valores individuais
sns.lineplot(x='Curso', y='Nota', data=df, marker='o')

# Define o título do gráfico
plt.title('Alunos por curso')

# Adiciona linhas de grade ao gráfico
# plt.grid(True) → opcional, facilita a leitura dos valores do eixo Y
# Você pode usar ou não, depende do quanto quer destacar a visualização
plt.grid(True)

# Exibe o gráfico na tela
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Cria um gráfico de linha usando Seaborn
# x='Curso' → eixo X com os nomes dos cursos presentes na coluna 'Curso'
# y='Nota' → eixo Y com os valores da coluna 'Nota'
# data=df → DataFrame que contém os dados
# marker='o' → adiciona marcadores circulares em cada ponto da linha
# hue='Certificado' → cria linhas separadas para cada valor da coluna 'Certificado'
#                      cada grupo terá uma cor diferente automaticamente
sns.lineplot(x='Curso', y='Nota', data=df, marker='o', hue='Certificado')

# Define o título do gráfico
plt.title('Alunos por curso')

# Adiciona linhas de grade ao gráfico (opcional)
# plt.grid(True) → ajuda a visualizar melhor os valores no eixo Y
plt.grid(True)

# Exibe o gráfico na tela
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Define o curso que será filtrado
var_curso = 'Excel'  # Pode ser 'Excel', 'Python', 'Lógica', 'Estatística', etc.

# Cria uma máscara booleana para filtrar apenas os dados do curso escolhido
# df.Curso == var_curso → retorna True para linhas onde a coluna 'Curso' é igual a var_curso
df_curso = df.Curso == var_curso

# Cria um gráfico de linha usando Seaborn apenas com os dados filtrados
# x='Nota' → eixo X com os valores das notas
# y='Aluno' → eixo Y com os nomes dos alunos
# data=df[df_curso] → aplica o filtro, usando apenas as linhas onde df_curso é True
# marker='o' → adiciona marcadores circulares em cada ponto da linha
sns.lineplot(x='Nota', y='Aluno', data=df[df_curso], marker='o')

# Define o título do gráfico, incluindo dinamicamente o nome do curso
plt.title(f'Média de Notas por Curso - {var_curso}')

# Adiciona linhas de grade ao gráfico (opcional)
# plt.grid(True) → facilita a leitura dos valores do eixo X
plt.grid(True)

# Exibe o gráfico na tela
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Define os cursos que podem ser filtrados
var_curso1 = 'Excel'       # Excel
var_curso2 = 'Python'      # Python
var_curso3 = 'Lógica'      # Lógica
var_curso4 = 'Estatística' # Estatística

# Cria uma máscara booleana para filtrar os dados de múltiplos cursos
# df.Curso == var_curso1 → True para linhas do curso Excel
# df.Curso == var_curso2 → True para linhas do curso Python
# | → operador "ou" para combinar as duas condições
df_curso = (df.Curso == var_curso1) | (df.Curso == var_curso2)

# Cria um gráfico de linha usando Seaborn apenas com os dados filtrados
# x='Nota' → eixo X com os valores das notas
# y='Aluno' → eixo Y com os nomes dos alunos
# data=df[df_curso] → aplica o filtro, usando apenas as linhas onde df_curso é True
# marker='o' → adiciona marcadores circulares em cada ponto da linha
# hue='Curso' → separa as linhas por curso, cada curso terá uma cor diferente
sns.lineplot(x='Nota', y='Aluno', data=df[df_curso], marker='o', hue='Curso')

# Define o título do gráfico, incluindo dinamicamente os cursos filtrados
plt.title(f'Média de Notas por Curso - {var_curso1} - {var_curso2}')

# Adiciona linhas de grade ao gráfico (opcional)
# plt.grid(True) → facilita a leitura dos valores do eixo X
plt.grid(True)

# Exibe o gráfico na tela
plt.show()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-