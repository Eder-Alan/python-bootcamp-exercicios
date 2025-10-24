# Assunto: Decisões.mp4
# - Peça ao usuário para digitar um número. Se o número for positivo,
# imprima "Número positivo!".

print('Programa que verifica se valor é positivo')
var_valor = float(input('Digite um valor qualquer: '))
if(var_valor > 0):
    print(f'{var_valor} é um valor positivo\n\n')


# =========================================.
# melhorias
print('Programa que verifica se valor é positivo ou negativo')
var_valor = float(input('Digite um valor qualquer: '))
if(var_valor == 0):
    print(f'{var_valor} é um valor neutro')
elif(var_valor > 0):
    print(f'{var_valor} é um valor positivo')
else:
    print(f'{var_valor} é um valor negativo')

# ===================================
# Versão simplificada e Pythonic
#
# Podemos deixar o código ainda mais limpo e profissional:.
print('Programa que verifica se valor é positivo, negativo ou neutro')

valor = float(input('Digite um valor qualquer: '))

if valor == 0:
    print(f'{valor} é um valor neutro')
elif valor > 0:
    print(f'{valor} é um valor positivo')
else:
    print(f'{valor} é um valor negativo')


# =============================
# Extra: deixando mais amigável
#
# Podemos melhorar a experiência do usuário e
# formatar o número para evitar casas decimais desnecessárias:.

print('Programa que verifica se valor é positivo, negativo ou neutro')

valor = float(input('Digite um valor qualquer: '))

if valor == 0:
    print(f'{valor:.0f} é um valor neutro')
elif valor > 0:
    print(f'{valor:.2f} é um valor positivo')
else:
    print(f'{valor:.2f} é um valor negativo')
