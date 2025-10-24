# - Peça ao usuário para digitar um número inteiro.
# ◦ Se o número for par, verifique se ele é maior que 10.
# ▪ Se for par e maior que 10, imprima "Número par e grande!".
# ▪ Se for par mas não maior que 10 (ou seja, menor ou igual a 10), imprima "Número
# par e pequeno.".
# ◦ Se o número for ímpar, imprima "Número ímpar."

# var_numint = 0
print('Programa que identifica número')
var_num = int(input('Digite um número inteiro: '))

if(var_num  % 2 == 0):
    if(var_num > 10):
        print('Número par e grande!')
    else:
        print('Número par e pequeno')
else:
    print('número é impar')

# ====================== melhorias
# Ajuste nas mensagens
#
# Colocar acentos corretamente em "ímpar" e "número".
#
# Adicionar ponto final em todas as mensagens para padronização.

print('Programa que identifica número')
var_num = int(input('Digite um número inteiro: '))

if var_num % 2 == 0:
    if var_num > 10:
        print('Número par e grande!')
    else:
        print('Número par e pequeno.')
else:
    print('Número ímpar.')

# Tratamento de entrada inválida (try/except)
#
# Se o usuário digitar algo que não seja um número, o programa quebrará com erro.
# Podemos resolver isso com try e except:.

print('Programa que identifica número')

try:
    var_num = int(input('Digite um número inteiro: '))

    if var_num % 2 == 0:
        if var_num > 10:
            print('Número par e grande!')
        else:
            print('Número par e pequeno.')
    else:
        print('Número ímpar.')
except ValueError:
    print('Entrada inválida! Por favor, digite apenas números inteiros.')
# Benefício: Evita que o programa quebre com uma entrada errada, como "abc".

# ========================================.
# Versão compacta usando condições compostas
#
# Podemos simplificar a lógica, mantendo a clareza:.

print('Programa que identifica número')

try:
    var_num = int(input('Digite um número inteiro: '))

    if var_num % 2 != 0:
        print('Número ímpar.')
    elif var_num > 10:
        print('Número par e grande!')
    else:
        print('Número par e pequeno.')
except ValueError:
    print('Entrada inválida! Por favor, digite apenas números inteiros.')
# Benefício: Menos níveis de indentação, tornando o código mais limpo.

# =============================
# Versão ainda mais elegante com função
#
# Se você quiser modularizar para reaproveitar depois:.

def classificar_numero(n):
    if n % 2 != 0:
        return 'Número ímpar.'
    elif n > 10:
        return 'Número par e grande!'
    else:
        return 'Número par e pequeno.'

print('Programa que identifica número')

try:
    var_num = int(input('Digite um número inteiro: '))
    print(classificar_numero(var_num))
except ValueError:
    print('Entrada inválida! Por favor, digite apenas números inteiros.')

# Benefício:
#
# Fácil de testar em programas maiores.
#
# Código fica mais organizado e reutilizável.