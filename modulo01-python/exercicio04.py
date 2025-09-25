# - Qual o resultado da expressão 10 + 6 * 2?
# Explique a ordem das operações.

print(f'O resultado de: 10 + 6 * 2 é {10 + 6 * 2}')
print(f'e o resultado de (10 + 6) * 2 {(10 + 6) * 2}')

# isto é chamdo de oredem de precedencia regras de precedencia:
# neste caso a ordem das operações é primeiro a multiplicação de
# depois a soma para que funcione corretamente devemos adicionar
# um par de parentese entre os números (10 + 6) e desta forma
# será feita a operação corretamente
# oredem de precendencia dos operadores aritiméticos sempre da
# esquerda para a direita
#
# Nível	Operador	Descrição	                Ordem
# 1️⃣	    ( )	         Parênteses – resolvem primeiro	Maior
# 2️⃣	** ou ^ (dependendo da linguagem)	Potência/Exponenciação	Esquerda → Direita (ou Direita → Esquerda, depende da linguagem)
# 3️⃣	*, /, %	Multiplicação, Divisão, Resto da divisão	Esquerda → Direita
# 4️⃣	+, -	Adição e Subtração	Esquerda → Direita
# 🔽		(outros operadores já não são aritméticos)	Menor
#
#
#
# Nos operadores lógicos a ordem de precedência também segue uma hierarquia, que pode variar levemente conforme a linguagem, mas na maioria (C, Java, Python, JavaScript) fica assim:
#
# Nível	Operador	Descrição	Ordem
# 1️⃣	! (C/Java/JS) ou not (Python)	Negação lógica (inverte o valor)	Maior
# 2️⃣	&& (C/Java/JS) ou and (Python)	Conjunção lógica (E)	Esquerda → Direita
# 3️⃣	`		(C/Java/JS) ou or` (Python).

# ============ com melhorias
# Programa para demonstrar ordem de precedência em expressões matemáticas

print(f'O resultado de 10 + 6 * 2 é: {10 + 6 * 2}')
print(f'O resultado de (10 + 6) * 2 é: {(10 + 6) * 2}')

# Explicação:
# Sem parênteses -> primeiro a multiplicação, depois a soma:
# 10 + 6 * 2
# 10 + 12 = 22
#
# Com parênteses -> primeiro resolve o que está dentro deles:
# (10 + 6) * 2
# 16 * 2 = 32

# Ordem de precedência dos operadores aritméticos no Python:
# 1️⃣ ( )    -> Parênteses (maior prioridade)
# 2️⃣ **     -> Potência
# 3️⃣ *, /, //, % -> Multiplicação, divisão, divisão inteira e resto
# 4️⃣ +, -   -> Adição e subtração

# Nos operadores lógicos:
# 1️⃣ not  -> Negação lógica
# 2️⃣ and  -> E lógico
# 3️⃣ or   -> OU lógico
