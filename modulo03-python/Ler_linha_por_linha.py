# %%
# Se quiser ler linha por linha, use:

with open("texto.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())  # strip() remove quebras de linha


# Resultado: uma lista onde 
# cada item é uma linha do arquivo.

