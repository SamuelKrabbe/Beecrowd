a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
if a == 0 or ((b**2) - (4 * a * c) < 0):
    print("Impossivel calcular")
else:
    import math

    r1 = ((-b) + math.sqrt((b**2) - (4 * a * c))) / (2 * a)
    r2 = ((-b) - math.sqrt((b**2) - (4 * a * c))) / (2 * a)
    print(f"R1 = {r1:.5f}\nR2 = {r2:.5f}")
