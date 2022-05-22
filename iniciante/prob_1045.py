# lendo 3 valores float
x, y, z = map(float, input().split())

# Ordenando os 3 valores de forma decrescente
if x >= y and x >= z:
    a = x
    if y >= z:
        b = y
        c = z
    else:
        b = z
        c = y
elif y >= x and y >= z:
    a = y
    if x >= z:
        b = x
        c = z
    else:
        b = z
        c = x
elif z >= x and z >= y:
    a = z
    if y >= x:
        b = y
        c = x
    else:
        b = x
        c = y

"""
Verificando se os 3 valores lidos formam ou não um 
triângulo (se sim, qual a relação dos seus lados e ângulos)
"""
if a >= b + c:
    print("NAO FORMA TRIANGULO")

elif (a**2) == (b**2) + (c**2):
    print("TRIANGULO RETANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif (a == b != c) or (b == c != a) or (c == a != b):
        print("TRIANGULO ISOSCELES")
elif (a**2) > (b**2) + (c**2):
    print("TRIANGULO OBTUSANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif (a == b != c) or (b == c != a) or (c == a != b):
        print("TRIANGULO ISOSCELES")
elif (a**2) < (b**2) + (c**2):
    print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif (a == b != c) or (b == c != a) or (c == a != b):
        print("TRIANGULO ISOSCELES")
