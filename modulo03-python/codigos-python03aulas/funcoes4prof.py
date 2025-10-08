# %%
def soma(pval: list):
    return sum(pval)


def media(ptotla:float, pqt: int):
    return ptotla / pqt

valores = [10, 20, 30 , 40, 50]

print(soma(valores))

print(media(soma(valores), len(valores)))





