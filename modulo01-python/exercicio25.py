# Exercício: Processamento de Registro e Conversão de Tipo
# Receba um registro de funcionário onde os campos estão separados por
# ponto-e-vírgula. Quebre o registro e, em seguida, verifique se o salário
# (terceiro campo) é maior que 50000. Lembre-se de que os valores vêm como
# string e precisam ser convertidos para float para comparação numérica.
# Ex: registro_funcionario = "ID005;Maria Silva;12500.75;Contabilidade".

registro_funcionario = "ID005;Maria Silva;12500.75;Contabilidade"

# Quebrando o registro em uma lista
campos = registro_funcionario.split(';')
print(campos)
if float(campos[2]) >= 50000:
     print(f'O salario de: R${campos[2]} é maior que R$50000')
else:
    # aqui pode dar erro pelo fato de querer adiciondo o :.2f o ideal
    # é já converter o a variavel para float logo no começo e depois
    # utiliza-lá como quiser dentro das condicionais.
    print(f'O salario de: R${campos[2]} não é maior que R$50000')
print('\n==========================================')



# ================== melhorias e evita erro na execução.
salario = float(campos[2])
if salario >= 50000:
    print(f'O salário de: R${salario:,.2f} é maior que R$50.000,00')
else:
    print(f'O salário de: R${salario:,.2f} não é maior que R$50.000,00')
