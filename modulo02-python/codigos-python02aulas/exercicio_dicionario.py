# %%

produto = input('Nome do produto: ')

lista = {"TV": 1500,
           "Rádio": 200,
           "Microondas": 500,
           "geladeira": 3500,
           "forno": 900
        }

if produto in lista.keys():
    print(lista[produto])
else:
    print('Não existe')


