# Lendo 3 valores reais
a, b, c = map(float, input().split())

# Verificando se esses 3 valores podem formar um triângulo
"""
Dados três segmentos de reta, se a soma das medidas de dois 
deles é sempre maior que a medida do terceiro, então, 
eles podem formar um triângulo
"""
if a + b > c and b + c > a and c + a > b:
    perimetro_tri = a + b + c
    print(f"Perimetro = {perimetro_tri:.1f}")
else:
    """
    Caso não forme um triângulo, calcular a área de um
    trapézio com a e b como base e c como altura
    """
    area_trap = ((a + b) * c) / 2
    print(f"Area = {area_trap:.1f}")
