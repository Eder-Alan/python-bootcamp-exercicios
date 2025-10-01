# Dicionários (Dictionaries)
# Dicionários funcionam com pares de chave e valor, definidos por chaves {}.
# As chaves devem ser únicas e são usadas para acessar os dados, não a posição
# numérica. Exercício: Crie um dicionário chamado aluno contendo chaves para nome,
# idade e curso. Imprima o nome do aluno acessando-o diretamente pela chave.

aluno = { 'nome': 'Carlos',
         'idade': 35,
         'curso': 'Engenharia de Software'}


print(aluno['nome'])
print('\n==========================================')


# ============ exercicios adicionais para praticar e testar
# usando listas dentro de um dicionário para armazenar vários alunos.
aluno = { 'nome': ['Carlos', 'Marcelo','Alberto', 'Pedro'],
         'idade': [28, 33, 45, 50],
         'curso': ['Engenharia de Software',
                   'Analise de Dados',
                   'Analise e desenvolvimento de Sistemas',
                   'Analiste de Redes']}

# imprime o primeiro aluno
print(aluno['nome'][0])

# imprime o terceiro aluno.
print(aluno['nome'][2])

#imprime a idade do quarto aluno
print(aluno['idade'][3])

#imprime nome idade e curos do segundo aluno
registro = 1
print(aluno['nome'][registro],
      aluno['idade'][registro],
      aluno['curso'][registro])

# uma outra forma de imprimmir na tela.
nome = aluno['nome'][registro]
idade = aluno['idade'][registro]
curso = aluno['curso'][registro]

print(f'O nome do aluno(a) é: {nome}, idade: {idade}, curso: {curso}')