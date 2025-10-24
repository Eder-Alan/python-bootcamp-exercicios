# ===============================================================
# Programa: Relatório de Vendas + Geração de Arquivo Formatado
# Autor: Eder (versão com funcionalidade de gravaçaõ)
# ===============================================================
import time
import os
# ---------------------------------------------------------------
# Define o nome do arquivo que contém os dados de vendas
# ---------------------------------------------------------------
var_arquivo = 'arquivovendas.txt'

# Verifica se o arquivo de entrada existe
if not os.path.exists(var_arquivo):
    print(f" Arquivo '{var_arquivo}' não encontrado! Certifique-se de que ele está na mesma pasta do programa.")
    exit()

# ---------------------------------------------------------------
# Lê o arquivo de vendas
# ---------------------------------------------------------------
with open(var_arquivo, 'r', encoding='utf-8') as arquivo:
    # Cada linha é dividida por ';' e removida de espaços/quebras de linha
    linhas = [linha.strip().split(';') for linha in arquivo]

# Separa o cabeçalho (primeira linha) do restante dos dados
cabecalho = linhas[0]  # Ex: ['Nome','Departamento','ValorVendas']
dados = linhas[1:]     # Registros de vendas

# ---------------------------------------------------------------
# Gera o relatório no terminal
# ---------------------------------------------------------------
var_total = 0.0  # Inicializa o total de vendas
titulo = "Relatório de Vendas"
largura_total = 42  # Largura total usada para formatação

print(titulo.center(largura_total, '='))
print(f'{cabecalho[0]:<10}  {cabecalho[1]:<12}  {cabecalho[2]:>12}')
print('-' * largura_total)

for nome, dep, valor in dados:
    vendas_float = float(valor)
    print(f'{nome:<10}  {dep:<12} R$ {vendas_float:>12,.2f}')
    var_total += vendas_float

print('-' * largura_total)
print(f'{"Total":<23}  R$ {var_total:>12,.2f}')
print('=' * largura_total, '\n')

# ---------------------------------------------------------------
# Opção de gerar o novo arquivo formatado
# ---------------------------------------------------------------
var_arquivonovo = 'arqvendasformatado.txt'

try:
    var_opcao = int(input('Deseja gerar um novo arquivo formatado? \nDigite 1 para Sim, ou 0 para Não: '))
except ValueError:
    print(' Opção inválida! Encerrando o programa.')
    exit()

if var_opcao == 1:
    print('\nVocê optou pela geração do arquivo...')
    print('Processando', end='', flush=True)
    for _ in range(3):  # efeito de carregamento
        time.sleep(1)
        print('.', end='', flush=True)
    print('\n')

    # Abre o arquivo em modo escrita (sobrescreve se já existir)
    with open(var_arquivonovo, 'w', encoding='utf-8') as arq_novo:
        arq_novo.write('\n')
        arq_novo.write(titulo.center(largura_total, '='))
        arq_novo.write(f'\n{cabecalho[0]:<10}  {cabecalho[1]:<12}  {cabecalho[2]:>12}\n')
        arq_novo.write('-' * largura_total)

        for nome, dep, valor in dados:
            vendas_float = float(valor)
            arq_novo.write(f'\n{nome:<10}  {dep:<12} R$ {vendas_float:>12,.2f}')

        arq_novo.write('\n' + '-' * largura_total)
        arq_novo.write(f'\n{"Total":<23}  R$ {var_total:>12,.2f}\n')
        arq_novo.write('=' * largura_total)

    print(f' Arquivo gerado com sucesso: {var_arquivonovo}\n')

else:
    print(' Você optou por não gerar o arquivo. Programa encerrado.')
