n = int(input())

for even in range(2, n + 1, 2):
    if even % 2 == 0:
        quad = even**2
        print(f"{even}^2 = {quad}")
    else:
        continue
