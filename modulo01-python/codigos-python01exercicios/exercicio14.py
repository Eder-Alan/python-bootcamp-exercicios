# - Peça ao usuário para digitar uma temperatura em Celsius.
# ◦ Se a temperatura for maior que 30, imprima "Está muito quente!".
# ◦ Se for menor que 10, imprima "Está muito frio!".
# ◦ Caso contrário (entre 10 e 30, inclusive), imprima "Temperatura agradável.".

print('Programa que informa se está muito quente ou está frio')
var_graus = float(input('Digite a temperatura em Graus Celsius: '))
if(var_graus > 30):
    print('Está muito quente!')
elif(var_graus < 10):
    print("Está muito frio!")
else:
    print('Temperatura agradável.')

# ======================== melhorias
# Validando a entrada do usuário
#
# Se alguém digitar algo que não seja um número, seu programa vai gerar erro.
# Podemos resolver isso usando try e except para capturar entradas inválidas:


print('Programa que informa se está muito quente ou está frio')

try:
    var_graus = float(input('Digite a temperatura em Graus Celsius: '))

    if var_graus > 30:
        print(f'A temperatura de {var_graus}°C indica que está muito quente! 🌞')
    elif var_graus < 10:
        print(f'A temperatura de {var_graus}°C indica que está muito frio! ❄️')
    else:
        print(f'A temperatura de {var_graus}°C está agradável. 🌤️')
except ValueError:
    print('Entrada inválida! Por favor, digite apenas números.')
# Benefício: O programa não quebra caso alguém digite, por exemplo, "abc"..


#============================
# Versão compacta usando uma função
#
# Se quiser organizar melhor, pode transformar em função e reutilizar depois:.
def analisar_temperatura(temp):
    if temp > 30:
        return f'A temperatura de {temp}°C indica que está muito quente! 🌞'
    elif temp < 10:
        return f'A temperatura de {temp}°C indica que está muito frio! ❄️'
    else:
        return f'A temperatura de {temp}°C está agradável. 🌤️'

print('Programa que informa se está muito quente ou está frio')

try:
    var_graus = float(input('Digite a temperatura em Graus Celsius: '))
    print(analisar_temperatura(var_graus))
except ValueError:
    print('Entrada inválida! Por favor, digite apenas números.')

# Benefício: Seu código fica modular, ideal para programas maiores.