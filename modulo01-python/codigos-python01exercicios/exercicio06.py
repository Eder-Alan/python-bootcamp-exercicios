# - Peça ao usuário para digitar o número de alunos em uma turma e
# armazene-o em uma variável, garantindo que seja do tipo inteiro
# Em seguida, imprima o número de alunos.

var_alunos = int(input('Digite o número de alunos: '))
print(f'A quantidade de alunos desta turma é: {var_alunos}')

# ============== melhorias
# Se o usuário digitar algo que não seja um número, o código atual vai gerar um erro (ValueError).
# Podemos melhorar isso usando try e except para tornar o programa mais robusto.
# Exemplo:
#
# Como funciona esse código
#
# try → tenta executar o código normalmente.
#
# except ValueError → se o usuário digitar algo inválido (como letras),
# exibe uma mensagem amigável em vez de travar o programa.


try:
    var_alunos = int(input('Digite o número de alunos: '))
    print(f'A quantidade de alunos desta turma é: {var_alunos}')
except ValueError:
    print("❌ Erro: você deve digitar um número inteiro!")
