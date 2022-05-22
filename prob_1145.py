x, y = map(int, input().split())
n = 0
lim_max = y // x

for i in range(lim_max):
    for j in range(x):
        n += 1
        if j < (x - 1):
            print(n, end=" ")
        else:
            print(n)
