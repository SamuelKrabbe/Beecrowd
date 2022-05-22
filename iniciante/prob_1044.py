# Lendo dois valores inteiros
a, b = map(int, input().split())

"""
Verificando se eles são multiplos:
Caso o resto da divisão do maior pelo menor for 0, 
então eles são multiplos, pois para serem multiplos 
a = b * k, sendo k um número inteiro
"""
if a >= b:
    if a % b == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
else:
    if b % a == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
