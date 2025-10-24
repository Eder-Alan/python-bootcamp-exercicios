var_notas = []
var_contador = 0
var_media    = 0
print('Programa que faz calculo de aprovado ou não')

for var_contador in range(4):
    var_notas.append(float(input('Digite uma nota: ')))
    var_media += var_notas[var_contador]
var_media /= 4

print(f"As notas digitadas são: ")

for var_contador in range(4):
    print(f"{var_contador +1}ª nota {var_notas[var_contador]}")
    
print(f'A média é: {var_media}')
if var_media >= 7:
    print('\nAprovado')
else:
    print('\nNova Prova')