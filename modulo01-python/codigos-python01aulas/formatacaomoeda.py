vendas_float = 17019.12
# Converte para string com separador de milhar americano
valor_formatado = f"{vendas_float:,.2f}"
# Troca ',' por temporário, '.' por ',', depois temporário por '.'
valor_formatado = valor_formatado.replace(',', 'X').replace('.', ',').replace('X', '.')
print(valor_formatado)
