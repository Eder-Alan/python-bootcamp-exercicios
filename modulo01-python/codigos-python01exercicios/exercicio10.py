# Declare palavra1 = "Olá" e palavra2 = "olá".
# Verifique se palavra1 é igual a palavra2 e se palavra1 é diferente de palavra2.
# Imprima os resultados das duas comparacoes (booleanos TRUE ou FALSE ).

palavra1 = "Olá"
palavra2 = "olá"

print(palavra1 == palavra2)
print(palavra1 != palavra2)

# =============
# Melhorando a saída
#
# Podemos deixar a saída mais descritiva usando f-strings:.
palavra1 = "Olá"
palavra2 = "olá"

print(f"As palavras são iguais? {palavra1 == palavra2}")
print(f"As palavras são diferentes? {palavra1 != palavra2}")


# Dica: Ignorar diferenças de maiúsculas/minúsculas
# Se o objetivo for comparar apenas o conteúdo, sem se
# importar com maiúsculas e minúsculas, podemos padronizar ambas as
# palavras com .lower() ou .upper().

palavra1 = "Olá"
palavra2 = "olá"

print(palavra1.lower() == palavra2.lower())  # Agora será True
