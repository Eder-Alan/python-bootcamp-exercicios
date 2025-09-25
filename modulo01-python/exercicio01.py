# Assunto: Operadores
# - Calcule e imprima a soma, subtração, multiplicação e divisão de dois números
# quaisquer . Ex: 20 e 4.



print('Programa que calcula soma, subtração, multiplicação e divisão'
      'de dois números')
num01 = float(input('Digite um número: '))
num02 = float(input('Digite outro número: '))

resultado = num01 + num02
print(f'A soma dos números é: {resultado}')
resultado = num01 - num02
print(f'A subtração dos números é: {resultado}')
resultado = num01 * num02
print(f'A multiplicação dos números é: {resultado}')
if(num02 == 0):
    print('Não é possivel dividir por 0 !!!')
else:
    resultado = num01 / num02
    print(f'A divisão dos números é: {resultado}')

# ========= com melhorias:

print('Programa que calcula soma, subtração, multiplicação e divisão '
      'de dois números')

# Entrada de dados
num01 = float(input('Digite um número: '))
num02 = float(input('Digite outro número: '))

# Processamento
soma = num01 + num02
subtracao = num01 - num02
multiplicacao = num01 * num02

if num02 != 0:
    divisao = num01 / num02
else:
    divisao = None

# Saída
print(f'\nA soma dos números é: {soma}')
print(f'A subtração dos números é: {subtracao}')
print(f'A multiplicação dos números é: {multiplicacao}')

if divisao is not None:
    print(f'A divisão dos números é: {divisao:.2f}')
else:
    print('Não é possível dividir por 0 !!!')
