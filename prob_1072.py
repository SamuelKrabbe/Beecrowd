n = int(input())
dentro = 0
fora = 0

for numbers in range(n):
    x = int(input())
    if 10 <= x <= 20:
        dentro += 1
    else:
        fora += 1
print(f"{dentro} in\n{fora} out")
