# video aula 06 modulo de python professor Ivan.
# ========== boleanos

var_boleana = 4 > 5

print(var_boleana)
print(type(var_boleana))

print(' 4 > 5 ', 4 > 5)
print(' 4 < 5 ', 4 < 5)
print(' 4 = 5 ', 4 == 5)
print(' 4 != 5 ', 4 != 5)
print('Ivan = Ivan', 'Ivan' == 'Ivan')
print('Ivan = Joao', 'Ivan' == 'Joao')
print('Ivan não Joao', 'Ivan' != 'Joao')

# ============= operadores relacionais
# and or

a = 5
b = 8
c = 4
print('Operador lógico E')
print(f'5 > 8 --> {5 > 8} E 5 < 4 --> {5 < 4} logo --> {(5 > 8) and (5 < 4)}')
print(f'5 > 8 --> {5 > 8} E 5 < 4 --> {5 > 4} logo --> {(5 > 8) and (5 < 4)}')
print(f'5 < 8 --> {5 < 8} E 5 > 4 --> {5 > 4} logo --> {(5 < 8) and (5 > 4)}')

print('\nOperador lógico OU')
print(f'5 > 8 --> {5 > 8} OU 5 < 4 --> {5 < 4} logo --> {(5 > 8) or (5 < 4)}')
print(f'5 > 8 --> {5 > 8} OU 5 > 4 --> {5 > 4} logo --> {(5 > 8) or (5 > 4)}')
print(f'5 < 8 --> {5 < 8} OU 5 > 4 --> {5 > 4} logo --> {(5 < 8) or (5 > 4)}')