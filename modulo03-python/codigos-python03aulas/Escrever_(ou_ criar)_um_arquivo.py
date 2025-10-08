# %%
# Se quiser criar ou sobrescrever um arquivo:

with open("novo_arquivo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Segunda linha de texto.")


# 🔹 "w" = write (escrita) — cria ou substitui o arquivo.
# 🔹 "a" = append — adiciona conteúdo no final, 
# sem apagar o que já existe.




