# aula 05 do modulo de python Professor Ivan.
num1 = 0 # esta é do tipo inteiro
num2 = 0.0 # esta é do tipo flutuante
nome = "Ana" # esta é do tipo string ou texto
cliente = True # isto é uma variável booleana variável lógica
# para descobrir o tipo de uma variávle podemos utilizar o type
# exemplo print(type(num2)).
print(type(num2))

# as vaiáveis no python são dinamicamente tipadas exemplo
# num1 = 0 é do tipo int mas se fizermos assim: num1 = 0.0
# ela já muda sua tipagem acompanhe.

print('num1 do tipo int ', type(num1))
num1 = 0.0
print('num1 do tipo flaot ', type(num1))

# no caso abaixo caso você digite qualquer coisa o python entenderá
# como uma string.
entrada = input('Digite algo: ')
print(type(entrada))

# para que isso não ocorrá devemos antes de capturar a variavel
# especificar o tipo dela acompanhe:.

entrada = int(input('Digite o mesmo caractere anterior: '))
print(type(entrada))

# Calcule a raiz quadrada de um número qualquer

raiz = int(input('Digite um número para se tornar raiz: '))
# abaixo como calcular a raiz quadrada!!!
resultado = raiz ** (1/2)
print(f'A raiz quadada de {raiz} = ', resultado)