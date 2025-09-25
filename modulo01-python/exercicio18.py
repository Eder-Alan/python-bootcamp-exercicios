# - Peça ao usuário para digitar um número e gere a tabuada desse
# número de 1 a 10 usando um loop.

print('Programa que gera tabuada')
var_num = int(input('Digite o número da tabuada: '))

for x in range(1,11):
    print(f'{var_num} * {x} = {var_num * x}')

print('---------------')

var_contador = 1
while(var_contador < 11):
    print(f'{var_num} * {var_contador} = {var_num * var_contador}')
    var_contador += 1

# ====================== melhorias
# agora a saida fica parecendo uma tabela.

print('Programa que gera tabuada')

# Entrada do usuário
numero = int(input('Digite o número da tabuada: '))

print('\nUsando for:')
print('-' * 20)
for x in range(1, 11):
    print(f'{numero:2} x {x:2} = {numero * x:3}')
print('-' * 20)

print('\nUsando while:')
print('-' * 20)
contador = 1
while contador <= 10:
    # aqui vai ficar igual  a uma tabela no final.
    print(f'{numero:2} x {contador:2} = {numero * contador:3}')
    contador += 1
print('-' * 20)
