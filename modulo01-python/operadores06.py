var_salario     = 0
var_faltas      = 0
varsalairo_novo = 0

var_salario = float(input("Digite o seu Salario R$ "))
var_faltas = int(input("Digite a quantidade de faltas: "))

if var_salario <= 2000 and var_faltas == 0:
    varsalairo_novo = var_salario * 1.10
    print(var_salario)
else:
    varsalairo_novo = var_salario

print(f' O salario final é : {varsalairo_novo:.2f}')