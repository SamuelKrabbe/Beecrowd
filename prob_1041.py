# lendo coordenadas de um plano e transformando-as em float
x, y = map(float, input().split())

"""
Criando condicionais para verificar em qual quadrande 
o ponto se encontra: 
"""
# (se +y e +x, então Q1)
# (se +y e -x, então Q2)
# (se +y e x = 0, então Eixo Y)
# (se -y e +x, então Q4)
# (se -y e -x, então Q3)
# (se -y e x = 0, então Eixo Y)
# (se y = 0 e x != 0, então Eixo X)
# (se y = 0 e x = 0, então Origem)
if y > 0:
    if x > 0:
        print("Q1")
    elif x < 0:
        print("Q2")
    else:
        print("Eixo Y")
elif y < 0:
    if x > 0:
        print("Q4")
    elif x < 0:
        print("Q3")
    else:
        print("Eixo Y")
elif y == 0:
    if x == 0:
        print("Origem")
    else:
        print("Eixo X")
