# ==========decisões
n1    = 0
n2    = 0
media = 0
ano   = 0

print('Programa que calcula média\n')
n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))
media = (n1 + n2) / 2

print('A média calculada é: ', media)
if(media >= 7):
    print('Aprovado')
    print('----------')
    ano = int(input('Digite o ano que você concluiu: '))
    if(ano == 3):
        print('Diplomado')
    else:
        print('Continue estudando')
elif (media >= 4):
    print('Nova prova')
else:
    print('Reprovado')

