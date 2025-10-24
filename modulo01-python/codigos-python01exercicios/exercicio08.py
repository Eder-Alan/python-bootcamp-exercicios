# - Peça ao usuário para digitar um número e exiba a raiz
# quadrada desse número.
import math


var_resultado = 0.0
var_raiz = float(input('Digite um número: '))

var_resultado = var_raiz**(1/2)
print(f'A raiz do número: {var_raiz} é {var_resultado}')

var_resultado = math.sqrt(var_raiz)
print(f'A raiz do número: {var_raiz} é {var_resultado}')

# ==============
# Pequena melhoria: tratamento de erros
# Se o usuário digitar algo que não seja um número, o programa quebra.
# Podemos evitar isso com try e except:.

import math

try:
    var_raiz = float(input('Digite um número: '))

    if var_raiz < 0:
        print("❌ Erro: não existe raiz quadrada real para números negativos!")
    else:
        var_resultado = math.sqrt(var_raiz)
        print(f'A raiz do número {var_raiz} é {var_resultado:.2f}')
except ValueError:
    print("❌ Erro: digite um número válido!")
# Comportamentos agora:
#
# Se digitar texto → mostra mensagem amigável.
#
# Se digitar número negativo → alerta sobre raiz imaginária.
#
# Se digitar corretamente → calcula normalmente..