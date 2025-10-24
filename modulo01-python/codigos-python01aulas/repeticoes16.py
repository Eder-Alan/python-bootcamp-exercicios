# ========repetições while significa enquanto
# for que significa para controlado.
#=========================================
x = 1

while(x <= 10):
    print('---------------')
    x += 1

x = int(input('Digite o inicio da contagem: '))
while(x <= 10):
    print('---------------')
    x += 1

x = int(input('Digite o inicio do loop: '))
fim = int(input('Digite o fim do loop: '))
while(x <= fim):
    print('---------------')
    x += 1

print('Visualizando uma taboada')
inicio = int(input('Digite o inicio da taboada: '))
num = int(input('Digite o número da taboada: '))
fim = int(input('Digite o fim da taboada: '))

while(inicio <= fim):
    print(f'{num} X {inicio} = {num * inicio}')
    inicio += 1
