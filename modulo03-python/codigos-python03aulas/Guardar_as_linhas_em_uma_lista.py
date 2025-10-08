# %%
# Guardar as linhas em uma lista
with open("texto.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

print(linhas)



