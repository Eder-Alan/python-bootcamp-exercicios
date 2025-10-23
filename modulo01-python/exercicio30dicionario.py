# ============================================================
# PROGRAMA PARA IDENTIFICAR O VENDEDOR COM MAIOR E MENOR VENDA
# ============================================================

# Criamos um dicionário para armazenar o total de vendas de cada vendedor
# A chave do dicionário será o nome do vendedor
# O valor do dicionário será a soma de todas as vendas deste vendedor
vendas_totais = {}

# Abrimos o arquivo 'vendas.txt' no modo leitura ('r') e com codificação UTF-8
# O 'with' garante que o arquivo será fechado automaticamente ao final do bloco
with open('../codigos-python04aulas/arquivovendas.txt', 'r', encoding='utf-8') as arquivo:
    # A primeira linha do arquivo é o cabeçalho: "Nome;Departamento;ValorVendas"
    # Usamos 'next(arquivo)' para pular essa primeira linha
    next(arquivo)

    # Agora percorremos cada linha restante do arquivo
    for linha in arquivo:

        # strip() remove espaços extras no começo/fim da linha
        # split(';') separa a linha em uma lista de strings usando ';' como separador
        # Por exemplo: "Helena;Logística;17019.12" vira ['Helena', 'Logística', '17019.12']
        partes = linha.strip().split(';')

        # Atribuímos cada parte a uma variável para ficar mais legível
        nome = partes[0]  # Nome do vendedor
        departamento = partes[1]  # Departamento (não vamos usar neste exemplo)
        valor = float(partes[2])  # Valor da venda, convertido de string para float

        # Agora somamos as vendas do vendedor no dicionário
        # Se o vendedor já existe no dicionário, somamos o valor atual
        # Se não existe, criamos a chave com o valor atual
        if nome in vendas_totais:
            vendas_totais[nome] += valor
        else:
            vendas_totais[nome] = valor

# Depois de percorrer thodo o arquivo, o dicionário 'vendas_totais' contém:
# chave -> nome do vendedor 
# valor -> total de todas as suas vendas

# Para descobrir quem vendeu mais, usamos a função max()
# key=vendas_totais.get faz com que o max seja calculado com base nos valores do dicionário
vendedor_max = max(vendas_totais, key=vendas_totais.get)
print(f"O vendedor que mais vendeu foi {vendedor_max} com R$ {vendas_totais[vendedor_max]:.2f}")

vendedor_min = min(vendas_totais, key=vendas_totais.get)
# Mostramos o resultado formatando o valor com 2 casas decimais
print(f"O vendedor que menos vendeu foi {vendedor_min} com R$ {vendas_totais[vendedor_min]:.2f}")
