a, b, c = map(int, input().split())

if a >= b + c or b >= a + c or c >= a + b:
    validity = "Invalido"
    print(validity)
else:
    validity = "Valido"
    if (a**2) == (b**2) + (c**2):
        ret = "S"
    else:
        ret = "N"
    if a == b == c:
        tipo = "Equilatero"
    elif (a == b and a != c) or (b == a and b != c) or (c == a and c != b):
        tipo = "Isoceles"
    else:
        tipo = "Escaleno"

    print(f"{validity}-{tipo}")
    print(f"Retangulo: {ret}")
