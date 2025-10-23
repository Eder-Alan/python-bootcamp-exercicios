var_n01   = 0
var_n02   = 0
var_media = 0
var_ano   = 0
var_msgDipl   = "Diplomado"
var_msgNoDipl = "Continue Estudando"
var_msgApr    = "Aprovado"
var_msgRep    = "Nova Prova"
print("Programa que calcula média")
var_n01 = float(input("\nDigite uma nota: "))
var_n02 = float(input("\nDigite outra nota: "))

var_media = (var_n01 + var_n02) / 2
print(var_media)
if(var_media >= 7.0):
    print("---------------")
    print(var_msgApr)
    var_ano = int(input("\nDigite o ano que foi conluido: "))
    if(var_ano == 3):
        print(var_msgDipl)
    else:
        print(var_msgNoDipl)
else:
    print("================")
    print(var_msgRep)