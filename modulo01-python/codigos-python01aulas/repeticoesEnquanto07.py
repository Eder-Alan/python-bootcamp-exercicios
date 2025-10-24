var_capital     = 0
var_taxa        = 0
var_meses       = 0
var_contador    = 1
var_capitafinal = 0

var_capital = float(input('Digite o capital inicial R$ '))
var_taxa = float(input('Digite a taxa : '))
var_meses = int(input('Digite a quantidade de meses: '))
var_capitafinal = var_capital

while var_contador <= var_meses:
    var_capitafinal = var_capitafinal + var_capitafinal * var_taxa
    var_contador += 1
print(f'O capital inicial era de R$ {var_capital :.2f}')
print(f'A taxa era de: {var_taxa}%')
print(f'A quantidade de meses foi de: {var_meses}')
print(f'E o capital final será de R$ {var_capitafinal:.2f}')


