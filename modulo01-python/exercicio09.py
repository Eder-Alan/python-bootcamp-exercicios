# Assunto: Booleano
# - Declare duas variáveis, valor_a = 15 e valor_b = 15. Verifique se valor_a é
# menor que valor_b Imprima o resultado booleano.

valor_a = 15
valor_b = 15

print(valor_a == valor_b)

# ============
# Melhorando a saída
#
# Podemos deixar a mensagem mais explicativa para o usuário:.
valor_a = 15
valor_b = 15

resultado = valor_a < valor_b
print(f"O valor_a ({valor_a}) é menor que o valor_b ({valor_b})? {resultado}")

# Comparações mais comuns em Python
# Operador	Significado	        Exemplo	  Resultado
# ==	    Igual a	            5 == 5	    True
# !=	    Diferente de	    5 != 3	    True
# <	        Menor que	        5 < 3	    False
# >	        Maior que	        5 > 3	    True
# <=	    Menor ou igual a	5 <= 5	    True
# >=	    Maior ou igual a	5 >= 6	    False.
