s = 0
n = 1

for i in range(1, 40, 2):
    s += i / n
    n *= 2

print(f"{s:.2f}")
