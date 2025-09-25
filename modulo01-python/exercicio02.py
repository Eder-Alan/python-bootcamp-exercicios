# - Para a divisão de 25 por 7, qual seria a parte inteira do resultado e qual seria o resto da
# divisão?


resultado = 0.0

print('Programa que calcula a parte inteira e o resto da divisão')
num01 = float(input('Digite um número: '))
num02 = float(input('Digite outro número: '))

if(num02 == 0):
    print('Não é possivel dividir por 0 !!!')
else:
    resultado = num01 // num02
    print(f'A parte inteira da divisão é: {resultado}')
    resultado = num01 % num02
    print(f'O resto da divisão é de: {resultado}')


# =========== com melhorias
# observações: a) Não usar float quando estamos falando de divisões inteiras
# Como o problema fala de parte inteira e resto, é mais natural trabalhar
# com números inteiros (int) ao invés de float.
# Assim, se o usuário digitar 25 e 7, o Python entende que são inteiros
# e evita problemas como 3.0 em vez de 3
#
# b) Variáveis separadas para parte inteira e resto
# Atualmente você está sobrescrevendo a variável resultado duas vezes.
# Não está errado, mas usar nomes diferentes deixa o código mais claro
# e organizado
#
# c) Mensagem final mais amigável
# Você pode formatar melhor o texto de saída, deixando um pequeno
# espaçamento ou usando \n para pular uma linha.

print('Programa que calcula a parte inteira e o resto da divisão')

# Entrada de dados
num01 = int(input('Digite um número: '))
num02 = int(input('Digite outro número: '))

# Processamento
if num02 == 0:
    print('Não é possível dividir por 0 !!!')
else:
    parte_inteira = num01 // num02
    resto = num01 % num02

    # Saída
    print(f'\nA parte inteira da divisão é: {parte_inteira}')
    print(f'O resto da divisão é: {resto}')
