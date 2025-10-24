# - Um cliente tem direito a frete grátis se a compra for acima de 200
# reais e o cliente for cadastrado.
# Atribua a cliente_cadastrado o valor True
# Receba via input o total da compra.
# Armazene em frete_gratis a condição BOOLEANA se total_compra > 200 e
# cliente_cadastrado = True .
# Imprima o valor (booleano) da variável frete_gratis.

cliente_cadastrado = True

print('Programa que verifica frete gratis')
total_compra = float(input('Digite o valor Total da compra: R$ '))
if(total_compra > 200 and cliente_cadastrado):
    frete_gratis = True
    print(frete_gratis)
print('Fim do primeiro teste\n\n')
# ===========================================

frete_gratis = False

print('Programa que verifica frete gratis (em compras acima de R$200,00)')
total_compra = float(input('Digite o valor Total da compra: R$ '))
if(total_compra > 200 and cliente_cadastrado):
    frete_gratis = True
    print(frete_gratis)
else:
    print(frete_gratis)

# ========================
# Código simplificado e direto
#
# Podemos simplificar ainda mais e deixar o código mais limpo e profissional:.

cliente_cadastrado = True

print('Programa que verifica frete grátis (em compras acima de R$200,00)')
total_compra = float(input('Digite o valor total da compra: R$ '))

# Condição booleana direta
frete_gratis = total_compra > 200 and cliente_cadastrado

print(f"Frete grátis disponível? {frete_gratis}")

# =======================
# Melhorando a experiência do usuário
#
# Podemos ainda deixar o programa mais amigável:.
cliente_cadastrado = True

print('Programa que verifica frete grátis (em compras acima de R$200,00)')
total_compra = float(input('Digite o valor total da compra: R$ '))

frete_gratis = total_compra > 200 and cliente_cadastrado

if frete_gratis:
    print("✅ Parabéns! Você ganhou frete grátis!")
else:
    print("❌ Infelizmente você não tem direito a frete grátis.")
