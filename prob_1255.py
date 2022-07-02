n = int(input())

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


def oraganizacaoString(string):
    """
    Organizando os caracteres
    """
    new_string = ""
    string = string.strip()
    string = string.lower()

    for caractere in string:
        if caractere in alfabeto:
            new_string += caractere
    return new_string


for i in range(n):
    string = input()
    new_string = oraganizacaoString(string)

    """
    Colocando a frequência de cada letra em uma lista e colocando a com maior frequencia em um variável
    """
    lista_frequencia = []

    for letra in new_string:
        frequencia_letra = new_string.count(letra)
        lista_frequencia.append(frequencia_letra)

    maior_frequencia = max(lista_frequencia)

    """
    Verificando se existem letras com a mesma frequencia e imprimindo elas
    """
    maior_frequencia_letra = ""

    for j in range(len(lista_frequencia)):
        if lista_frequencia[j] == maior_frequencia:
            if new_string[j] not in maior_frequencia_letra:
                maior_frequencia_letra += new_string[j]

    print(maior_frequencia_letra)
