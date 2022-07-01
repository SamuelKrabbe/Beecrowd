values = input().split()
a, b, c = values
a = float(a)
b = float(b)
c = float(c)

# B = base| H = height| rad = radius| S = side| rec = rectangle| trap = trapezium
area_rectriangle_BaHc = (a * c) / 2
area_circle_radc = 3.14159 * (c**2)
area_trap_BaBbHc = ((a + b) * c) / 2
area_square_Sb = b * b
area_rec_Sab = a * b

print(f"TRIANGULO: {area_rectriangle_BaHc:.3f}")
print(f"CIRCULO: {area_circle_radc:.3f}")
print(f"TRAPEZIO: {area_trap_BaBbHc:.3f}")
print(f"QUADRADO: {area_square_Sb:.3f}")
print(f"RETANGULO: {area_rec_Sab:.3f}")
