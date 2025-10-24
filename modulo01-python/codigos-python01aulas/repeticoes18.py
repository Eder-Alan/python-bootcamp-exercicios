# while True repetição verdadeiro
# este tipo de while garante que ele seja executado pelo menos 1 vez!!!
boleto_acum = 0

while True:
    boleto = float(input('Valor do Boleto: '))
    if(boleto == 0):
        break
    boleto_acum += boleto

print(f'Valor totol do Boleto a pagar: R$ {boleto_acum}')

# for que lê texto.

empresa = "escola"

for letra in (empresa):
    print(letra, end='')
print('')
# o end='' força a não imprimir uma linha.

empresa = "escola@gmail.com"
for letra in (empresa):
    if (letra == '@'):
        print('---------')
    else:
        print(letra)
