var_n01   = 0
var_n02   = 0
var_media = 0
var_msgApr = "Aprovado"
var_msgRep = "Nova Prova"
print("Programa que calcula média")
var_n01 = input("\nDigite uma nota: ")
var_n02 = input("\nDigite outra nota: ")

var_media = (float(var_n01) + float(var_n02)) / 2
print(var_media)
if(var_media >= 7.0):
    print("---------------")
    print(var_msgApr)
else:
    print("================")
    print(var_msgRep)