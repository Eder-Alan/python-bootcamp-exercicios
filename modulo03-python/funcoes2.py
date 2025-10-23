# %%
def soma(var1:int, var2:int, var3:int)->int:
    return var1 + var2 + var3

def media(vartotal:float, varqnant:int)->float:
    return vartotal / varqnant

try:
    var_num1 = int(input('Digite um número: '))
except Exception as erro:
    print('Erro', erro)

try:
    var_num2 = int(input('Digite um número: '))
except Exception as erro:
    print('Erro', erro)

try:
    var_num3 = int(input('Digite um número: '))
except Exception as erro:
    print('Erro', erro)

# chamando a função soma
vartot = soma(var_num1, var_num2, var_num3)
print(vartot)

# chamando a função media
varmedi = media(soma(var_num1, var_num2, var_num3),3)
print(varmedi)

# também é possível chamar função dentro de um print
# que também é uma função.
print(media(soma(var_num1, var_num2, var_num3),3))


