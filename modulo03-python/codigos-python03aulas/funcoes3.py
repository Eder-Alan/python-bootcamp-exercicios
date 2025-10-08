# %%

# Função que calcula a soma de uma lista de números.
# Recebe uma lista de floats e retorna o total somado.
def calcular_soma(valores: list[float]) -> float:
    return sum(valores)


# Função que calcula a média aritmética.
# Recebe o total e a quantidade de elementos e retorna a média.
def calcular_media(total: float, quantidade: int) -> float:
    return total / quantidade


# Cria uma lista vazia para armazenar os números informados pelo usuário.
numeros = []

# Loop infinito para solicitar os números até que o usuário digite 0.
while True:
    try:
        # Lê o valor digitado e converte para float.
        valor = float(input("Digite um número (0 para sair): "))
        
        # Se o valor for 0, o programa interrompe a entrada de dados.
        if valor == 0:
            break

        # Adiciona o número digitado na lista.
        numeros.append(valor)

    # Trata erro caso o usuário digite algo que não seja número.
    except ValueError:
        print("Por favor, digite um número válido.")


# Após sair do loop, verifica se há números na lista antes de calcular.
if numeros:
    # Calcula a soma dos números usando a função calcular_soma().
    total = calcular_soma(numeros)

    # Calcula a média dos números usando a função calcular_media().
    media_valores = calcular_media(total, len(numeros))

    # Exibe os resultados formatados na tela.
    print(f"\nNúmeros digitados: {numeros}")
    print(f"Soma: {total:.2f}")
    print(f"Média: {media_valores:.2f}")

# Caso o usuário não tenha digitado nenhum número (só 0), informa isso.
else:
    print("Nenhum número foi informado.")

