x = [17,2]
print(x)

x.append(5)

print(x)

x.insert(1,30)

print(x)

total = len(x)
print(total)
print(sum(x))
print(max(x))
print(min(x))
print(sum(x) / len(x))
print(sorted(x))
lista_reversa = sorted(x, reverse= True)
print(lista_reversa)
# listas nome = [12, 25, 65] é mutavel
# tuplas nome = (12, 25, 65) é imutavél
# dicionário nomedicio = {'Nome':'Eder',
#                         'Curso': 'Engenharia de Software',
#                         'Profissao': 'Analista de Dados'}

nomelista = [12, 25, 65]
nometupla = (12, 25, 65)

nomedicio = {'Nome':'Eder',
             'Curso': 'Engenharia de Software',
             'Profissao': 'Analista de Dados'}

print(nomelista[0])
print(nometupla[2])
print(nomedicio.get('Nome')) # assim é mais segura evita erros
print(nomedicio['Nome'])     # assim também dá mas se digitar algo que tenha
                             # na chave dará erro

turma = {
    "curso": "Engenharia de Software",
    "alunos": [
        {"nome": "Eder", "idade": 25, "notas": (8, 9, 10)}, # aqui = 0
        {"nome": "Ana", "idade": 22, "notas": (7, 8, 9)}    # aqui = 1
    ]
}
# curso é uma chave e alunos também é uma chave
# "Engenharia de Software" é valor e o que tem dentro de alunos também
# dentro de alunos que é uma chave temos uma lista que contem dois
# dicionários e dentro destes dicionários temos uma tupla em cada um.
print(turma["alunos"][0]["nome"])   # Eder
print(turma["alunos"][1]["notas"][2])  # 9


print(type(nomelista))
print(type(nometupla))
print(type(nomedicio))