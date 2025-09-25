# - Peça ao usuário para digitar o preço unitário de um item (que pode ter
# casas decimais)e armazene-o em uma variável, garantindo que seja do tipo
# float. Imprima o preço digitado.

var_preco = float(input('Digite o preço do produto: '))
print(f'O preço do produto é: {var_preco}')

# ====================
# Pequena Melhoria: Formatar o valor como moeda
#
# Se o valor for exibido diretamente, pode sair algo como 19.9.
# Para deixá-lo mais bonito, você pode formatar para duas casas decimais,
# simulando um preço:.

var_preco = float(input('Digite o preço do produto: '))
print(f'O preço do produto é: R$ {var_preco:.2f}')

# Tratamento de erros (opcional)
#
# Assim como no caso dos alunos, se o usuário digitar algo que não seja número, o programa pode travar.
# Para evitar isso, podemos usar try e except:.

try:
    var_preco = float(input('Digite o preço do produto: '))
    print(f'O preço do produto é: R$ {var_preco:.2f}')
except ValueError:
    print("❌ Erro: digite um número válido, usando ponto para separar os centavos. Exemplo: 19.90")
