# - Peça ao usuário para digitar o turno em que estuda ('M' para manhã, 'N' para noite). Se
# for 'M', imprima "Bom dia!". Caso contrário (para qualquer outro valor,
# incluindo 'N'), imprima "Boa noite!".


print('Programa que imprime turno que estuda')
var_turno = str(input('Digite o turno que estudo: (M = Manhã / N = Noite) : ')).strip().upper()
if(var_turno == 'M'):
    print('Bom dia!')
else:
    print('Boa noite!')


# ============= melhorias
# Tratar entradas inválidas
#
# No seu código, se o usuário digitar outra letra (ex: X), ele
# automaticamente mostra "Boa noite!",
# o que pode confundir.
# Podemos melhorar com uma verificação extra:.
print('Programa que imprime turno que estuda')
var_turno = input('Digite o turno que você estuda [M = Manhã / N = Noite]: ').strip().upper()

if var_turno == 'M':
    print('Bom dia!')
elif var_turno == 'N':
    print('Boa noite!')
else:
    print('Turno inválido! Por favor, digite apenas M ou N.')

#==============================
# Versão compacta (usando dicionário)
#
# Se quiser algo mais enxuto e elegante, dá para usar um
# dicionário para mapear os turnos:.

print('Programa que imprime turno que estuda')

turnos = {
    'M': 'Bom dia!',
    'N': 'Boa noite!'
}

var_turno = input('Digite o turno que você estuda [M = Manhã / N = Noite]: ').strip().upper()
print(turnos.get(var_turno, 'Turno inválido! Digite M ou N.'))

