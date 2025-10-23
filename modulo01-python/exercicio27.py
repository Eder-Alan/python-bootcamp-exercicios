# Exercício: Verificação de Chave antes do Acesso
# Crie um dicionário chamado estoque com alguns produtos. Peça ao usuário que
# digite um nome de produto. Antes de tentar imprimir o preço, verifique se a
# chave digitada existe no dicionário para evitar erros.
# estoque = {
# "TV": 1500,
# "Rádio": 200,
# "Microondas": 900
# }.


estoque = {"TV": 1500,
           "Rádio": 200,
           "Microondas": 900
           }

print(estoque)

produto = input('Digite o nome do produto: ')
if produto in estoque:
    print(f'O produto {produto} existe no estoque e custa: R${estoque[produto]}')
else:
    print('Este produto não existe no estoque.')
print('\n==========================================')


# ============ exercicios adicionais para praticar e testar
# primeiro padronizar o dicionário e deixar tudo minúsculo.
estoque = {"tv": 1500,
           "rádio": 200,
           "microondas": 900,
           "dvd": 1500,
           "pc": 3500,
           "monitor": 4500,
           "teclado": 75,
           "mouse": 40
           }

print('Programa que faz verificação se existe produto no estoque')
produto = input('Digite o nome do produto que procura: ').lower().strip()
if produto in estoque:
    print(f'O produto {produto} consta no estoque e custa R${estoque[produto]:.2f}')
else:
    print('Este produto não consta no estoque.')