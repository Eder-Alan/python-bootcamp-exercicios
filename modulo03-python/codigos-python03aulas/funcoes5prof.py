# %%
def soma(nome:str, *argumentos:float):
    print('Quem me chamou: ', nome)
    return sum(*argumentos)


def media(ptotla:float, pqt: int):
    return ptotla / pqt

valores = [10, 20, 30 , 40, 50]

print(soma('Jonas',valores))

print(media(soma('Jonas',valores), len(valores)))





