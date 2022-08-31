alfabeto = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def calculoHash(string, linha):
    hash = 0

    for letra in string:
        posicaoAlfabeto = alfabeto.index(letra)
        elementoEntrada = linha
        posicaoElemento = string.index(letra)

        hash += posicaoAlfabeto + elementoEntrada + posicaoElemento

    return hash


casosDeTeste = int(input())

for caso in range(casosDeTeste):
    linhasPorCaso = int(input())
    totalHash = 0

    for linha in range(linhasPorCaso):
        string = input()
        newString = string.lower()
        totalHash += calculoHash(newString, linha)

    print(totalHash)
