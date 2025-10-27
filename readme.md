# Bootcamp Python -Aulas e Exercícios

Este repositório contém os exercícios que desenvolvi durante o **Bootcamp de Python**, organizados por módulos.  
O objetivo é acompanhar minha evolução, praticar a linguagem e criar um portfólio que mostre minha jornada no aprendizado de programação.




## 📝 Módulo 01 - Fundamentos de Python

O primeiro módulo aborda os conceitos iniciais da linguagem.  
Aqui estão alguns dos temas estudados:

- Variáveis e tipos de dados  
- Operadores matemáticos e lógicos  
- Estruturas condicionais (`if`, `elif`, `else`)  
- Estruturas de repetição (`while`, `for`)  
- Entrada e saída de dados (`input` e `print`)  
- Tratamento básico de erros (`try` e `except`)


## 📝 Módulo 02 - Estruturas de Dados e Módulos

O segundo módulo explora as principais estruturas de dados do Python e o uso de módulos nativos.
Aqui estão alguns dos temas estudados:

- Listas: criação, acesso, modificação, fatiamento (slices), step e inversão; uso do método split() para transformar strings em listas.

- Dicionários: criação e manipulação de pares chave-valor; verificação de existência de chaves antes do acesso.

- Módulos: utilização do módulo random para gerar números aleatórios e simular jogos, como apostas de Mega-Sena.

- Tuplas: tuplas como coleções imutáveis; manipulação de listas internas dentro de tuplas.

- Boas práticas aplicadas: tratamento de erros com try/except, uso de f-strings, padronização de listas e dicionários, comentários explicativos para reforço do aprendizado.


## 📝 Módulo 03 - Manipulação de Arquivos e Funções Avançadas

- O terceiro módulo foca em técnicas de manipulação de arquivos e aprofundamento no uso de funções no Python.

Aqui estão alguns dos temas estudados:

- Funções: definição, parâmetros, retorno de valores, funções com múltiplos argumentos.

- Tratamento de exceções: uso de try, except, finally para capturar e tratar erros de forma segura.

- Leitura e escrita em arquivos: abrir arquivos em diferentes modos (r, w, a), leitura linha a linha, gravação de dados, fechamento automático de arquivos com with.

- Exercícios práticos com arquivos: manipulação de arquivos de texto, registros estruturados, listas a partir de arquivos.

- Boas práticas: documentação de funções, comentários explicativos, organização de código em módulos e reaproveitamento de funções em múltiplos exercícios.


## 📝 Módulo 04 - Análise de Dados com Pandas

Neste módulo, o foco foi aplicar os conceitos de análise de dados utilizando a biblioteca Pandas do Python.
A proposta prática foi o desenvolvimento de um projeto para uma locadora de carros e vendas, com o objetivo de criar uma extratificação de dados.

💡 Descrição do projeto

A locadora forneceu uma base de dados contendo informações sobre montadoras, modelos e anos dos veículos.
O desafio foi coletar, analisar e disponibilizar esses dados de forma estruturada, permitindo que o usuário pudesse:

Selecionar uma montadora específica;

Filtrar por modelo e ano;

Receber um extrato analítico com base nessas informações.

🧰 Ferramentas utilizadas

Pandas: para leitura, manipulação e análise da base de dados.

Google Colab: ambiente de desenvolvimento utilizado para implementação e testes do código.

Trello: ferramenta empregada para organização e acompanhamento das etapas do projeto, facilitando a gestão das tarefas e a divisão de responsabilidades entre as fases.

🎯 Objetivo

Proporcionar uma experiência prática no uso do Pandas para análise de dados reais, desenvolvendo a capacidade de estruturar informações, aplicar filtros e gerar resultados úteis para a tomada de decisão em um contexto empresarial.

## 💼 Atividade Extra (Projeto Pessoal)

Como atividade complementar — desenvolvida por iniciativa própria — criei um dashboard interativo no Excel utilizando a base de dados original do projeto.
O processo envolveu as seguintes etapas:

Limpeza e tratamento dos dados para padronização e consistência das informações;

Modelagem e estruturação dos dados tratados;

Criação de um dashboard dinâmico, com gráficos e indicadores de desempenho, oferecendo uma visualização clara e intuitiva dos principais resultados da análise.

Essa atividade reforçou o entendimento sobre preparação de dados e visualização de informações, além de demonstrar a integração entre ferramentas como Python, Pandas e Excel no contexto de análise de dados aplicada.


## 📝 Módulo 05 - Visualização de Dados com Matplotlib, Plotly e Seaborn

Neste módulo, o foco foi aprender a visualizar dados utilizando diferentes bibliotecas do Python, aplicando os conceitos de análise de dados em situações práticas.

💡 Bibliotecas estudadas:

Matplotlib: criação de gráficos de barra, pizza e linha; personalização de cores, bordas e grades; tratamento de dados nulos para visualizações precisas.

Plotly: gráficos interativos para exploração de dados em dashboards.

Seaborn: gráficos estatísticos com estilo refinado e fácil integração com Pandas.

🧰 Atividades desenvolvidas:

Atividade 1 (Vendas da Loja):

Leitura e tratamento de valores nulos no dataset vendas_loja.csv (preenchimento com 0).

Criação de gráficos com Matplotlib:

Gráfico de barras: total de vendas por categoria.

Gráfico de pizza: proporção de vendas por região.

Gráfico de linhas: evolução das vendas ao longo dos meses.

Objetivo: identificar categorias mais lucrativas, distribuição regional e tendências mensais de vendas.

Atividade 2 (Pacientes da Clínica):

Leitura e tratamento de valores nulos no dataset pacientes_clinica.csv (preenchimento com média para glicose e pressão).

Criação de gráficos com Matplotlib:

Gráfico de barras: média de glicose por faixa etária.

Gráfico de pizza: proporção de pacientes por gênero.

Gráfico de linhas: evolução média da pressão arterial por mês.

Objetivo: compreender padrões de saúde por faixa etária, distribuição de gênero e tendências mensais na pressão arterial.

🎯 Resultados e aprendizado:

Aprendi a tratar dados nulos de forma estratégica para cada tipo de análise.

Desenvolvi habilidade em criar gráficos informativos e esteticamente claros usando diferentes bibliotecas de visualização.

Consolidei a prática de gerar insights a partir de dados reais, visualizando tendências e distribuições importantes.


## 🌐 Módulo 06 - Criação de Dashboards Interativos com Streamlit

Neste módulo, o foco foi aprender a criar **aplicativos web interativos** para visualização de dados, utilizando a biblioteca **Streamlit**, facilitando a apresentação de insights de forma dinâmica e profissional.

💡 Conceitos estudados:

Streamlit: transformar scripts Python em dashboards interativos sem necessidade de HTML/CSS/JavaScript.

Widgets interativos: sliders, checkboxes, dropdowns e botões para permitir filtros e ajustes em tempo real.

Visualização dinâmica: integração com Matplotlib, Seaborn, Plotly e tabelas do Pandas.

Upload de arquivos: permitir que o usuário carregue datasets diretamente no aplicativo.

🎯 Neste módulo, o foco foi aprender a criar **dashboards interativos** utilizando **Python**, permitindo explorar dados de forma dinâmica e intuitiva através do navegador.

💡 Bibliotecas estudadas:

- **Pandas**: manipulação e filtragem de dados (DataFrames), leitura de CSVs e operações com datas.
- **Plotly Express**: criação de gráficos interativos (barras, linhas, pizza) integrados ao dashboard.
- **Streamlit**: criação de aplicativos web interativos sem necessidade de HTML/CSS/JavaScript, com suporte a widgets como `selectbox`, filtros e visualização de tabelas.

🧰 Atividades desenvolvidas:

1. **Leitura e tratamento de dados**:  
   - Carregamento do dataset `consultas.csv`.  
   - Conversão da coluna `dataconsulta` para o formato datetime.  
   - Criação de listas únicas de datas e unidades para filtros.

2. **Filtragem interativa**:  
   - Criação de `selectbox` na barra lateral (`sidebar`) para filtrar por data e unidade.  
   - Aplicação de filtros no DataFrame com base nas seleções do usuário.

3. **Criação de gráficos e visualizações**:  
   - Número de consultas por unidade usando `groupby` e gráficos interativos com Plotly.  
   - Exibição do DataFrame filtrado no dashboard.  
   - Layout configurado para ocupar toda a largura da tela (`layout='wide'`) e título personalizado da página.

4. **Configuração do Streamlit**:  
   - Definição do título do dashboard: “📊 Painel de Consultas Médicas”.  
   - Preparação do app para execução local com:  

   ```bash
   streamlit run Dashboard.py
