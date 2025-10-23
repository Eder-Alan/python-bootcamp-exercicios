# Módulos (Modules)
# Exercício: Módulos são arquivos externos que contêm definições e instruções
# que podem ser importadas. Podemos importar módulos nativos do Python ou módulos
# criados por nós mesmos. Importe o módulo random (módulo nativo do Python).
# Gere uma lista de 5 números aleatórios no intervalo de 1 a 100 e imprima-a.

import random

lista = []
for x in range(5):
    aleatorio = random.randint(1,100)
    lista.append(aleatorio)
print(lista)
print('\n==========================================')





# ============ exercicios adicionais para praticar e testar

print('programa que sorteia jogos para mega sena')
# random.sample() já retorna uma lista pronta com os 6 números únicos.
numero_jogo = random.sample(range(1, 61), 6)  # 6 números únicos entre 1 e 60
numero_jogo.sort()
print(f'Os números para apostar são: {numero_jogo}')
print('\n==========================================')

# ============ exercicios adicionais para praticar e testar
pc = random.randint(1,10)
print('Programa que advina número digitado pelo ususário')
#print(pc)
try:
    numero = int(input('Digite um número inteiro entre 1 a 10: '))
    if numero == pc:
        print('Parabéns você adivinhou o número!!!')
    else:
        print(f'Sinto muito não foi desta vez, o número correto é: {pc}')
except ValueError:
    print("Erro: você não digitou um número inteiro válido!")
