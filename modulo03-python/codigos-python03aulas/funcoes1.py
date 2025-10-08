# %%
# uma função tradicional
def soma(nun1:float, num2:float)->float:
   
    return nun1 * num2
    
# entrada de valores, com verificação de número
try:
    var_num1 = float(input('Digite um número: '))
    print(var_num1)
except Exception as erro:
    print('Erro! Digite um número válido!!',erro)

try:
    var_num2 = float(input('Digite um número: '))
    print(var_num2)
except Exception as erro:
    print('Erro! Digite um número válido!!',erro)

# chamada da função
var_resultado = soma(var_num1, var_num2)
print(var_resultado)




