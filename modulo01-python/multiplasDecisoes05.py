var_produto = ""
var_valor = 0
var_estado = ""
var_frete = 0
print("Programa que calcula frete")
var_produto = str(input("Qual é o produto: ")).strip().upper()
var_valor = float(input("Qual o valor do produto: R$ "))
var_estado = str(input("Qual é o estado de entrega: ")).strip().upper()


# match var_estado:
#     case "SP":
#         var_frete = var_frete + var_valor * 1.10
#     case "RJ":
#         var_frete = var_frete + var_valor * 1.15
#     case "MG":
#         var_frete = var_frete + var_valor * 1.17
#
# if(var_frete == 0):
#     print("\nNão entregamos")
# else:
#     print("O prodututo é: ", var_produto)
#     print("O valor     é:  R$", var_valor)
#     print("O estado    é: ", var_estado)
#     print("O valor do frete é: R$ {:.1f}".format(var_frete))

# outra opção:

if(var_estado == "SP"):
    var_frete = var_frete + var_valor * 1.10
elif(var_estado == "RJ"):
    var_frete = var_frete + var_valor * 1.15
elif(var_estado == "MG"):
    var_frete = var_frete + var_valor * 1.17

if(var_frete == 0):
    print("\nNão entregamos")
else:
    print("O prodututo é: ", var_produto)
    print("O valor     é:  R$", var_valor)
    print("O estado    é: ", var_estado)
    print("O valor do frete é: R$ {:.1f}".format(var_frete))
