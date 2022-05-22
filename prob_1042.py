# Lendo 3 variáveis
a, b, c = map(int, input().split())

"""
Operções condicionais para ver qual variável é maior que qual, em cada possibilidade imprimir as 3 variáveis na ordem crescente (menor pro maior)
"""
if a <= b and a <= c:
    print(a)
    if b <= c:
        print(b)
        print(c)
    else:
        print(c)
        print(b)
elif b <= a and b <= c:
    print(b)
    if a <= c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)
else:
    print(c)
    if b <= a:
        print(b)
        print(a)
    else:
        print(a)
        print(b)

"""Imprimindo as variáveis na ordem que foram 
lidas no começo do programa
"""
print("")
print(a)
print(b)
print(c)
