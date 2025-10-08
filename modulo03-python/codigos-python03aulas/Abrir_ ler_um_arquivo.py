# %%

# Abre o arquivo no modo de leitura ('r')
# O que é o with

# Em Python, o with é uma forma elegante e segura de 
# trabalhar com recursos externos, como:

# arquivos (open("arquivo.txt"))

# conexões de rede

# bancos de dados

# ou qualquer coisa que precise abrir e depois fechar..

with open("texto.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()  # Lê todo o conteúdo
    print(conteudo)


# Suponha que você tenha um arquivo chamado texto.txt no mesmo 
# diretório do seu código Python 
# O jeito mais comum de abrir e ler é usando a função open():.
# 
# 
# Explicação:

# with open(...) as arquivo: → abre o arquivo e fecha automaticamente ao 
# final (boa prática). "r" → modo de leitura (read).

# encoding="utf-8" → garante que acentos e caracteres especiais 
# apareçam corretamente.

# arquivo.read() → lê todo o texto de uma vez..



# | Modo  | Significado            | Explicação                                           |
# | ----- | ---------------------- | ---------------------------------------------------- |
# | `"r"` | **read**               | leitura (padrão) — o arquivo precisa existir         |
# | `"w"` | **write**              | escrita — cria ou apaga o conteúdo anterior          |
# | `"a"` | **append**             | adiciona conteúdo no final                           |
# | `"x"` | **exclusive creation** | cria novo, mas dá erro se já existir                 |
# | `"b"` | **binary**             | usado junto com outros, ex: `"rb"` (ler binário)     |
# | `"t"` | **text**               | modo texto (padrão) — geralmente nem precisa colocar |
# .

